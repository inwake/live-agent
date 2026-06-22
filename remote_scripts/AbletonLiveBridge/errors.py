from __future__ import annotations


class BridgeCommandError(Exception):
    def __init__(self, code, message, details=None):
        super().__init__(message)
        self.code = code
        self.message = message
        self.details = details or {}


def bad_request(message, details=None):
    return BridgeCommandError("BAD_REQUEST", message, details)


def object_not_found(message, details=None):
    return BridgeCommandError("OBJECT_NOT_FOUND", message, details)


def unsupported_operation(message, details=None):
    return BridgeCommandError("UNSUPPORTED_LOM_OPERATION", message, details)
