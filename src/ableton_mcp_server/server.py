from __future__ import annotations

import os
from pathlib import Path
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


@mcp.tool()
def inspect_live_set_capabilities() -> dict:
    """Return a read-only capability scan of tracks, racks, parameters, notes, and LOM limits."""
    return live_set.inspect_capabilities()


@mcp.tool()
def inspect_track_detail(track_ref: str) -> dict:
    """Return detailed Arrangement clips, devices, rack trees, and parameter counts for one track."""
    return live_set.inspect_track_detail(track_ref)


@mcp.tool()
def inspect_device_tree(device_ref: str) -> dict:
    """Return a recursive read-only tree for one device, including rack chains and Drum Rack pads."""
    return live_set.inspect_device_tree(device_ref)


@mcp.tool()
def inspect_clip_notes(
    clip_ref: str,
    from_time: float | None = None,
    time_span: float | None = None,
    from_pitch: int | None = None,
    pitch_span: int | None = None,
) -> dict:
    """Return MIDI notes and report which extended note fields are visible."""
    return live_set.inspect_clip_notes(
        clip_ref,
        from_time=from_time,
        time_span=time_span,
        from_pitch=from_pitch,
        pitch_span=pitch_span,
    )


@mcp.tool()
def inspect_parameter_exposure() -> dict:
    """Return exposed DeviceParameter counts by track, plugin, native device, and whole set."""
    return live_set.inspect_parameter_exposure()


@mcp.tool()
def generate_capability_report(output_path: str | None = None) -> dict:
    """Generate a markdown capability report from a real Live set scan."""
    data = live_set.inspect_capabilities()
    markdown = _capability_report_markdown(data)
    result = {"markdown": markdown}
    if output_path:
        path = Path(output_path)
        path.write_text(markdown, encoding="utf-8")
        result["path"] = str(path)
    return result


def _yes_no(value: object) -> str:
    if value is None:
        return "Unknown"
    return "Yes" if bool(value) else "No"


def _cell(value: object) -> str:
    if value is None:
        return ""
    return str(value).replace("\n", " ")


def _table(headers: list[str], rows: list[list[object]]) -> list[str]:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _header in headers) + " |",
    ]
    lines.extend("| " + " | ".join(_cell(value) for value in row) + " |" for row in rows)
    return lines


def _capability_report_markdown(data: dict) -> str:
    summary = data.get("set_summary", {})
    parameter_exposure = data.get("parameter_exposure", {})
    lines = [
        "# Live Set Capability Report",
        "",
        "## Set Summary",
        "- Name: " + _cell(summary.get("name")),
        "- Tempo: " + _cell(summary.get("tempo")),
        "- Time signature: " + _cell(summary.get("signature")),
        "- Track count: " + _cell(summary.get("track_count")),
        "- Return track count: " + _cell(summary.get("return_track_count")),
        "- Master track visible: " + _yes_no(summary.get("master_track_visible")),
        "- Arrangement clip count: " + _cell(summary.get("arrangement_clip_count")),
        "- MIDI clip count: " + _cell(summary.get("midi_clip_count")),
        "- Audio clip count: " + _cell(summary.get("audio_clip_count")),
        "",
        "## Return Tracks",
    ]
    lines.extend(
        _table(
            ["Ref", "Name", "Devices", "Exposed Params"],
            [
                [
                    track.get("ref"),
                    track.get("name"),
                    track.get("device_count"),
                    track.get("exposed_parameter_count"),
                ]
                for track in data.get("return_tracks", [])
            ],
        )
    )
    lines.extend(["", "## Tracks"])
    lines.extend(
        _table(
            ["Ref", "Name", "Type", "Arrangement Clips", "Devices", "Exposed Params"],
            [
                [
                    track.get("ref"),
                    track.get("name"),
                    track.get("kind"),
                    track.get("arrangement_clip_count"),
                    track.get("device_count"),
                    track.get("exposed_parameter_count"),
                ]
                for track in data.get("tracks", [])
            ],
        )
    )
    lines.extend(["", "## Plugin Parameter Exposure"])
    lines.extend(
        _table(
            ["Track", "Device", "Class", "Exposed Parameter Count", "Notes"],
            [
                [
                    device.get("track"),
                    device.get("device"),
                    device.get("class_name"),
                    device.get("exposed_parameter_count"),
                    device.get("notes"),
                ]
                for device in parameter_exposure.get("plugin_devices", [])
            ],
        )
    )
    lines.extend(["", "## Ableton Native Device Parameters"])
    lines.extend(
        _table(
            ["Track", "Device", "Class", "Exposed Parameter Count", "Example Parameters"],
            [
                [
                    device.get("track"),
                    device.get("device"),
                    device.get("class_name"),
                    device.get("exposed_parameter_count"),
                    ", ".join(device.get("example_parameters", [])),
                ]
                for device in parameter_exposure.get("native_devices", [])
            ],
        )
    )
    lines.extend(["", "## Drum Rack / Rack Depth"])
    lines.extend(
        _table(
            ["Track", "Rack", "Depth", "Chains", "Drum Pads", "Nested Devices", "Samples Found"],
            [
                [
                    rack.get("track"),
                    rack.get("rack"),
                    rack.get("depth"),
                    rack.get("chains"),
                    rack.get("drum_pads"),
                    rack.get("nested_devices"),
                    rack.get("samples_found"),
                ]
                for rack in data.get("rack_depth", [])
            ],
        )
    )
    lines.extend(["", "## MIDI Note Visibility"])
    lines.extend(
        _table(
            [
                "Clip",
                "Notes",
                "Velocity Visible",
                "Probability Visible",
                "Velocity Deviation Visible",
                "Release Velocity Visible",
            ],
            [
                [
                    clip.get("clip"),
                    clip.get("note_count"),
                    _yes_no(clip.get("velocity_visible")),
                    _yes_no(clip.get("probability_visible")),
                    _yes_no(clip.get("velocity_deviation_visible")),
                    _yes_no(clip.get("release_velocity_visible")),
                ]
                for clip in data.get("midi_note_visibility", [])
            ],
        )
    )
    limitation_messages = {
        item.get("code"): item.get("message") for item in data.get("limitations_observed", [])
    }
    lines.extend(
        [
            "",
            "## Limitations Observed",
            "- Hidden plugin parameters: "
            + _cell(limitation_messages.get("HIDDEN_PLUGIN_PARAMETERS_UNAVAILABLE")),
            "- Rendered waveforms: "
            + _cell(limitation_messages.get("RENDERED_WAVEFORMS_UNAVAILABLE")),
            "- Sampler/Simpler internals: "
            + _cell(limitation_messages.get("SAMPLER_WAVEFORM_DISPLAY_UNAVAILABLE")),
            "- Any unsupported LOM paths: "
            + _cell(limitation_messages.get("PLUGIN_GUI_UNAVAILABLE")),
            "",
        ]
    )
    return "\n".join(lines)


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


@mcp.resource("ableton://set/capabilities")
def set_capabilities_resource() -> dict:
    """Return the current Live set capability inspection scan."""
    return live_set.inspect_capabilities()


@mcp.resource("ableton://track/{track_ref}/detail")
def track_detail_resource(track_ref: str) -> dict:
    """Return detailed inspection for one track."""
    return live_set.inspect_track_detail(track_ref)


@mcp.resource("ableton://device/{device_ref}/tree")
def device_tree_resource(device_ref: str) -> dict:
    """Return recursive device tree inspection for one device."""
    return live_set.inspect_device_tree(device_ref)


@mcp.resource("ableton://set/parameter-exposure")
def parameter_exposure_resource() -> dict:
    """Return exposed parameter counts across the current Live set."""
    return live_set.inspect_parameter_exposure()


if __name__ == "__main__":
    mcp.run()
