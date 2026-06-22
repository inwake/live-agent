# Remote Script threading notes

## Bad pattern

```text
client socket thread receives request
client socket thread calls Live API / LOM object directly
client socket thread serializes result
```

This is risky because the Live Object Model is owned by Live's application/control-surface execution context.

## Preferred pattern

```text
client socket thread receives request
client socket thread parses framed JSON
client socket thread enqueues command
Remote Script update tick drains queue
update tick calls LOM safely
update tick stores response
client socket thread returns response
```

## Practical v0.1 approach

- Use `queue.Queue`.
- A request has `id`, `type`, `params`, and a response slot.
- The bridge exposes `update_display` or equivalent periodic method.
- `update_display` drains a bounded number of queued commands per tick.
- Client threads wait with timeout.
- Long operations should be broken up or explicitly rejected.

## Watchouts

- Do not block Live's UI/audio thread with huge scans.
- Add pagination/ranges for notes and arrangement clips.
- Add result size limits.
- Add timeouts.
- Prefer read snapshots over chatty per-object calls.
