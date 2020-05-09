import unittest

from practica2.binary_tree import BinaryTree
from practica2.binary_node import BinaryNode
from practica2.profundidad_arbol_binario import ProfundidadDeArbolBinario

class ProfundidadDeArbolBinarioTest(unittest.TestCase):
    def build_full_tree(self):
        node_1 = BinaryNode(1)
        tree = ProfundidadDeArbolBinario(node_1)
        node_2 = BinaryTree(BinaryNode(2))
        node_3 = BinaryTree(BinaryNode(3))
        node_4 = BinaryTree(BinaryNode(4))
        node_5 = BinaryTree(BinaryNode(5))
        node_6 = BinaryTree(BinaryNode(6))
        node_7 = BinaryTree(BinaryNode(7))

        tree.leftChild = node_2
        tree.rightChild = node_3
        node_2.leftChild = node_4
        node_2.rightChild = node_5
        node_3.leftChild = node_6
        node_3.rightChild = node_7

        return tree

    def test_can_sum_all_nodes_in_desired_level(self):
        tree = self.build_full_tree()

        res = tree.sumOnDeep(level=3)

        self.assertEqual(res, 22)
