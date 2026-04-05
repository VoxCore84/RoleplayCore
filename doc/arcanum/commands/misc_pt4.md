---
title: "Miscellaneous Commands -- Arcanum Wiki (Part 4/8)"
description: "miscellaneous commands — /help /exit /copy /vim /voice /keybindings /feedback /release-notes /plan /tag /summary /env /bughunter /tasks /status /rewind /statusline"
tags: [commands]
part: 4
parts: 8
---

### /feedback
- **Aliases**: `/bug`
- **Arguments**: `[report]`
- **What it does**: Submits feedback about Claude Code. Opens a feedback form or directly submits a bug report with the provided text.
- **Feature gating**: Disabled in many contexts:
  - Bedrock users
  - Vertex users
  - Foundry users
  - `DISABLE_FEEDBACK_COMMAND` or `DISABLE_BUG_COMMAND` env vars
  - Essential-traffic-only privacy mode
  - Anthropic employees (`USER_TYPE === 'ant'` -- they use internal channels)
  - When `allow_product_feedback` policy is not allowed
- **Key code**:
```typescript
const feedback = {
  aliases: ['bug'],
  type: 'local-jsx',
  name: 'feedback',
  description: 'Submit feedback about Claude Code',
  argumentHint: '[report]',
  isEnabled: () => !(
    isEnvTruthy(process.env.CLAUDE_CODE_USE_BEDROCK) ||
    isEnvTruthy(process.env.CLAUDE_CODE_USE_VERTEX) ||
    isEnvTruthy(process.env.CLAUDE_CODE_USE_FOUNDRY) ||
    isEnvTruthy(process.env.DISABLE_FEEDBACK_COMMAND) ||
    isEnvTruthy(process.env.DISABLE_BUG_COMMAND) ||
    isEssentialTrafficOnly() ||
    process.env.USER_TYPE === 'ant' ||
    !isPolicyAllowed('allow_product_feedback')
  ),
}
```

---

### /release-notes
- **Arguments**: None
- **What it does**: Displays the release notes for the current version of Claude Code. Shows what changed in the latest update.
- **Feature gating**: None -- always available. Supports non-interactive mode.
- **Key code**:
```typescript
const releaseNotes: Command = {
  description: 'View release notes',
  name: 'release-notes',
  type: 'local',
  supportsNonInteractive: true,
}
```

---

---
[Part 1](misc_pt1.md) | [Part 2](misc_pt2.md) | [Part 3](misc_pt3.md) | **Part 4** | [Part 5](misc_pt5.md) | [Part 6](misc_pt6.md) | [Part 7](misc_pt7.md) | [Part 8](misc_pt8.md)
