import os
import sys
import json
from pathlib import Path
from colorama import init, Fore, Style
import anthropic

SCRIPT_DIR = Path(__file__).resolve().parent
CONFIG_DIR = SCRIPT_DIR.parent.parent / "config"

init()


def _load_env():
    """Load API keys from .env files."""
    for env_path in [SCRIPT_DIR / ".env", CONFIG_DIR / "gemini.local.env"]:
        if env_path.exists():
            with open(env_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        k, v = line.split("=", 1)
                        os.environ.setdefault(k.strip(), v.strip().strip('"\''))


def _get_gemini_client():
    """Initialize google-genai client (same SDK as call_gemini.py)."""
    _load_env()
    api_key = os.environ.get("GOOGLE_API_KEY", "")
    if not api_key:
        print(f"{Fore.RED}Error: GOOGLE_API_KEY not set in config/gemini.local.env{Style.RESET_ALL}")
        sys.exit(1)
    from google import genai
    return genai.Client(api_key=api_key)


GEMINI_MODEL = os.environ.get("ORCHESTRATOR_GEMINI_MODEL", "gemini-3.1-pro")


class TriadOrchestrator:
    def __init__(self, project_dir: str):
        self.project_dir = Path(project_dir)

        _load_env()
        self.anthropic_api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not self.anthropic_api_key:
            print(f"{Fore.RED}Error: Missing ANTHROPIC_API_KEY in .env{Style.RESET_ALL}")
            sys.exit(1)

        self.gemini_client = _get_gemini_client()
        self.anthropic_client = anthropic.Anthropic(api_key=self.anthropic_api_key)

        print(f"{Fore.CYAN}Initializing Triad Orchestrator for: {self.project_dir}{Style.RESET_ALL}")

    def run_architect(self, user_prompt: str) -> str:
        """
        Gemini (Lead Architect)
        Generates the markdown specification based on user request.
        """
        print(f"{Fore.YELLOW}[Architect]{Style.RESET_ALL} Designing specification via Gemini ({GEMINI_MODEL})...")

        system = (
            "You are the Lead Architect in a Triad AI system. Output ONLY a Markdown "
            "specification containing the file names and the logic for the feature "
            "requested by the user. Do NOT write full code, just the architecture spec. "
            "THE TRIAD EVOLUTION DIRECTIVE: You must actively consider the capabilities "
            "of the entire AI Fleet (Claude Code subagents, ChatGPT API, Gemini API, "
            "Claude API, Codex CLI) and design the smartest, fastest, and cheapest "
            "architecture possible. Explicitly communicate how to best utilize the "
            "other AIs in your spec."
        )
        prompt = f"Design a spec for the following requirement: {user_prompt}"

        try:
            response = self.gemini_client.models.generate_content(
                model=GEMINI_MODEL,
                contents=prompt,
                config={
                    "system_instruction": system,
                    "temperature": 0.3,
                    "max_output_tokens": 8192,
                },
            )
            spec_content = response.text or "(Gemini returned empty response)"
        except Exception as e:
            print(f"{Fore.YELLOW}[Architect]{Style.RESET_ALL} API Error: {e}")
            spec_content = f"**ERROR**: Architect call failed: {e}"

        print(f"{Fore.YELLOW}[Architect]{Style.RESET_ALL} Specification drafted.")
        return spec_content

    def run_executor(self, spec_content: str) -> list[str]:
        """
        Claude (Frontline Executor)
        Analyzes the spec and returns a list of files that would be modified.
        """
        print(f"{Fore.GREEN}[Executor]{Style.RESET_ALL} Analyzing spec for implementation plan...")

        response = self.anthropic_client.messages.create(
            model="claude-opus-4-7",
            max_tokens=4096,
            system="You are the Frontline Executor in a Triad AI system. Your job is to read the markdown specification from the Architect and return a JSON list of file paths that you theoretically would have modified based on the spec. Focus on practical VoxCore project structure.",
            messages=[
                {"role": "user", "content": f"Here is the Architect's specification:\n\n{spec_content}\n\nBased on this spec, which files would you edit? Return ONLY a valid JSON array of strings representing file paths (e.g., [\"src/main.py\"])."}
            ]
        )
        
        try:
            # Parse the response to extract the JSON array
            content = response.content[0].text
            # Basic cleanup in case Claude added markdown backticks
            if content.startswith("```json"):
                content = content[7:-3]
            elif content.startswith("```"):
                content = content[3:-3]
            modified_files = json.loads(content.strip())
        except Exception as e:
            print(f"{Fore.RED}[Executor] Failed to parse modified files list: {e}{Style.RESET_ALL}")
            modified_files = []
            
        print(f"{Fore.GREEN}[Executor]{Style.RESET_ALL} Modified files: {modified_files}")
        return modified_files

    def run_auditor(self, spec_content: str, modified_files: list[str]) -> tuple[bool, str]:
        """
        Gemini (Backend Auditor)
        Audits modified files against the spec. Returns (passed, reason).
        """
        print(f"{Fore.MAGENTA}[Auditor]{Style.RESET_ALL} Verifying implementation plan against spec...")

        file_list_str = ", ".join(modified_files) if modified_files else "(none)"
        prompt = (
            f"Original Specification:\n{spec_content}\n\n"
            f"Modified Files:\n{file_list_str}\n\n"
            f"Do these modified files accurately reflect everything the spec demanded? "
            f"Reply with ONLY 'PASS' or 'FAIL' followed by a one-line reason."
        )

        try:
            response = self.gemini_client.models.generate_content(
                model=GEMINI_MODEL,
                contents=prompt,
                config={
                    "system_instruction": (
                        "You are the Backend Auditor in a Triad AI system. "
                        "Review whether the Executor's file list matches the Architect's spec. "
                        "Reply with ONLY 'PASS' or 'FAIL' followed by a one-line reason."
                    ),
                    "temperature": 0.1,
                    "max_output_tokens": 256,
                },
            )
            result = (response.text or "").strip()
        except Exception as e:
            reason = f"Gemini API error: {e}"
            print(f"{Fore.RED}[Auditor] {reason}{Style.RESET_ALL}")
            return False, reason

        result_upper = result.upper()
        if "PASS" in result_upper:
            return True, result
        elif "FAIL" in result_upper:
            return False, result
        else:
            print(f"{Fore.RED}[Auditor] Invalid output: {result}. Defaulting to FAIL.{Style.RESET_ALL}")
            return False, result

    def orchestrate(self, user_prompt: str):
        print(f"\n{Fore.BLUE}=== Starting Triad Pipeline ==={Style.RESET_ALL}")
        print(f"Goal: {user_prompt}\n")

        spec = self.run_architect(user_prompt)

        max_attempts = 3
        attempt = 1
        success = False
        prior_feedback = ""

        while attempt <= max_attempts and not success:
            print(f"\n{Fore.BLUE}--- Iteration {attempt}/{max_attempts} ---{Style.RESET_ALL}")

            executor_prompt = spec
            if prior_feedback:
                executor_prompt += (
                    f"\n\n## Prior Auditor Feedback (fix these issues):\n{prior_feedback}"
                )

            modified_files = self.run_executor(executor_prompt)
            success, reason = self.run_auditor(spec, modified_files)

            if success:
                print(f"\n{Fore.GREEN}[SUCCESS] Auditor Approved! Pipeline Complete.{Style.RESET_ALL}")
            else:
                prior_feedback = reason
                print(f"\n{Fore.RED}[FAILED] Auditor: {reason}{Style.RESET_ALL}")
                print(f"{Fore.RED}Sending feedback to Executor for retry...{Style.RESET_ALL}")
                attempt += 1

        if not success:
            print(f"\n{Fore.RED}Pipeline aborted after {max_attempts} failed attempts.{Style.RESET_ALL}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python orchestrator.py \"<your feature request>\"")
        sys.exit(1)
    
    prompt = " ".join(sys.argv[1:])
    orchestrator = TriadOrchestrator(os.getcwd())
    orchestrator.orchestrate(prompt)
