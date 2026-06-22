# Project goal

This project is for seasoned Ableton Live users, not beginners asking an agent to make a song for them.

The agent should act like a project-aware collaborator: it can inspect the Live set, understand the arrangement, notice missing contrast or overcrowding, inspect MIDI density, identify exposed device automation/parameter state, and suggest concrete next moves.

## In scope

- Understanding the state of a Live set.
- Reading Arrangement View deeply enough to talk about the music in context.
- Reading MIDI notes and clip placement.
- Reading audio clip metadata and warp markers where available.
- Reading device chains and exposed parameters.
- Making small, explicit, reversible edits.
- Creating alternate MIDI ideas in a selected time range or new clip.
- Diagnosing likely reasons a section feels empty, cluttered, static, or disconnected.

## Out of scope

- Writing complete tracks for novice musicians.
- Pretending to understand unexposed VST3 internals.
- Replacing the producer's judgment.
- Hidden destructive edits.
- Generic Python eval over MCP.
- Fully autonomous arrangement/mix decisions.

## Product heuristic

The right experience is: “I am stuck at bar 49 and the agent can see why this section is flat.”

The wrong experience is: “Make me an EDM banger.”
