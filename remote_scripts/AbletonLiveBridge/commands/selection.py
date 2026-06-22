from __future__ import annotations

from ..serializers import (
    safe_get,
    serialize_clip,
    serialize_device,
    serialize_parameter,
    serialize_track,
)
from .resolvers import (
    find_arrangement_clip_ref,
    find_device_ref,
    find_parameter_ref,
    find_track_ref,
    is_lom_null,
)


def _serialize_selected_track(song, track):
    found = find_track_ref(song, track)
    if not found:
        return None
    track_ref, index, kind = found
    return serialize_track(track, index, ref=track_ref, kind=kind)


def _serialize_detail_clip(song, clip):
    found = find_arrangement_clip_ref(song, clip)
    if not found:
        if is_lom_null(clip):
            return None
        return {"ref": None, "name": safe_get(clip, "name"), "source": "detail_clip"}
    clip_ref, _track, _track_ref, _clip_index = found
    return serialize_clip(clip, clip_ref)


def _serialize_selected_device(song, selected_track, selected_track_ref):
    if is_lom_null(selected_track):
        return None
    track_view = safe_get(selected_track, "view")
    device = safe_get(track_view, "selected_device")
    found = find_device_ref(song, device, selected_track, selected_track_ref)
    if not found:
        return None
    device_ref, _track, _track_ref, device_index = found
    return serialize_device(device, device_ref, device_index)


def _serialize_selected_parameter(song, parameter):
    found = find_parameter_ref(song, parameter)
    if not found:
        return None
    parameter_ref, _device, device_ref, _track, track_ref = found
    parameter_index = int(parameter_ref.rsplit(":", 1)[1])
    return {
        "track_ref": track_ref,
        "device_ref": device_ref,
        **serialize_parameter(parameter, parameter_ref, parameter_index),
    }


def get_selected_context(song, params, app=None):
    view = safe_get(song, "view")
    selected_track = safe_get(view, "selected_track")
    selected_track_payload = _serialize_selected_track(song, selected_track)
    selected_track_ref = selected_track_payload["ref"] if selected_track_payload else None
    detail_clip = safe_get(view, "detail_clip")
    selected_parameter = safe_get(view, "selected_parameter")
    selected_chain = safe_get(view, "selected_chain")
    highlighted_clip_slot = safe_get(view, "highlighted_clip_slot")
    return {
        "selected_track": selected_track_payload,
        "detail_clip": _serialize_detail_clip(song, detail_clip),
        "selected_device": _serialize_selected_device(song, selected_track, selected_track_ref),
        "selected_parameter": _serialize_selected_parameter(song, selected_parameter),
        "selected_chain": None
        if is_lom_null(selected_chain)
        else {"name": safe_get(selected_chain, "name")},
        "highlighted_clip_slot": None
        if is_lom_null(highlighted_clip_slot)
        else {"has_clip": safe_get(highlighted_clip_slot, "has_clip")},
        "draw_mode": safe_get(view, "draw_mode"),
        "follow_song": safe_get(view, "follow_song"),
    }
