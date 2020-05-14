import unittest

from practica2.binary_node import BinaryNode
from practica2.red_binaria_llena import RedBinariaLlena


class RedBinariaLlenaTest(unittest.TestCase):
    def build_mid_tree(self):
        node_1 = BinaryNode(1)
        tree = RedBinariaLlena(node_1)
        node_2 = RedBinariaLlena(BinaryNode(2))
        node_3 = RedBinariaLlena(BinaryNode(3))
        node_4 = RedBinariaLlena(BinaryNode(4))
        node_5 = RedBinariaLlena(BinaryNode(5))
        node_6 = RedBinariaLlena(BinaryNode(6))
        node_7 = RedBinariaLlena(BinaryNode(7))
        node_8 = RedBinariaLlena(BinaryNode(8))
        node_9 = RedBinariaLlena(BinaryNode(9))
        node_10 = RedBinariaLlena(BinaryNode(10))

        tree.leftChild = node_2
        tree.rightChild = node_3
        node_2.leftChild = node_4
        node_2.rightChild = node_5
        node_3.leftChild = node_6
        node_3.rightChild = node_7
        node_4.leftChild = node_8
        node_4.rightChild = node_10
        node_5.leftChild = node_9

        return tree

    def build_full_tree(self):
        node_1 = BinaryNode(1)
        tree = RedBinariaLlena(node_1)
        node_2 = RedBinariaLlena(BinaryNode(2))
        node_3 = RedBinariaLlena(BinaryNode(3))
        node_4 = RedBinariaLlena(BinaryNode(4))
        node_5 = RedBinariaLlena(BinaryNode(5))
        node_6 = RedBinariaLlena(BinaryNode(6))
        node_7 = RedBinariaLlena(BinaryNode(7))

        tree.leftChild = node_2
        tree.rightChild = node_3
        node_2.leftChild = node_4
        node_2.rightChild = node_5
        node_3.leftChild = node_6
        node_3.rightChild = node_7

        return tree

    def test_tree_is_valid_if_is_full(self):
        tree = self.build_full_tree()
        
        self.assertTrue(tree.isFull(tree=0))

    def test_tree_is_not_valid_if_is_not_full(self):
        tree = self.build_mid_tree()

        self.assertFalse(tree.isFull(tree=0))

    def test_can_calculate_retard_delay_between_nodes(self):
        tree = self.build_full_tree()

        result = tree.redirect_delay()

        self.assertEqual(result, 11)