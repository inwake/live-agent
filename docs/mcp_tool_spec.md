# MCP resource and tool spec

## Resources

```text
ableton://live/version
ableton://set/summary
ableton://set/transport
ableton://tracks
ableton://track/{track_ref}
ableton://track/{track_ref}/arrangement
ableton://track/{track_ref}/devices
ableton://clip/{clip_ref}
ableton://clip/{clip_ref}/notes
ableton://clip/{clip_ref}/warp
ableton://selection
```

## Read tools v0.1

```text
scan_live_set()
get_arrangement_clips(track_ref? = null)
get_clip_notes(clip_ref, from_time? = null, time_span? = null, from_pitch? = null, pitch_span? = null)
get_audio_clip_warp_markers(clip_ref)
get_track_devices(track_ref)
get_device_parameters(device_ref)
get_selected_context()
```

## Edit tools v0.2

```text
create_midi_track(index? = null, name? = null, dry_run = true)
create_audio_track(index? = null, name? = null, dry_run = true)
create_arrangement_midi_clip(track_ref, start_time, length, name? = null, dry_run = true)
create_arrangement_audio_clip(track_ref, file_path, position, dry_run = true)
add_clip_notes(clip_ref, notes, dry_run = true)
replace_clip_notes(clip_ref, notes, dry_run = true)
delete_clip_notes(clip_ref, note_ids? = null, range? = null, dry_run = true)
set_device_parameter(device_param_ref, value, dry_run = true)
set_track_state(track_ref, mute? = null, solo? = null, arm? = null, dry_run = true)
```

## Tool behavior rules

- Read tools should be generous and structured.
- Edit tools should be narrow and explicit.
- No tool should silently create broad changes.
- Dry run should be default for destructive or creative changes until the UX is proven.
- Return patch previews in music-time terms: bars/beats, clip names, track names, note counts.
