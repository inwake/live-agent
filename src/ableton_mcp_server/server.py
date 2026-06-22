from __future__ import annotations

import os
from mcp.server.fastmcp import FastMCP

from ableton_live_client import LiveBridgeClient
from ableton_live_client.orm import LiveSet

mcp = FastMCP("ableton-live-mcp")
client = LiveBridgeClient(
    host=os.getenv("ABLETON_BRIDGE_HOST", "127.0.0.1"),
    port=int(os.getenv("ABLETON_BRIDGE_PORT", "9877")),
    token=os.getenv("ABLETON_BRIDGE_TOKEN"),
)
live_set = LiveSet(client)


@mcp.tool()
def scan_live_set() -> dict:
    """Return a structured summary of the current Ableton Live set."""
    return live_set.scan()


@mcp.tool()
def get_arrangement_clips(track_ref: str | None = None) -> dict:
    """Return Arrangement clips for one track or all tracks."""
    return live_set.arrangement_clips(track_ref)


@mcp.tool()
def get_clip_notes(clip_ref: str, from_time: float | None = None, time_span: float | None = None, from_pitch: int | None = None, pitch_span: int | None = None) -> dict:
    """Return MIDI notes from a clip. Works for MIDI clips; returns typed error for non-MIDI clips."""
    return live_set.clip_notes(
        clip_ref,
        from_time=from_time,
        time_span=time_span,
        from_pitch=from_pitch,
        pitch_span=pitch_span,
    )


@mcp.tool()
def get_track_devices(track_ref: str) -> dict:
    """Return devices on a track."""
    return live_set.devices(track_ref)


@mcp.tool()
def get_device_parameters(device_ref: str) -> dict:
    """Return exposed Live DeviceParameter objects for a device."""
    return live_set.device_parameters(device_ref)


if __name__ == "__main__":
    mcp.run()
