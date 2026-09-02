---
name: a0-prompt-builder
description: >
  Guides planning, building, testing, upgrading and releasing native iOS and Android apps with the current a0.dev platform. Use when the user mentions a0.dev, a0 runtime, Expo mobile preview, IPA/APK, OTA updates, deep links, push notifications, Convex, App Store or Play Store. Inspect runtime and build state before generating prompts.
license: MIT
---

# a0 Prompt Builder

This skill is mobile-native. It treats web preview, quick mobile preview, native builds, OTA and store release as different evidence layers.

## Origin version check

Canonical source:

```text
https://github.com/AndreAlmeidaDC/a0-prompt-builder
```

At meaningful use, follow `references/version-check.md`. Never self-update silently.

## Load order

1. Read `references/vibecode-core.md`.
2. Read `references/platform-a0dev.md`.
3. Read `references/accessibility-mobile.md` for any user-facing app.
4. Use `references/archetypes.md` only if platform choice is open.

## Non-negotiable boundaries

- Use screens, navigation, safe areas, permissions and builds — not web page/SEO vocabulary.
- Inspect `.a0/build.yaml`, runtime version, deployed updates and store builds before changing native behavior.
- OTA only within a compatible runtime.
- Web preview and Expo/a0 preview cannot validate every native feature.
- Never request unnecessary permissions.
- Do not deploy OTA, create/submit builds, upload credentials, process payment or change store production without explicit approval.

## Output

Return only the needed artifact: mobile project knowledge, screen flow, permission map, build/runtime spec, planning prompt, atomic implementation prompt, native test plan, OTA decision or store release checklist.

## Change history

| Date | Version | Change |
|---|---|---|
| 2026-09-02 | 2026.09.02 | Added runtime/build engineering, OTA boundaries, deep links, push, native test matrix, mobile accessibility and store release gates. |
