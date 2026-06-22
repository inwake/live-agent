from __future__ import annotations

import queue
import threading


class PendingRequest:
    def __init__(self, request):
        self.request = request
        self.event = threading.Event()
        self.response = None

    def resolve(self, response):
        self.response = response
        self.event.set()


class CommandDispatcher:
    def __init__(self, command_registry, max_per_tick=16):
        self.command_registry = command_registry
        self.max_per_tick = max_per_tick
        self._queue = queue.Queue()

    def submit(self, request):
        pending = PendingRequest(request)
        self._queue.put(pending)
        return pending

    def drain(self):
        count = 0
        while count < self.max_per_tick:
            try:
                pending = self._queue.get_nowait()
            except queue.Empty:
                break
            response = self.command_registry.handle(pending.request)
            pending.resolve(response)
            count += 1
