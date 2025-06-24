# MCP-OS

The **Model Context Protocol Operating System (MCP-OS)** is a concept for a post‑application computing platform. Instead of bundling discrete programs with fixed user interfaces, MCP-OS delegates most logic and UI generation to a large language model. A lightweight shell running on the device gathers user actions and context, sends them to the model, and renders the model's declarative response.

## System architecture

MCP-OS consists of three key pieces:

1. **MCP-Kernel** – the large language model that interprets requests and produces responses.
2. **MCP-Shell** – a minimal renderer that captures user input, formats protocol requests, and displays the returned UI tree.
3. **Model Context Protocol** – a structured message format defining how the shell and kernel communicate.

The shell packages each user action and the current view state into an MCP request. The kernel reasons about this context and replies with a new UI description. The shell simply renders that description, forming a continuous feedback loop.

## Model Context Protocol

A minimal request example:

```json
{
  "protocol_version": "1.0",
  "session_id": "sid_example_1234",
  "user_context": { "name": "Alex" },
  "current_ui_state": {
    "view_id": "view_home",
    "component_tree_hash": "abcd1234"
  },
  "event": {
    "type": "click",
    "target": { "component_id": "desktop_icon_documents" }
  }
}
```

A response from the kernel might look like:

```json
{
  "protocol_version": "1.0",
  "session_id": "sid_example_1234",
  "directive": "REPLACE_VIEW",
  "new_ui_state": {
    "view_id": "view_documents",
    "component_tree": {
      "component": "Window",
      "children": [ { "component": "ListView" } ]
    }
  }
}
```

## Example workflow

1. The user interacts with the shell, for instance by clicking an icon.
2. The shell emits an MCP request describing that event and the current view.
3. The kernel analyzes the request and produces an MCP response describing the next view.
4. The shell renders the new view and awaits further input.

## Challenges

Achieving practical performance and consistency with a model‑driven OS presents challenges around latency, state management, cost, and security. The protocol is intentionally simple to enable experimentation with these issues while keeping the renderer lightweight.


## Reference implementation

A small command-line prototype demonstrates the MCP loop.
It consists of three modules under the `mcp/` package:

- `protocol.py` – definitions for request and response structures
- `kernel.py` – a trivial kernel that generates example views
- `shell.py` – an interactive renderer that prints UI trees and sends events

### Running the demo

```
python -m mcp.shell
```

The shell prints a simple desktop containing a Documents icon.
Enter the component id you wish to click (for example `desktop_icon_documents`).
The shell sends an MCP request to the kernel and renders the
returned view description.
=======

