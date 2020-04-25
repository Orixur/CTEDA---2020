import unittest

from practica1.nodo_general import NodoGeneral

class NodoGeneralTest(unittest.TestCase):
    def test_node_save_initial_data_and_empty_child_list(self):
        empty_general_node = NodoGeneral(data="data")
        
        self.assertEqual(empty_general_node.data, "data")
        self.assertEqual(empty_general_node.childs, [])

    def test_node_can_save_new_childls(self):
        empty_general_node = NodoGeneral(data="data")
        new_child_node = NodoGeneral(data="child_node")

        empty_general_node.add_child(new_child_node)

        self.assertIn(new_child_node, empty_general_node.childs)