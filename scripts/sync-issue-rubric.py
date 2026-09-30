#!/usr/bin/env python3
"""Copy the canonical issue rubric into every file that uses it.

Usage:
  python3 scripts/sync-issue-rubric.py          # write the copies
  python3 scripts/sync-issue-rubric.py --check  # exit 1 if any copy is out of date
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SOURCE = ROOT / "rubric" / "issue-rubric.md"
BEGIN = "<!-- BEGIN ISSUE-RUBRIC: generated from rubric/issue-rubric.md, do not edit here -->"
END = "<!-- END ISSUE-RUBRIC -->"
EMBEDDED = [ROOT / "prompts" / "issue-evaluator.md"]
SKILL_COPIES = [
    ROOT / "skills" / "draft-issue" / "issue-rubric.md",
    ROOT / "skills" / "implement-issue" / "issue-rubric.md",
]
SKILL_HEADER = (
    "<!-- Generated from rubric/issue-rubric.md in the Prompt Engineering Toolkit. "
    "Edit the source and run scripts/sync-issue-rubric.py. -->\n\n"
    "# Implementation Plan Issue Rubric\n\n"
)


def rubric_body():
    text = SOURCE.read_text(encoding="utf-8")
    # Drop the maintainer comment at the top of the source file.
    return re.sub(r"\A<!--.*?-->\s*", "", text, flags=re.S).rstrip() + "\n"


def expected(path, body):
    if path in SKILL_COPIES:
        return SKILL_HEADER + body
    current = path.read_text(encoding="utf-8")
    pattern = re.compile(re.escape(BEGIN) + r".*?" + re.escape(END), re.S)
    if not pattern.search(current):
        sys.exit(f"{path.relative_to(ROOT)}: rubric markers not found")
    return pattern.sub(lambda _: f"{BEGIN}\n\n{body}\n{END}", current, count=1)


def main():
    check = "--check" in sys.argv[1:]
    body = rubric_body()
    stale = []
    for path in EMBEDDED + SKILL_COPIES:
        want = expected(path, body)
        have = path.read_text(encoding="utf-8") if path.exists() else None
        if have != want:
            stale.append(path.relative_to(ROOT))
            if not check:
                path.write_text(want, encoding="utf-8")
    if check and stale:
        print("Out of date with rubric/issue-rubric.md:")
        for p in stale:
            print(f"  {p}")
        print("Run: python3 scripts/sync-issue-rubric.py")
        return 1
    print("Updated: " + ", ".join(map(str, stale)) if stale else "All rubric copies are up to date.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
