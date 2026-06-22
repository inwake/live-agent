from __future__ import annotations

from typing import Any
from pydantic import BaseModel, Field


class BridgeErrorPayload(BaseModel):
    code: str
    message: str
    details: dict[str, Any] = Field(default_factory=dict)


class BridgeError(Exception):
    def __init__(self, payload: BridgeErrorPayload):
        super().__init__(f"{payload.code}: {payload.message}")
        self.payload = payload


class BridgeRequest(BaseModel):
    id: str
    token: str | None = None
    type: str
    params: dict[str, Any] = Field(default_factory=dict)


class BridgeResponse(BaseModel):
    id: str | None
    ok: bool
    result: Any | None = None
    error: BridgeErrorPayload | None = None


class TrackSummary(BaseModel):
    ref: str
    index: int | None
    name: str
    kind: str | None = None
    mute: bool | None = None
    solo: bool | None = None
    arm: bool | None = None


class ClipSummary(BaseModel):
    ref: str
    name: str | None = None
    is_audio_clip: bool | None = None
    is_midi_clip: bool | None = None
    is_arrangement_clip: bool | None = None
    start_time: float | None = None
    end_time: float | None = None
    length: float | None = None
    file_path: str | None = None
    warping: bool | None = None
    warp_mode: int | None = None
    sample_length: int | None = None
    sample_rate: float | None = None


class MidiNote(BaseModel):
    note_id: int | None = None
    pitch: int
    start_time: float
    duration: float
    velocity: int
    mute: bool = False
    probability: float | None = None
    velocity_deviation: int | None = None
    release_velocity: int | None = None


class DeviceParameterSummary(BaseModel):
    ref: str
    index: int
    name: str | None = None
    original_name: str | None = None
    value: float | int | str | bool | None = None
    display_value: str | None = None
    min: float | None = None
    max: float | None = None
    default_value: float | None = None
    is_enabled: bool | None = None
    is_quantized: bool | None = None
    automation_state: int | None = None
    value_items: list[str] | None = None


class DeviceSummary(BaseModel):
    ref: str
    index: int
    name: str | None = None
    class_name: str | None = None
    class_display_name: str | None = None
    is_active: bool | None = None
    parameter_count: int | None = None


class WarpMarker(BaseModel):
    sample_time: float
    beat_time: float
