# a0-prompt-builder

Workflow skill for native apps built with current a0.dev.

The new edition keeps the useful mobile vocabulary from the original and adds the missing production layer: `.a0/build.yaml`, runtime versions, upgrades, OTA compatibility, deep links, push delivery, native IPA/APK testing, accessibility and store release safety.

## Evidence ladder

```text
web preview -> a0/Expo preview -> native build -> beta channel -> production
```

Each layer proves different things. The skill never calls a web preview a native validation.

## Verification

```bash
python3 scripts/validate_skill.py
```
