from __future__ import annotations

from .transport import LiveBridgeClient


class LiveSet:
    """High-level facade over the bridge command surface."""

    def __init__(self, client: LiveBridgeClient):
        self.client = client

    def scan(self):
        return self.client.call("song.scan")

    def arrangement_clips(self, track_ref: str | None = None):
        return self.client.call("arrangement.get_clips", track_ref=track_ref)

    def clip(self, clip_ref: str):
        return self.client.call("clip.get", clip_ref=clip_ref)

    def clip_notes(self, clip_ref: str, **ranges):
        return self.client.call("clip.get_notes", clip_ref=clip_ref, **ranges)

    def audio_clip_warp_markers(self, clip_ref: str):
        return self.client.call("clip.get_warp_markers", clip_ref=clip_ref)

    def devices(self, track_ref: str):
        return self.client.call("track.get_devices", track_ref=track_ref)

    def device_parameters(self, device_ref: str):
        return self.client.call("device.get_parameters", device_ref=device_ref)

    def selected_context(self):
        return self.client.call("selection.get_context")

    def inspect_capabilities(self):
        return self.client.call("set.inspect_capabilities")

    def inspect_track_detail(self, track_ref: str):
        return self.client.call("track.inspect_detail", track_ref=track_ref)

    def inspect_device_tree(self, device_ref: str, **options):
        return self.client.call("device.inspect_tree", device_ref=device_ref, **options)

    def inspect_clip_notes(self, clip_ref: str, **ranges):
        return self.client.call("clip.inspect_notes", clip_ref=clip_ref, **ranges)

    def inspect_parameter_exposure(self):
        return self.client.call("set.inspect_parameter_exposure")
