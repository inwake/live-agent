from __future__ import annotations

import os
from ableton_live_client import LiveBridgeClient


def main() -> None:
    client = LiveBridgeClient(token=os.getenv("ABLETON_BRIDGE_TOKEN"), timeout=30.0)
    print(client.call("song.scan"))


if __name__ == "__main__":
    main()
