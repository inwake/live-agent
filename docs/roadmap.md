# Roadmap

## v0.0 scaffold

- Project docs.
- Protocol docs.
- Remote Script skeleton.
- External client skeleton.
- MCP server skeleton.
- Fake Live tests.

## v0.1 read-only visibility

The agent can understand the Live set.

- scan set
- tracks/devices/parameters
- arrangement clips
- clip details
- MIDI notes
- audio warp markers
- selected context

## v0.2 safe Arrangement edits

The agent can propose and optionally apply focused edits.

- create Arrangement MIDI clip
- add/replace notes
- create audio clip
- set exposed parameter
- rename/mute/solo/arm track

## v0.3 producer-assistant workflows

The agent can answer higher-level music-production questions using project state.

- “Why does this drop feel weak?”
- “What is missing in the 8 bars before the chorus?”
- “Find clips with dense MIDI but no movement.”
- “Suggest 3 alternate bass rhythms for this clip.”
- “Find exposed parameters that are static across a long section.”

## v0.4 optional integrations

- state cache / event subscriptions
- plugin visibility diagnostics
- Max for Live helper for specific gaps
- external screenshot helper
- richer browser/device workflows
