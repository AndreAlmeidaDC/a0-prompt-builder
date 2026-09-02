#!/usr/bin/env python3
from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parents[1]
REQ=["SKILL.md","README.md","CHANGELOG.md","metadata.json","references/vibecode-core.md","references/platform-a0dev.md","references/version-check.md","references/archetypes.md","references/accessibility-mobile.md","templates/BUILD_RUNTIME_SPEC.md"]
def fail(x): print("FAIL:",x); raise SystemExit(1)
def main():
    missing=[p for p in REQ if not (ROOT/p).exists()]
    if missing: fail("missing: "+", ".join(missing))
    meta=json.loads((ROOT/"metadata.json").read_text()); version=str(meta.get("version",""))
    if not re.fullmatch(r"\d{4}\.\d{2}\.\d{2}",version): fail("bad version")
    if meta.get("origin_url")!="https://github.com/AndreAlmeidaDC/a0-prompt-builder": fail("wrong origin")
    text="\n".join((ROOT/p).read_text() for p in REQ if p.endswith(".md"))
    for token in [version,"runtimeVersion","build.yaml","OTA","deep links","push","IPA","APK","VoiceOver","TalkBack"]:
        if token.lower() not in text.lower(): fail("missing concept: "+token)
    stale=["SEO / GEO","Em apps mobile nativos (a0.dev), esta referência não se aplica","Apple Developer ($99/ano)","harness-engineering-coding-agent/main/metadata.json"]
    for value in stale:
        if value.lower() in text.lower(): fail("stale claim: "+value)
    print(f"Validation passed. version={version}")
if __name__=="__main__": main()
