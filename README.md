# Ableton Live MCP Seed

Arrangement-first Ableton Live bridge + MCP server scaffold.

This package is intentionally scoped for experienced producers. The goal is **not** to make an agent generate full tracks for novice users. The goal is to give an agent enough read/write context to understand the state of a real Ableton Live project and help a seasoned producer with diagnosis, alternatives, arrangement/mix observations, and fresh ideas when stuck.

## Design stance

- Arrangement View is first-class.
- Session View is supported only where useful, not as the conceptual center.
- The in-Live component is a small Python Remote Script bridge.
- The external component is a normal Python package with typed models, tests, and an MCP server.
- Plugin deep parameter scraping is not a v1 goal. Only parameters exposed to Live as `DeviceParameter` objects are in scope.
- No arbitrary `eval` tool is exposed to MCP by default.
- Mutations default to dry-run / preview until explicitly enabled.

## Layout

```text
remote_scripts/AbletonLiveBridge/    # stdlib-only Live Remote Script bridge
src/ableton_live_client/             # external Python client / ORM facade
src/ableton_mcp_server/              # MCP resources + tools
docs/                                # Codex brief, architecture, protocol, capability matrix
docs/vendor/cycling74_lom_live_12_3_5 # focused markdown extraction + fetch scripts
tests/                               # fake Live fixtures and contract tests
scripts/                             # install/fetch/smoke-test helpers
```

## First useful milestone

1. Connect to Live.
2. Read full set summary.
3. Read Arrangement clips per track.
4. Read notes from an Arrangement MIDI clip.
5. Create an Arrangement MIDI clip.
6. Add notes to that clip.
7. Read them back.
8. Report unsupported plugin/warp operations explicitly.

## Current package status

This is a Codex-ready seed package, not a finished implementation. It includes:

- project spec
- architecture docs
- MCP tool/resource spec
- transport protocol
- Remote Script skeleton
- external client skeleton
- focused LOM markdown seed docs
- Firecrawl/PDF fetch scripts for regenerating full LOM markdown in a real networked environment

See `AGENTS.md` and `docs/codex_project_brief.md` first.
