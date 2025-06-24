"""Simplistic MCP-Kernel stub."""
import random
from typing import Dict, Any

from .protocol import MCPRequest, MCPResponse, hash_tree


class MCPKernel:
    def handle_request(self, req: MCPRequest) -> MCPResponse:
        """Generate a trivial response based on the click target."""
        # Use random example UI elements
        if req.event.target.get("component_id") == "desktop_icon_documents":
            new_view = {
                "component": "Window",
                "properties": {"title": "Documents"},
                "children": [
                    {
                        "component": "ListView",
                        "children": [
                            {
                                "component": "ListItem",
                                "properties": {
                                    "id": "file_report",
                                    "label": "Report.docx",
                                },
                            },
                            {
                                "component": "ListItem",
                                "properties": {
                                    "id": "folder_projects",
                                    "label": "Projects/",
                                },
                            },
                        ],
                    }
                ],
            }
        else:
            # Default generic window
            new_view = {
                "component": "Window",
                "properties": {"title": "Home"},
                "children": [
                    {
                        "component": "Text",
                        "properties": {
                            "content": f"Clicked {req.event.target.get('component_id')}",
                        },
                    }
                ],
            }

        return MCPResponse(
            protocol_version=req.protocol_version,
            session_id=req.session_id,
            directive="REPLACE_VIEW",
            new_ui_state={
                "view_id": f"view_{random.randint(1000,9999)}",
                "component_tree": new_view,
                "component_tree_hash": hash_tree(new_view),
            },
        )
