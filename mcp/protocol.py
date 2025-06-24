from dataclasses import dataclass, field
from typing import Any, Dict, Optional
import hashlib


def hash_tree(tree: Dict[str, Any]) -> str:
    """Return a simple hash for a dictionary representing a UI tree."""
    return hashlib.md5(repr(tree).encode()).hexdigest()[:8]


@dataclass
class Event:
    type: str
    target: Dict[str, Any]
    payload: Optional[Dict[str, Any]] = None


@dataclass
class MCPRequest:
    protocol_version: str
    session_id: str
    user_context: Dict[str, Any]
    current_ui_state: Dict[str, Any]
    event: Event


@dataclass
class MCPResponse:
    protocol_version: str
    session_id: str
    directive: str
    new_ui_state: Dict[str, Any]
