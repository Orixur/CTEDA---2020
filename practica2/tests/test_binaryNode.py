import unittest

from practica2.binary_node import BinaryNode

class BinaryNodeTest(unittest.TestCase):
    def test_binary_nodes_can_have_at_least_two_childs(self):
        node = BinaryNode(data='test-node')
        left_child = BinaryNode(data='left-child')
        right_child = BinaryNode(data='right-child')
        
        node.leftChild  = left_child
        node.rightChild = right_child

        self.assertEqual(node.leftChild, left_child)
        self.assertEqual(node.rightChild, right_child)