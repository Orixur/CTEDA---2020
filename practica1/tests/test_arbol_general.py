import unittest

from practica1.arbol_general import ArbolGeneral
from practica1.nodo_general import NodoGeneral

class ArbolGeneralTest(unittest.TestCase):
    def set_tree_with_node(self):
        root_node = NodoGeneral(data="root_node")
        tree = ArbolGeneral(root=root_node)
        return root_node, tree
    
    def test_general_tree_can_allocate_root_node_only_on_init(self):
        root_node, tree = self.set_tree_with_node()
        
        self.assertEqual(root_node, tree.root)

    def test_can_fetch_root_node_data(self):
        root_node, tree = self.set_tree_with_node()
        
        root_data = tree.root_data

        self.assertEqual(root_node.data, root_data)