from unittest import TestCase
from .singly import LinkedListNode, delete_node


class SinglyTest(TestCase):
    def test_delete_node(self):
        a = LinkedListNode('A')
        b = LinkedListNode('B')
        c = LinkedListNode('C')

        a.next = b
        b.next = c

        delete_node(b)
        self.assertEqual(a.next.value, c.value)
