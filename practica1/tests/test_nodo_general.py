import unittest

from practica1.nodo_general import NodoGeneral

class NodoGeneralTest(unittest.TestCase):
    def test_node_save_initial_data_and_empty_child_list(self):
        empty_general_node = NodoGeneral(data = "data")
        
        self.assertEqual(empty_general_node.data, "data")
        self.assertEqual(empty_general_node.childs, [])