from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path


REPO_URL = re.compile(r"https://github[.]com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)")


def catalog_files(root: Path) -> list[Path]:
    catalog_dir = root / "catalog"
    files = []
    for path in catalog_dir.iterdir():
        if path.is_file() and path.suffix == ".md" and path.name[:2].isdigit():
            files.append(path)
    return sorted(files)


def find_repos(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    repos = []
    for owner, name in REPO_URL.findall(text):
        repos.append(f"{owner}/{name}")
    return repos


def check_remote(repo: str) -> bool:
    result = subprocess.run(
        ["gh", "repo", "view", repo, "--json", "nameWithOwner"],
        capture_output=True,
        text=True,
        check=False,
    )
    return result.returncode == 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--remote", action="store_true")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    failures = []
    total = 0

    for path in catalog_files(root):
        repos = find_repos(path)
        if not repos:
            failures.append(f"{path.name}: no repositories found")
            continue
        total += len(repos)
        seen = set()
        for repo in repos:
            if repo in seen:
                failures.append(f"{path.name}: duplicate {repo}")
            seen.add(repo)
            if args.remote and not check_remote(repo):
                failures.append(f"{path.name}: remote check failed {repo}")

    if failures:
        for failure in failures:
            print(failure)
        return 1

    mode = "remote" if args.remote else "local"
    print(f"{mode} validation passed for {total} repositories")
    return 0


if __name__ == "__main__":
    sys.exit(main())

