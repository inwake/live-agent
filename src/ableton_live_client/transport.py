from __future__ import annotations

import json
import socket
import uuid
from typing import Any

from .models import BridgeError, BridgeErrorPayload, BridgeRequest, BridgeResponse


class LiveBridgeClient:
    def __init__(self, host: str = "127.0.0.1", port: int = 9877, token: str | None = None, timeout: float = 10.0):
        self.host = host
        self.port = port
        self.token = token
        self.timeout = timeout

    def call(self, command_type: str, **params: Any) -> Any:
        request = BridgeRequest(
            id=f"req_{uuid.uuid4().hex[:12]}",
            token=self.token,
            type=command_type,
            params=params,
        )
        payload = request.model_dump_json().encode("utf-8") + b"\n"
        with socket.create_connection((self.host, self.port), timeout=self.timeout) as sock:
            sock.settimeout(self.timeout)
            sock.sendall(payload)
            raw = self._readline(sock)
        response = BridgeResponse.model_validate_json(raw)
        if not response.ok:
            raise BridgeError(response.error or BridgeErrorPayload(code="UNKNOWN", message="Unknown bridge error"))
        return response.result

    @staticmethod
    def _readline(sock: socket.socket) -> bytes:
        chunks: list[bytes] = []
        while True:
            chunk = sock.recv(4096)
            if not chunk:
                break
            chunks.append(chunk)
            if b"\n" in chunk:
                break
        data = b"".join(chunks)
        line, _, _rest = data.partition(b"\n")
        return line
