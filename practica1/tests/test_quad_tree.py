import unittest

from practica1.quad_tree import QuadTree
from practica1.nodo_general import NodoGeneral

class QuadTreeTest(unittest.TestCase):
    def test_adding_a_child_appends_4_new_sub_trees(self):
        root_node = NodoGeneral('root-node')
        tree = QuadTree(root_node)

        tree.add_child([
            NodoGeneral('negro'),
            NodoGeneral('blanco'),
            NodoGeneral('negro'),
            NodoGeneral('blanco'),
        ])

        self.assertEqual(len(tree.childs), 4)

    def test_can_get_pixels_of_image_based_on_image_total_size(self):
        root_node = NodoGeneral('root-node')
        tree = QuadTree(root_node)

        first_node = NodoGeneral('base-node1')
        first_node.add_child([
            NodoGeneral('blanco'),
            NodoGeneral('blanco'),
            NodoGeneral('blanco'),
            NodoGeneral('negro'),
        ])
        second_node = NodoGeneral('base-node2')
        second_node.add_child([
            NodoGeneral('negro'),
            NodoGeneral('negro'),
            NodoGeneral('blanco'),
            NodoGeneral('blanco'),
        ])
        third_node = NodoGeneral('negro')
        fourth_node = NodoGeneral('blanco')
        tree.add_child([
            first_node,
            second_node,
            third_node,
            fourth_node
        ])

        pixel_count_result = tree.pixel_count(size=1024, color='negro')
        self.assertEqual(pixel_count_result, 44)