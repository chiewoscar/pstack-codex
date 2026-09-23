"""Check the public pstack for Codex archive without third-party dependencies."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "pstack-codex"


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    catalog = read_json(ROOT / ".agents" / "plugins" / "marketplace.json")
    assert catalog["name"] == "pstack-codex"
    assert len(catalog["plugins"]) == 1
    entry = catalog["plugins"][0]
    assert entry["name"] == "pstack-codex"
    assert entry["source"] == {"source": "local", "path": "./plugins/pstack-codex"}
    assert entry["policy"] == {"installation": "AVAILABLE", "authentication": "ON_INSTALL"}
    assert (ROOT / entry["source"]["path"]).resolve() == PLUGIN

    portable = read_json(PLUGIN / "plugin.json")
    codex = read_json(PLUGIN / ".codex-plugin" / "plugin.json")
    assert portable["name"] == codex["name"] == "pstack-codex"
    assert portable["version"] == codex["version"]
    assert portable["repository"] == codex["repository"]
    assert portable["license"] == codex["license"] == "MIT"
    assert codex["skills"] == "./skills/"
    assert (PLUGIN / codex["interface"]["composerIcon"]).is_file()
    assert (PLUGIN / codex["interface"]["logo"]).is_file()
    assert (PLUGIN / "assets" / "icon.png").read_bytes() == (PLUGIN / "assets" / "logo.png").read_bytes()

    skills = sorted((PLUGIN / "skills").glob("*/SKILL.md"))
    assert len(skills) == 47, f"Expected 47 skills, found {len(skills)}"
    for skill in skills:
        lines = skill.read_text(encoding="utf-8-sig").splitlines()
        assert lines[0] == "---", skill
        assert f"name: {skill.parent.name}" in lines[:12], skill
        assert any(line.startswith("description:") for line in lines[:12]), skill
    assert len(list((PLUGIN / "skills" / "principle-fix-root-causes").parent.glob("principle-*/SKILL.md"))) == 23
    assert len(list((PLUGIN / "skills" / "poteto-mode" / "playbooks").glob("*.md"))) == 23
    assert not any("benny" in path.name.lower() for path in ROOT.rglob("*"))

    public_docs = (
        ROOT / "README.md",
        ROOT / "README.zh-CN.md",
        ROOT / "NOTICE.md",
        ROOT / "LICENSE",
        PLUGIN / "README.md",
        PLUGIN / "README.zh-CN.md",
        PLUGIN / "NOTICE.md",
        PLUGIN / "LICENSE",
        PLUGIN / "third_party" / "cursor-team-kit-LICENSE",
        PLUGIN / "references" / "codex-runtime.md",
        PLUGIN / "docs" / "test-report.md",
        PLUGIN / "docs" / "execution-parity.md",
    )
    for path in public_docs:
        assert path.is_file(), path
        if path.suffix == ".md":
            for target in re.findall(r"\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
                if target.startswith(("https://", "http://", "#", "mailto:")):
                    continue
                local_target = target.split("#", 1)[0]
                assert (path.parent / local_target).exists(), f"Broken link in {path}: {target}"

    for path in (ROOT / "README.md", ROOT / "README.zh-CN.md", PLUGIN / "README.md", PLUGIN / "README.zh-CN.md"):
        content = path.read_text(encoding="utf-8")
        assert len(content.strip()) > 1000, f"README is empty or truncated: {path}"
        assert "codex plugin add pstack-codex@pstack-codex" in content, path

    print(f"OK: {len(skills)} skills, 23 playbooks, 23 principles, manifests, licenses, and marketplace")


if __name__ == "__main__":
    main()
