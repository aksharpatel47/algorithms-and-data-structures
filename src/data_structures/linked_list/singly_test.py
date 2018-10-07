from unittest import TestCase, main
from .singly import LinkedListNode, delete_node, reverse_singly_linked_list


class SinglyTest(TestCase):
    def setUp(self):
        self.a = LinkedListNode('A')
        self.b = LinkedListNode('B')
        self.c = LinkedListNode('C')
        self.a.next = self.b
        self.b.next = self.c

    def test_delete_node(self):
        delete_node(self.b)
        self.assertEqual(self.a.next.value, self.c.value)

    def test_rev_singly_list(self):
        reverse_singly_linked_list(self.a)

        self.assertEqual(self.a.next, None)
        self.assertEqual(self.b.next, self.a)
        self.assertEqual(self.c.next, self.b)
