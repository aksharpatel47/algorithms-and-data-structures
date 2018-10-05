from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class LinkedListNode():
    value: Any
    next: Optional['LinkedListNode'] = None


def delete_node(node: LinkedListNode):
    next_node = node.next

    if next_node:
        node.value = next_node.value
        node.next = next_node.next
    else:
        raise ValueError("Cannot delete last node")
