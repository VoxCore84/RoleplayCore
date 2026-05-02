#!/usr/bin/env python3
"""LegalBench harness — run Stanford's legal reasoning benchmark against VoxCore's stack.

Downloads benchmark tasks from HuggingFace, runs them through local LLM (Qwen 27B)
or Ollama, scores against gold answers, and reports results comparable to published
baselines.

LegalBench has 162 tasks across 6 categories:
  - Issue spotting
  - Rule application
  - Rule conclusion
  - Interpretation
  - Rhetorical understanding
  - Practice-specific (contracts, evidence, civil procedure)

We start with a curated subset of high-signal tasks most relevant to legal AI
capability claims. Expand later.

Usage:
    python tools/legalbench_harness.py                     # run default task set
    python tools/legalbench_harness.py --tasks contract_qa rule_qa
    python tools/legalbench_harness.py --list-tasks        # show available tasks
    python tools/legalbench_harness.py --model qwen3.5:27b-q4_K_M  # specify model
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
REPORT_DIR = REPO_ROOT / "AI_Studio" / "Reports" / "scheduled"
OLLAMA_URL = "http://localhost:11434"
DEFAULT_MODEL = "qwen3.5:27b-q4_K_M"

CLOUD_MODELS = {
    "opus": "claude-opus-4-20250514",
    "sonnet": "claude-sonnet-4-20250514",
    "haiku": "claude-haiku-4-5-20251001",
    "gpt4": "gpt-4o",
}

DEFAULT_TASKS = [
    "contract_qa",
    "rule_qa",
    "citation_prediction_classification",
    "contract_nli_confidentiality_of_agreement",
    "contract_nli_explicit_identification",
    "learned_hands_benefits",
    "learned_hands_courts",
    "definition_extraction",
    "hearsay",
    "diversity_1",
]


def list_available_tasks():
    """Print all known LegalBench tasks."""
    try:
        from datasets import list_datasets
    except ImportError:
        pass

    known_tasks = [
        "abercrombie", "canada_tax_court_outcomes", "citation_prediction_classification",
        "citation_prediction_open", "consumer_contracts_qa", "contract_nli_confidentiality_of_agreement",
        "contract_nli_explicit_identification", "contract_nli_inclusion_of_verbatim_terms",
        "contract_nli_limited_use", "contract_nli_no_licensing", "contract_nli_notice_on_compelled_disclosure",
        "contract_nli_permissible_acquirement_of_similar_information",
        "contract_nli_permissible_copy", "contract_nli_permissible_development_of_similar_information",
        "contract_nli_permissible_post_agreement_possession", "contract_nli_return_of_confidential_information",
        "contract_nli_sharing_with_employees", "contract_nli_sharing_with_third_parties",
        "contract_nli_survival_of_obligations", "contract_qa",
        "corporate_lobbying", "cuad_affiliate_license",
        "definition_classification", "definition_extraction",
        "diversity_1", "diversity_2", "diversity_3", "diversity_4", "diversity_5", "diversity_6",
        "function_of_decision_section", "hearsay",
        "international_citizenship_questions",
        "learned_hands_benefits", "learned_hands_business",
        "learned_hands_consumer", "learned_hands_courts",
        "learned_hands_crime", "learned_hands_divorce",
        "learned_hands_domestic_violence", "learned_hands_education",
        "learned_hands_employment", "learned_hands_estates",
        "learned_hands_family", "learned_hands_health",
        "learned_hands_housing", "learned_hands_immigration",
        "learned_hands_torts", "learned_hands_traffic",
        "legal_reasoning_causality",
        "maud_ability_to_consummate",
        "oral_argument_question_purpose",
        "overruling", "proa",
        "rule_qa",
        "scalr", "sara_entailment",
        "successor_liability", "supply_chain_disclosure",
        "telemarketing_sales_rule",
        "textualism_tool_dictionaries", "textualism_tool_plain",
        "unfair_tos",
    ]
    print(f"Known LegalBench tasks: {len(known_tasks)}")
    for t in sorted(known_tasks):
        print(f"  {t}")


def load_task(task_name: str) -> list[dict]:
    """Load a LegalBench task from HuggingFace."""
    from datasets import load_dataset

    ds = load_dataset("nguha/legalbench", task_name, split="test")
    return [dict(row) for row in ds]


def _load_anthropic_key() -> str:
    """Load ANTHROPIC_API_KEY from env or tools/ai_studio/.env."""
    key = os.environ.get("ANTHROPIC_API_KEY", "")
    if key:
        return key
    env_file = REPO_ROOT / "tools" / "ai_studio" / ".env"
    if env_file.exists():
        for line in env_file.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if "=" in line and not line.startswith("#"):
                k, _, v = line.partition("=")
                if k.strip() == "ANTHROPIC_API_KEY":
                    return v.strip().strip("\"'")
    return ""


def query_claude(prompt: str, model: str = "claude-sonnet-4-20250514", max_tokens: int = 256) -> str:
    """Query Anthropic Claude API."""
    api_key = _load_anthropic_key()
    if not api_key:
        return "ERROR: ANTHROPIC_API_KEY not set"

    payload = json.dumps({
        "model": model,
        "max_tokens": max_tokens,
        "messages": [{"role": "user", "content": prompt}],
    }).encode("utf-8")

    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=payload,
        headers={
            "Content-Type": "application/json",
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            blocks = result.get("content", [])
            return "".join(b.get("text", "") for b in blocks).strip()
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")[:200]
        return f"ERROR: HTTP {e.code} — {body}"
    except Exception as e:
        return f"ERROR: {e}"


def query_model(prompt: str, model: str = DEFAULT_MODEL, max_tokens: int = 256) -> str:
    """Route to the right backend based on model name."""
    resolved = CLOUD_MODELS.get(model, model)
    if resolved.startswith("claude-"):
        return query_claude(prompt, model=resolved, max_tokens=max_tokens)
    return query_ollama(prompt, model=resolved, max_tokens=max_tokens)


def query_ollama(prompt: str, model: str = DEFAULT_MODEL, max_tokens: int = 256) -> str:
    """Query local Ollama model. Handles Qwen's thinking/response split."""
    payload = json.dumps({
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {"num_predict": max_tokens, "temperature": 0.1},
    }).encode("utf-8")

    req = urllib.request.Request(
        f"{OLLAMA_URL}/api/generate",
        data=payload,
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            response = result.get("response", "").strip()
            if response:
                return response
            thinking = result.get("thinking", "").strip()
            if thinking:
                lines = [l.strip() for l in thinking.split("\n") if l.strip()]
                for line in reversed(lines):
                    clean = line.strip("*- .>#")
                    cl = clean.lower()
                    if cl in ("yes", "no", "yes.", "no."):
                        return clean
                    if cl.startswith(("the answer is", "answer:", "conclusion:", "**answer")):
                        after = clean.split(":", 1)[-1].strip().strip("*. ") if ":" in clean else clean
                        return after
                    if cl.startswith("yes") and len(cl) < 60:
                        return clean
                    if cl.startswith("no") and len(cl) < 60 and not cl.startswith("not"):
                        return clean
                for line in lines:
                    clean = line.strip("*- .>#")
                    cl = clean.lower()
                    if cl.startswith(("yes", "no")) and len(cl) < 60 and not cl.startswith("not"):
                        return clean
                return lines[-1].strip("*- .>#") if lines else ""
            return ""
    except Exception as e:
        return f"ERROR: {e}"


def _is_binary_task(task_name: str) -> bool:
    """Tasks where the gold answer is always Yes or No."""
    return task_name in {
        "contract_qa", "citation_prediction_classification", "hearsay",
        "diversity_1", "diversity_2", "diversity_3", "diversity_4",
        "diversity_5", "diversity_6", "overruling", "successor_liability",
        "unfair_tos", "corporate_lobbying", "abercrombie",
        "contract_nli_confidentiality_of_agreement",
        "contract_nli_explicit_identification",
        "contract_nli_inclusion_of_verbatim_terms",
        "contract_nli_limited_use", "contract_nli_no_licensing",
        "contract_nli_notice_on_compelled_disclosure",
        "contract_nli_permissible_acquirement_of_similar_information",
        "contract_nli_permissible_copy",
        "contract_nli_permissible_development_of_similar_information",
        "contract_nli_permissible_post_agreement_possession",
        "contract_nli_return_of_confidential_information",
        "contract_nli_sharing_with_employees",
        "contract_nli_sharing_with_third_parties",
        "contract_nli_survival_of_obligations",
        "learned_hands_benefits", "learned_hands_business",
        "learned_hands_consumer", "learned_hands_courts",
        "learned_hands_crime", "learned_hands_divorce",
        "learned_hands_domestic_violence", "learned_hands_education",
        "learned_hands_employment", "learned_hands_estates",
        "learned_hands_family", "learned_hands_health",
        "learned_hands_housing", "learned_hands_immigration",
        "learned_hands_torts", "learned_hands_traffic",
    }


def build_prompt(task_name: str, example: dict) -> str:
    """Build a task-appropriate prompt for the LLM."""
    binary = _is_binary_task(task_name)
    strict = "\n\nYou MUST respond with ONLY the single word 'Yes' or 'No'. Nothing else." if binary else ""

    if "question" in example and "text" in example:
        return (
            f"Read the following legal text and answer the question.\n\n"
            f"Text: {example['text']}\n\n"
            f"Question: {example['question']}{strict}"
        )
    elif "text" in example and "answer" in example and "doctrine" in example:
        return (
            f"Answer the following legal question about {example.get('doctrine', 'law')}.\n\n"
            f"Question: {example['text']}\n\n"
            f"Provide a concise answer in 1-2 sentences."
        )
    elif "text" in example and "citation" in example:
        return (
            f"Does the following legal text cite or reference the case '{example['citation']}'?\n\n"
            f"Text: {example['text']}{strict}"
        )
    else:
        text_field = example.get("text", example.get("question", ""))
        return (
            f"Answer the following legal question.\n\n"
            f"{text_field}{strict}"
        )


def normalize_answer(answer: str) -> str:
    """Normalize an answer for comparison."""
    answer = answer.strip().lower()
    answer = answer.split("\n")[0].strip()
    answer = answer.strip(".,;:!?\"'`")

    if answer.startswith("yes"):
        return "yes"
    if answer.startswith("no"):
        return "no"
    return answer[:200]


def score_answer(predicted: str, gold: str, task_name: str) -> bool:
    """String-match score (legacy, used for binary tasks)."""
    pred_norm = normalize_answer(predicted)
    gold_norm = normalize_answer(gold)

    if gold_norm in ("yes", "no"):
        return pred_norm == gold_norm

    return gold_norm in pred_norm or pred_norm in gold_norm


# Tasks where string-match systematically under-scores correct answers because
# the model's wording diverges from the gold (e.g., "28 USC § 1367" vs
# "28 U.S.C. § 1367", citation phrasings, multi-sentence rule statements).
# These get the LLM-as-judge wrapper when --judge is enabled.
FREE_TEXT_TASKS = {
    "rule_qa",
    "citation_prediction_open",
    "citation_prediction_classification",
}


JUDGE_SYSTEM = (
    "You are a LegalBench answer judge. Decide whether the PREDICTED answer is "
    "semantically equivalent to or correctly entails the GOLD answer for the "
    "given legal question. On the FIRST line output exactly one token: "
    "CORRECT or INCORRECT. On the SECOND line write a one-sentence reason "
    "(<= 25 words). Do not output thinking tags or anything else."
)

JUDGE_USER = (
    "QUESTION (LegalBench task: {task}):\n{question}\n\n"
    "GOLD ANSWER:\n{gold}\n\n"
    "PREDICTED ANSWER:\n{predicted}\n\n"
    "Verdict on line 1, reason on line 2."
)


def _judge_via_ollama(question: str, predicted: str, gold: str, task: str,
                      model: str = "gemma4:26b") -> tuple[bool, str]:
    """Ask local Ollama for CORRECT/INCORRECT. Returns (is_correct, reason)."""
    import json as _json
    import urllib.request
    body = _json.dumps({
        "model": model,
        "messages": [
            {"role": "system", "content": JUDGE_SYSTEM},
            {"role": "user", "content": JUDGE_USER.format(
                task=task, question=question, gold=gold, predicted=predicted,
            )},
        ],
        "stream": False,
        "options": {"temperature": 0.0},
    }).encode("utf-8")
    req = urllib.request.Request(
        "http://localhost:11434/api/chat",
        data=body, headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            payload = _json.loads(resp.read())
    except Exception as e:
        return (False, f"judge_ollama_error: {e}")
    text = (payload.get("message", {}).get("content", "") or "").strip()
    upper = text.upper()
    if "CORRECT" in upper.split("\n", 1)[0] and "INCORRECT" not in upper.split("\n", 1)[0]:
        verdict = True
    elif "INCORRECT" in upper.split("\n", 1)[0]:
        verdict = False
    else:
        verdict = False
    # Extract reason from second line
    lines = text.splitlines()
    reason = lines[1].strip() if len(lines) > 1 else text[:200]
    return (verdict, reason[:200])


def _judge_via_claude(question: str, predicted: str, gold: str, task: str,
                       model: str = "claude-opus-4-7") -> tuple[bool, str]:
    """Ask Claude API for CORRECT/INCORRECT. Returns (is_correct, reason).

    Mirrors _judge_via_ollama's interface so callers can swap backends
    via --judge-backend ollama|claude.
    """
    import json as _json
    import os
    import urllib.request

    api_key = os.environ.get("ANTHROPIC_API_KEY", "").strip()
    if not api_key:
        # Fallback: load from tools/ai_studio/.env (same pattern as
        # citation_scorer.py and the synthesizers)
        env_path = Path(__file__).resolve().parent / "ai_studio" / ".env"
        if env_path.exists():
            for line in env_path.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if line.startswith("ANTHROPIC_API_KEY"):
                    api_key = line.partition("=")[2].strip().strip('"').strip("'")
                    break
    if not api_key:
        return (False, "judge_claude_error: ANTHROPIC_API_KEY not set")

    body = _json.dumps({
        "model": model,
        "max_tokens": 200,
        "system": JUDGE_SYSTEM,
        "messages": [
            {"role": "user", "content": JUDGE_USER.format(
                task=task, question=question, gold=gold, predicted=predicted,
            )},
        ],
    }).encode("utf-8")
    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=body,
        headers={
            "Content-Type": "application/json",
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            payload = _json.loads(resp.read())
    except Exception as e:
        return (False, f"judge_claude_error: {e}")
    text = ""
    for block in payload.get("content", []):
        if block.get("type") == "text":
            text += block.get("text", "")
    text = text.strip()
    upper = text.upper()
    if "CORRECT" in upper.split("\n", 1)[0] and "INCORRECT" not in upper.split("\n", 1)[0]:
        verdict = True
    elif "INCORRECT" in upper.split("\n", 1)[0]:
        verdict = False
    else:
        verdict = False
    lines = text.splitlines()
    reason = lines[1].strip() if len(lines) > 1 else text[:200]
    return (verdict, reason[:200])


def score_answer_with_judge(question: str, predicted: str, gold: str, task_name: str,
                             judge_model: str = "gemma4:26b",
                             judge_backend: str = "ollama") -> tuple[bool, str]:
    """Hybrid scorer: string-match for binary tasks, LLM-as-judge for free-text tasks."""
    gold_norm = normalize_answer(gold)
    if gold_norm in ("yes", "no"):
        # Binary task — string match is the right scorer
        return (score_answer(predicted, gold, task_name), "string-match (binary)")
    if task_name in FREE_TEXT_TASKS:
        if judge_backend == "claude":
            return _judge_via_claude(question, predicted, gold, task_name, model=judge_model)
        return _judge_via_ollama(question, predicted, gold, task_name, model=judge_model)
    # Default fallback for any other task type
    return (score_answer(predicted, gold, task_name), "string-match (default)")


def run_task(task_name: str, model: str, max_examples: int = 50,
             use_judge: bool = False, judge_model: str = "gemma4:26b",
             judge_backend: str = "ollama") -> dict:
    """Run a single LegalBench task and return results.

    When ``use_judge`` is True, free-text tasks (rule_qa, citation_prediction_*)
    are scored via LLM-as-judge instead of string match.
    """
    print(f"\n  Loading {task_name}...", end=" ", flush=True)
    try:
        examples = load_task(task_name)
    except Exception as e:
        print(f"FAILED: {e}")
        return {"task": task_name, "error": str(e)}

    examples = examples[:max_examples]
    scoring = f"judge-{judge_backend}" if (use_judge and task_name in FREE_TEXT_TASKS) else "string-match"
    print(f"{len(examples)} examples, scoring={scoring}", flush=True)

    correct = 0
    total = 0
    results = []

    for i, ex in enumerate(examples):
        prompt = build_prompt(task_name, ex)
        predicted = query_model(prompt, model=model)
        gold = ex.get("answer", "")
        if use_judge:
            is_correct, reason = score_answer_with_judge(
                ex.get("text", "") or prompt, predicted, gold, task_name,
                judge_model=judge_model, judge_backend=judge_backend,
            )
        else:
            is_correct = score_answer(predicted, gold, task_name)
            reason = ""

        if is_correct:
            correct += 1
        total += 1

        results.append({
            "index": ex.get("index", i),
            "predicted": predicted[:200],
            "gold": gold[:200],
            "correct": is_correct,
            "judge_reason": reason if use_judge else None,
        })

        if (i + 1) % 10 == 0:
            print(f"    {i+1}/{len(examples)} ({correct}/{total} correct)", flush=True)

    accuracy = correct / total if total > 0 else 0
    print(f"  {task_name}: {correct}/{total} = {accuracy:.1%}  ({scoring})")

    return {
        "task": task_name,
        "correct": correct,
        "total": total,
        "accuracy": round(accuracy, 4),
        "scoring": scoring,
        "results": results,
    }


def main():
    parser = argparse.ArgumentParser(description="LegalBench harness for VoxCore")
    parser.add_argument("--tasks", nargs="+", default=None, help="Tasks to run")
    parser.add_argument("--list-tasks", action="store_true", help="List available tasks")
    parser.add_argument("--model", default=DEFAULT_MODEL, help="Ollama model to use")
    parser.add_argument("--max-examples", type=int, default=50, help="Max examples per task")
    parser.add_argument("--output", help="Output JSON file")
    parser.add_argument("--judge", action="store_true",
                        help="Use LLM-as-judge for free-text tasks (rule_qa, citation_prediction_*)")
    parser.add_argument("--judge-model", default="gemma4:26b",
                        help="Judge model id. Default gemma4:26b (Ollama). For Claude judge use e.g. claude-opus-4-7.")
    parser.add_argument("--judge-backend", choices=["ollama", "claude"], default="ollama",
                        help="Judge backend: 'ollama' (free, default) or 'claude' (API, more accurate)")
    args = parser.parse_args()

    if args.list_tasks:
        list_available_tasks()
        return

    tasks = args.tasks or DEFAULT_TASKS
    print(f"=== LegalBench Harness ===")
    print(f"Model: {args.model}")
    print(f"Tasks: {len(tasks)}")
    print(f"Max examples per task: {args.max_examples}")

    all_results = []
    total_correct = 0
    total_count = 0
    t0 = time.time()

    for task in tasks:
        result = run_task(
            task, args.model, args.max_examples,
            use_judge=args.judge, judge_model=args.judge_model,
            judge_backend=args.judge_backend,
        )
        all_results.append(result)
        if "error" not in result:
            total_correct += result["correct"]
            total_count += result["total"]

    elapsed = time.time() - t0
    overall_accuracy = total_correct / total_count if total_count > 0 else 0

    print(f"\n=== SUMMARY ===")
    print(f"  Tasks run: {len(all_results)}")
    print(f"  Total examples: {total_count}")
    print(f"  Overall accuracy: {total_correct}/{total_count} = {overall_accuracy:.1%}")
    print(f"  Elapsed: {elapsed:.0f}s")
    print()

    for r in all_results:
        if "error" in r:
            print(f"  {r['task']}: ERROR - {r['error']}")
        else:
            print(f"  {r['task']}: {r['accuracy']:.1%} ({r['correct']}/{r['total']})")

    report = {
        "date": time.strftime("%Y-%m-%d %H:%M:%S"),
        "model": args.model,
        "overall_accuracy": round(overall_accuracy, 4),
        "total_correct": total_correct,
        "total_count": total_count,
        "elapsed_seconds": round(elapsed, 1),
        "tasks": all_results,
    }

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    ts = time.strftime("%Y%m%d_%H%M%S")
    report_path = args.output or str(REPORT_DIR / f"legalbench_{ts}.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"\n  Report: {report_path}")


if __name__ == "__main__":
    main()
