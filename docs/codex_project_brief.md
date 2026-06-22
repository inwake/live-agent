# Codex project brief

Build an Arrangement-first Ableton Live MCP server.

Do not build a toy MCP demo. The core deliverable is a real Live Object Model bridge that can inspect and eventually edit Arrangement View safely.

## Architecture

```text
MCP Host / Codex
  <-> external Python MCP server
  <-> external Python client / ORM facade
  <-> localhost framed JSON transport
  <-> Ableton Python Remote Script bridge
  <-> Live Object Model
```

## Implementation split

### In Live

`remote_scripts/AbletonLiveBridge/`

- stdlib only
- socket listener
- request framing
- auth token check
- command queue
- object registry
- serializers
- command handlers
- executes LOM commands on the Live/control-surface tick, not directly from client threads

### Outside Live

`src/ableton_live_client/`

- typed transport client
- Pydantic models
- high-level ORM facade
- capability checks
- typed errors

`src/ableton_mcp_server/`

- MCP resources
- MCP tools
- patch previews
- dry-run behavior
- no arbitrary eval tool by default

## v0.1 acceptance criteria

- Connect to Live over localhost.
- Read Live app/version/session metadata.
- Read track list including track type, name, mute/solo/arm where available.
- Read Arrangement clips per track.
- Read MIDI notes from an Arrangement MIDI clip using extended note APIs where available.
- Read audio clip warp metadata and warp markers where available.
- Read device chain and exposed DeviceParameter metadata.
- Return typed unsupported-operation errors.
- Include fake Live contract tests.

## v0.2 acceptance criteria

- Create Arrangement MIDI clips directly on a target track/time range.
- Add/replace/delete MIDI notes with dry-run preview.
- Create Arrangement audio clips from a file path.
- Set exposed device parameter values.
- Rename and mute/solo/arm tracks.
- Keep all destructive operations explicit and reversible.

## v0.3 candidate features

- Event subscriptions / state cache.
- Exposed plugin parameter diagnosis.
- Optional Options.txt helper.
- Optional external screenshot helper for plugin windows.
- Optional Max for Live helper only for cases the Remote Script cannot reach.

## Non-goals

- Full arbitrary VST3 parameter scraping.
- Autonomous full-song generation.
- Session View as the primary data model.
- Arbitrary Python code execution via MCP.
