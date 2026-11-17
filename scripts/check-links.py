"""Check relative Markdown paths and heading fragments in the tracked vault."""
import re
import subprocess
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"!?\[[^\]\n]+\]\(([^\s)]+)\)")
HEADING = re.compile(r"^#{1,6}\s+(.+?)\s*$", re.MULTILINE)
CODE = re.compile(r"^```[^\n]*\n.*?^```\s*$", re.MULTILINE | re.DOTALL)


def markdown_headings(path):
    content = CODE.sub("", path.read_text(encoding="utf-8"))
    return {
        re.sub(r"[^\w -]", "", title.lower()).replace(" ", "-")
        for title in HEADING.findall(content)
    }


def main():
    tracked = subprocess.check_output(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z", "--", "*.md"],
        cwd=ROOT,
    )
    notes = sorted({ROOT / name.decode() for name in tracked.split(b"\0") if name})
    errors = []

    for note in notes:
        if not note.is_file():
            errors.append(f"Missing note: {note.relative_to(ROOT)}")
            continue

        content = CODE.sub("", note.read_text(encoding="utf-8"))
        for match in LINK.finditer(content):
            link = urlsplit(match.group(1))
            if link.scheme or link.netloc:
                continue

            path = unquote(link.path)
            target = (note.parent / path).resolve() if path else note
            heading = unquote(link.fragment)
            if not target.is_relative_to(ROOT) or not target.exists():
                errors.append(f"{note.relative_to(ROOT)}: missing target {match.group(1)}")
            elif heading and target.suffix == ".md" and heading not in markdown_headings(target):
                errors.append(f"{note.relative_to(ROOT)}: missing heading {match.group(1)}")

    if errors:
        print("\n".join(errors))
        return 1

    print(f"Checked relative links in {len(notes)} Markdown files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
