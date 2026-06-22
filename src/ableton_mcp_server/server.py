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
def get_audio_clip_warp_markers(clip_ref: str) -> dict:
    """Return audio warp markers for an Arrangement audio clip."""
    return live_set.audio_clip_warp_markers(clip_ref)


@mcp.tool()
def get_track_devices(track_ref: str) -> dict:
    """Return devices on a track."""
    return live_set.devices(track_ref)


@mcp.tool()
def get_device_parameters(device_ref: str) -> dict:
    """Return exposed Live DeviceParameter objects for a device."""
    return live_set.device_parameters(device_ref)


@mcp.tool()
def get_selected_context() -> dict:
    """Return the selected track, detail clip, selected device, and selected parameter."""
    return live_set.selected_context()


def _scan() -> dict:
    return live_set.scan()


def _find_track(summary: dict, track_ref: str) -> dict:
    for track in summary.get("tracks", []):
        if track.get("ref") == track_ref:
            return track
    for track in summary.get("return_tracks", []):
        if track.get("ref") == track_ref:
            return track
    master_track = summary.get("master_track")
    if master_track and master_track.get("ref") == track_ref:
        return master_track
    return {"ref": track_ref, "error": {"code": "OBJECT_NOT_FOUND", "message": "Track not found"}}


@mcp.resource("ableton://live/version")
def live_version_resource() -> dict:
    """Return Ableton Live version metadata."""
    return _scan().get("application", {})


@mcp.resource("ableton://set/summary")
def set_summary_resource() -> dict:
    """Return a structured summary of the current Live set."""
    return _scan()


@mcp.resource("ableton://set/transport")
def set_transport_resource() -> dict:
    """Return transport and timeline state for the current Live set."""
    summary = _scan()
    return {
        "tempo": summary.get("tempo"),
        "current_song_time": summary.get("current_song_time"),
        "is_playing": summary.get("is_playing"),
        "loop": summary.get("loop"),
        "loop_start": summary.get("loop_start"),
        "loop_length": summary.get("loop_length"),
        "signature_numerator": summary.get("signature_numerator"),
        "signature_denominator": summary.get("signature_denominator"),
    }


@mcp.resource("ableton://tracks")
def tracks_resource() -> dict:
    """Return track, return-track, and master-track summaries."""
    summary = _scan()
    return {
        "tracks": summary.get("tracks", []),
        "return_tracks": summary.get("return_tracks", []),
        "master_track": summary.get("master_track"),
    }


@mcp.resource("ableton://track/{track_ref}")
def track_resource(track_ref: str) -> dict:
    """Return one track summary by path reference."""
    return _find_track(_scan(), track_ref)


@mcp.resource("ableton://track/{track_ref}/arrangement")
def track_arrangement_resource(track_ref: str) -> dict:
    """Return Arrangement clips for one track."""
    return live_set.arrangement_clips(track_ref)


@mcp.resource("ableton://track/{track_ref}/devices")
def track_devices_resource(track_ref: str) -> dict:
    """Return devices for one track."""
    return live_set.devices(track_ref)


@mcp.resource("ableton://clip/{clip_ref}")
def clip_resource(clip_ref: str) -> dict:
    """Return one Arrangement clip by path reference."""
    return live_set.clip(clip_ref)


@mcp.resource("ableton://clip/{clip_ref}/notes")
def clip_notes_resource(clip_ref: str) -> dict:
    """Return MIDI notes for one Arrangement MIDI clip."""
    return live_set.clip_notes(clip_ref)


@mcp.resource("ableton://clip/{clip_ref}/warp")
def clip_warp_resource(clip_ref: str) -> dict:
    """Return warp markers for one Arrangement audio clip."""
    return live_set.audio_clip_warp_markers(clip_ref)


@mcp.resource("ableton://selection")
def selection_resource() -> dict:
    """Return the current Live selection context."""
    return live_set.selected_context()


if __name__ == "__main__":
    mcp.run()
