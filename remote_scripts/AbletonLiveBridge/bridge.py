from __future__ import annotations

import os
import socket
import threading

try:
    from _Framework.ControlSurface import ControlSurface
except Exception:
    ControlSurface = object

from .dispatcher import CommandDispatcher
from .protocol import decode_request, encode_response, err
from .commands.registry import CommandRegistry


class AbletonLiveBridge(ControlSurface):
    def __init__(self, c_instance):
        if hasattr(super(), "__init__"):
            try:
                super().__init__(c_instance)
            except TypeError:
                super().__init__()
        self.host = "127.0.0.1"
        self.port = int(os.environ.get("ABLETON_BRIDGE_PORT", "9877"))
        self.token = os.environ.get("ABLETON_BRIDGE_TOKEN")
        self.registry = CommandRegistry(
            song_getter=self.song if hasattr(self, "song") else lambda: None,
            app_getter=self.application if hasattr(self, "application") else lambda: None,
        )
        self.dispatcher = CommandDispatcher(self.registry)
        self._shutdown = False
        self._server_thread = threading.Thread(target=self._serve, name="AbletonLiveBridgeSocket", daemon=True)
        self._server_thread.start()

    def update_display(self):
        # Called periodically by Live control-surface framework.
        self.dispatcher.drain()

    def disconnect(self):
        self._shutdown = True
        try:
            super().disconnect()
        except Exception:
            pass

    def _serve(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((self.host, self.port))
        server.listen(8)
        while not self._shutdown:
            try:
                client, _addr = server.accept()
            except Exception:
                continue
            thread = threading.Thread(target=self._handle_client, args=(client,), daemon=True)
            thread.start()

    def _handle_client(self, client):
        with client:
            try:
                data = self._recv_line(client)
                request = decode_request(data)
                request_id = request.get("id")
                if self.token and request.get("token") != self.token:
                    client.sendall(encode_response(err(request_id, "AUTH_FAILED", "Invalid bridge token")))
                    return
                pending = self.dispatcher.submit(request)
                if not pending.event.wait(timeout=10):
                    client.sendall(encode_response(err(request_id, "TIMEOUT", "Bridge request timed out")))
                    return
                client.sendall(encode_response(pending.response))
            except Exception as exc:
                client.sendall(encode_response(err(None, "INTERNAL_ERROR", str(exc))))

    @staticmethod
    def _recv_line(client):
        chunks = []
        while True:
            chunk = client.recv(4096)
            if not chunk:
                break
            chunks.append(chunk)
            if b"\n" in chunk:
                break
        line, _sep, _rest = b"".join(chunks).partition(b"\n")
        return line
