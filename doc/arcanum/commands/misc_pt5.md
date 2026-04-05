---
title: "Miscellaneous Commands -- Arcanum Wiki (Part 5/8)"
description: "miscellaneous commands — /help /exit /copy /vim /voice /keybindings /feedback /release-notes /plan /tag /summary /env /bughunter /tasks /status /rewind /statusline"
tags: [commands]
part: 5
parts: 8
---

### /plan
- **Arguments**: `[open|<description>]`
- **What it does**: Enables plan mode or views the current session plan. Plan mode structures the conversation around a specific goal with tracked progress. The underlying "ultraplan" feature can:
  - Create structured plans with steps
  - Track completion status
  - Optionally teleport to a remote environment for complex multi-agent exploration (30-minute timeout)
  - Use Claude Code on the web (CCR) for deeper analysis

  The standalone ultraplan (`ultraplan.tsx`) implements the remote planning flow:
  1. Checks remote agent eligibility
  2. Reads a prompt template from a file
  3. Teleports to a cloud environment
  4. Polls for plan approval (30-min timeout)
  5. Archives the remote session when done
- **Feature gating**: Basic plan mode is always available. Ultraplan remote features require GrowthBook flags and remote session policy.
- **Key code**:
```typescript
const plan = {
  type: 'local-jsx',
  name: 'plan',
  description: 'Enable plan mode or view the current session plan',
  argumentHint: '[open|<description>]',
}
```

---

### /tag
- **Arguments**: `<tag-name>`
- **What it does**: Toggles a searchable tag on the current session. Tags make it easier to find specific sessions later. This is a labeling/categorization system.
- **Feature gating**: Only enabled for Anthropic employees (`USER_TYPE === 'ant'`).
- **Key code**:
```typescript
const tag = {
  type: 'local-jsx',
  name: 'tag',
  description: 'Toggle a searchable tag on the current session',
  isEnabled: () => process.env.USER_TYPE === 'ant',
  argumentHint: '<tag-name>',
}
```

---

### /summary
- **Arguments**: Unknown (stubbed)
- **What it does**: STUBBED OUT. Was likely a conversation summary generator.
- **Feature gating**: `isEnabled: () => false`, `isHidden: true`

---

### /env
- **Arguments**: Unknown (stubbed)
- **What it does**: STUBBED OUT. Was likely for displaying environment variables or configuration.
- **Feature gating**: `isEnabled: () => false`, `isHidden: true`

---

### /onboarding
- **Arguments**: Unknown (stubbed)
- **What it does**: STUBBED OUT. Was likely the initial user onboarding flow.
- **Feature gating**: `isEnabled: () => false`, `isHidden: true`

---

---
[Part 1](misc_pt1.md) | [Part 2](misc_pt2.md) | [Part 3](misc_pt3.md) | [Part 4](misc_pt4.md) | **Part 5** | [Part 6](misc_pt6.md) | [Part 7](misc_pt7.md) | [Part 8](misc_pt8.md)
