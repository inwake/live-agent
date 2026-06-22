# Bridge protocol

Use newline-delimited framed JSON for v0.1. This is simple enough for the Remote Script and easy to debug.

## Request

```json
{
  "id": "req_001",
  "token": "dev-token",
  "type": "clip.get_notes",
  "params": {
    "clip_ref": "track:2/arrangement_clip:4",
    "include_extended": true
  }
}
```

## Success response

```json
{
  "id": "req_001",
  "ok": true,
  "result": {
    "clip_id": "track:2/arrangement_clip:4",
    "notes": []
  }
}
```

## Error response

```json
{
  "id": "req_001",
  "ok": false,
  "error": {
    "code": "UNSUPPORTED_LOM_OPERATION",
    "message": "Warp markers are only available for audio clips.",
    "details": {
      "clip_type": "midi"
    }
  }
}
```

## Error codes

- `AUTH_FAILED`
- `UNKNOWN_COMMAND`
- `BAD_REQUEST`
- `OBJECT_NOT_FOUND`
- `UNSUPPORTED_LOM_OPERATION`
- `LIVE_API_ERROR`
- `INTERNAL_ERROR`
- `TIMEOUT`

## Object references

Initial refs should be human-readable and reconstructable:

```text
song
track:0
track:2/arrangement_clip:4
track:1/device:3
track:1/device:3/parameter:5
selected_track
selected_clip
selected_device
```

Later versions can add stable registry IDs, but path refs are easier for debugging and Codex comprehension.
