# Architecture

## Why this split

Ableton's useful control surface API lives inside Live's Python environment. MCP, modern typing, packaging, tests, and document tooling live much more comfortably outside Live. The bridge should keep these worlds separated.

## Components

### Remote Script bridge

Responsible for:

- accepting localhost requests
- authenticating requests
- parsing framed JSON
- enqueueing commands
- executing commands on the Live/control-surface tick
- serializing LOM objects into plain data
- returning typed errors

Not responsible for:

- MCP
- Pydantic
- heavy dependencies
- AI logic
- high-level musical interpretation

### External client / ORM facade

Responsible for:

- request/response transport
- typed models
- higher-level object references
- capability checks
- user-friendly exceptions
- patch preview construction

### MCP server

Responsible for:

- exposing resources and tools
- shaping responses for agents
- keeping tool schemas small and explicit
- enforcing dry-run defaults for mutating tools

## Threading rule

Do not touch Live Object Model objects from socket client threads. Socket threads can parse and enqueue. LOM commands should execute from the Remote Script/control-surface update path.

## Security rule

Bind to `127.0.0.1` by default and require a token. Ableton project control is powerful enough that a LAN-visible unauthenticated socket is not acceptable.
