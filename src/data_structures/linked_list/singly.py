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


def reverse_singly_linked_list(head: LinkedListNode):
    """
    Reverses the singly linked list in place.
    """
    prev_node = None
    cur_node = head
    next_node = head.next

    while cur_node.next:
        cur_node.next = prev_node

        prev_node = cur_node
        cur_node = next_node
        next_node = cur_node.next

    cur_node.next = prev_node
