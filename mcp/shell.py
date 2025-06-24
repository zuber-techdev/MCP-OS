"""Minimal MCP-Shell command-line renderer."""
import json
import uuid

from .protocol import Event, MCPRequest
from .kernel import MCPKernel


def pretty_print(tree, indent=0):
    prefix = ' ' * indent
    component = tree.get('component')
    props = tree.get('properties', {})
    print(f"{prefix}{component}: {props}")
    for child in tree.get('children', []):
        pretty_print(child, indent + 2)


def main():
    kernel = MCPKernel()
    session_id = f"sid_{uuid.uuid4().hex[:8]}"

    current_ui_state = {
        "view_id": "view_home",
        "component_tree": {
            "component": "Desktop",
            "children": [
                {
                    "component": "Icon",
                    "properties": {
                        "id": "desktop_icon_documents",
                        "label": "Documents",
                    },
                },
                {
                    "component": "Icon",
                    "properties": {
                        "id": "desktop_icon_other",
                        "label": "Other",
                    },
                },
            ],
        },
    }

    while True:
        print("\nCurrent UI:")
        pretty_print(current_ui_state["component_tree"])
        target = input("\nEnter component id to click (or 'quit'): ")
        if target == 'quit':
            break
        event = Event(type="click", target={"component_id": target})
        req = MCPRequest(
            protocol_version="1.0",
            session_id=session_id,
            user_context={"name": "Alex"},
            current_ui_state={
                "view_id": current_ui_state["view_id"],
                "component_tree_hash": "",
            },
            event=event,
        )
        resp = kernel.handle_request(req)
        current_ui_state = resp.new_ui_state

if __name__ == "__main__":
    main()
