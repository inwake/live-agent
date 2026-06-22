# Capability matrix

| Capability | v1 status | Notes |
|---|---:|---|
| Read Live version and basic app state | Yes | Via Live application/song objects. |
| Read tracks / return tracks / master | Yes | Core Song children. |
| Read Arrangement clips | Yes | Track has `arrangement_clips`. |
| Create Arrangement MIDI clip | Yes | Track has `create_midi_clip(start_time, length)`. |
| Create Arrangement audio clip | Yes | Track has `create_audio_clip(file_path, position)`. |
| Read MIDI notes | Yes | Prefer extended note APIs on modern Live. |
| Add MIDI notes | Yes | Prefer `add_new_notes`. |
| Replace/delete MIDI notes | Yes | Use note IDs / pitch-time ranges depending on Live version. |
| Read audio warp markers | Yes, audio clips only | Some marker details are intentionally hidden. |
| Add/move/remove warp marker | Yes-ish | Expose with typed errors and capability checks. |
| Read device chain | Yes | Devices are LOM children on tracks/chains. |
| Read exposed device parameters | Yes | `Device.parameters` gives automatable parameters. |
| Set exposed device parameter | Yes | Set DeviceParameter value. |
| Full arbitrary VST3 params | No | Out of scope; not generally exposed by Live. |
| Plugin Configure automation helper | Later | Could provide diagnostics and Options.txt guidance. |
| Insert native Live devices | Later | Newer LOM has limited `insert_device`; plugins/M4L unsupported there. |
| Insert arbitrary VST plugins | No v1 | Needs browser/UI workaround or separate strategy. |
| Plugin window screenshots | No v1 | External OS helper, not Remote Script core. |
| Max for Live helper | Optional later | Use only where Remote Script API cannot reach. |
