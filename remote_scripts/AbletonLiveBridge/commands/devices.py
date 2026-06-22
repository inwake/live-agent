from __future__ import annotations

from ..serializers import safe_get, serialize_device, serialize_parameter
from .resolvers import resolve_device, resolve_track


def get_track_devices(song, params, app=None):
    track_ref = params["track_ref"]
    track, track_ref, _index, _kind = resolve_track(song, track_ref)
    devices = list(safe_get(track, "devices", []) or [])
    return {
        "track_ref": track_ref,
        "track_name": safe_get(track, "name"),
        "device_count": len(devices),
        "devices": [serialize_device(device, f"{track_ref}/device:{i}", i) for i, device in enumerate(devices)],
    }


def get_device_parameters(song, params, app=None):
    device_ref = params["device_ref"]
    device, device_ref, _track, track_ref, _device_index = resolve_device(song, device_ref)
    parameters = list(safe_get(device, "parameters", []) or [])
    return {
        "track_ref": track_ref,
        "device_ref": device_ref,
        "device": serialize_device(device, device_ref, _device_index),
        "parameter_count": len(parameters),
        "parameters": [serialize_parameter(param, f"{device_ref}/parameter:{i}", i) for i, param in enumerate(parameters)],
    }
