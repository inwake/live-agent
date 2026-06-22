from __future__ import annotations

import json


def encode_response(response):
    return (json.dumps(response, separators=(",", ":"), ensure_ascii=False) + "\n").encode("utf-8")


def decode_request(data):
    if isinstance(data, bytes):
        data = data.decode("utf-8")
    return json.loads(data)


def ok(request_id, result):
    return {"id": request_id, "ok": True, "result": result}


def err(request_id, code, message, details=None):
    return {
        "id": request_id,
        "ok": False,
        "error": {
            "code": code,
            "message": message,
            "details": details or {},
        },
    }
