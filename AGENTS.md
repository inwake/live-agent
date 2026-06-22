# Instructions for Codex / coding agents

Do not turn this into a hello-world MCP demo.

The project goal is to build an Arrangement-first Ableton Live bridge that helps an experienced producer understand and unblock a real Live set. The agent should be able to inspect tracks, arrangement clips, MIDI notes, audio/warp metadata, device chains, and exposed device parameters. It should not pretend to write complete tracks or fully control arbitrary VST3 internals.

## Hard constraints

- Prioritize Arrangement View over Session View.
- Keep the in-Live Remote Script stdlib-only.
- Do not import Pydantic, MCP SDK, requests, or heavy third-party libs inside Ableton.
- Do not call LOM objects directly from socket/client threads.
- Socket thread must parse/enqueue only; the Live/control-surface tick must execute LOM commands.
- Bind bridge to `127.0.0.1` by default.
- Require local auth token unless explicitly disabled for development.
- Use framed JSON, not pickle.
- Use typed errors.
- Expose safe, explicit tools. Do not expose arbitrary Python eval to MCP.
- Mutating tools must support `dry_run` and patch previews.
- Treat full arbitrary VST3 parameter access as out of scope for v1.

## v0.1 target

Implement read-only inspection:

- `scan_live_set`
- `get_arrangement_clips`
- `get_clip_notes`
- `get_audio_clip_warp_markers`
- `get_track_devices`
- `get_device_parameters`
- `get_selected_context`

## v0.2 target

Implement safe edits:

- create audio/MIDI tracks
- create Arrangement MIDI clips
- create Arrangement audio clips
- add/replace/delete MIDI notes
- set exposed device parameters
- rename/mute/solo/arm tracks

## Testing requirement

Before requiring Ableton, write contract tests against `tests/fake_live`. The fake objects should emulate the subset of the Live Object Model used by the bridge serializers and command handlers.
