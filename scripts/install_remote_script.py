from __future__ import annotations

import os
import shutil
from pathlib import Path


def default_user_library() -> Path:
    # Override with ABLETON_USER_LIBRARY when needed.
    override = os.getenv("ABLETON_USER_LIBRARY")
    if override:
        return Path(override)
    return Path.home() / "Documents" / "Ableton" / "User Library"


def main() -> None:
    repo = Path(__file__).resolve().parents[1]
    src = repo / "remote_scripts" / "AbletonLiveBridge"
    dst = default_user_library() / "Remote Scripts" / "AbletonLiveBridge"
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)
    print(f"Installed Remote Script to: {dst}")
    print("Restart Live, then select AbletonLiveBridge as a Control Surface in Live preferences.")


if __name__ == "__main__":
    main()
