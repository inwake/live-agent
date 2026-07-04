from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from ableton_live_client import LiveBridgeClient  # noqa: E402
from ableton_live_client.orm import LiveSet  # noqa: E402
from ableton_mcp_server.server import _capability_report_markdown  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate CAPABILITY_REPORT.md from a Live bridge scan.")
    parser.add_argument("--host", default=os.getenv("ABLETON_BRIDGE_HOST", "127.0.0.1"))
    parser.add_argument("--port", type=int, default=int(os.getenv("ABLETON_BRIDGE_PORT", "9877")))
    parser.add_argument("--token", default=os.getenv("ABLETON_BRIDGE_TOKEN"))
    parser.add_argument("--output", default="CAPABILITY_REPORT.md")
    args = parser.parse_args()

    live_set = LiveSet(LiveBridgeClient(host=args.host, port=args.port, token=args.token))
    data = live_set.inspect_capabilities()
    markdown = _capability_report_markdown(data)
    output_path = Path(args.output)
    output_path.write_text(markdown, encoding="utf-8")
    print(str(output_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
