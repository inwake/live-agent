from __future__ import annotations

from ..serializers import safe_get, serialize_device, serialize_parameter


def _resolve_track(song, track_ref):
    track_index = int(track_ref.split(":", 1)[1])
    return list(song.tracks)[track_index]


def _resolve_device(song, device_ref):
    # v0 resolver: track:N/device:M
    parts = device_ref.split("/")
    track = _resolve_track(song, parts[0])
    device_index = int(parts[1].split(":", 1)[1])
    return list(track.devices)[device_index]


def get_track_devices(song, params):
    track_ref = params["track_ref"]
    track = _resolve_track(song, track_ref)
    devices = list(safe_get(track, "devices", []) or [])
    return {
        "track_ref": track_ref,
        "devices": [serialize_device(device, f"{track_ref}/device:{i}", i) for i, device in enumerate(devices)],
    }


def get_device_parameters(song, params):
    device_ref = params["device_ref"]
    device = _resolve_device(song, device_ref)
    parameters = list(safe_get(device, "parameters", []) or [])
    return {
        "device_ref": device_ref,
        "parameters": [serialize_parameter(param, f"{device_ref}/parameter:{i}", i) for i, param in enumerate(parameters)],
    }
