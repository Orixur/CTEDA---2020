import unittest

from practica1.arbol_general import ArbolGeneral
from practica1.nodo_general import NodoGeneral

class ArbolGeneralTest(unittest.TestCase):
    def set_tree_with_node(self):
        root_node = NodoGeneral(data="root_node")
        tree = ArbolGeneral(root=root_node)
        return root_node, tree

    def build_tree(self):
        node_1 = NodoGeneral('1')
        tree = ArbolGeneral(node_1)

        node_2 = NodoGeneral('2')
        node_3 = NodoGeneral('3')
        node_4 = NodoGeneral('4')
        node_5 = NodoGeneral('5')
        node_6 = NodoGeneral('6')
        
        node_1.add_child(node_2)
        node_1.add_child(node_3)
        node_2.add_child(node_4)
        node_4.add_child(node_5)
        node_3.add_child(node_6)

        return tree

    def build_big_tree(self):
        node_1 = NodoGeneral('1')
        tree = ArbolGeneral(node_1)

        node_2 = NodoGeneral('2')
        node_3 = NodoGeneral('3')
        node_4 = NodoGeneral('4')
        node_5 = NodoGeneral('5')
        node_6 = NodoGeneral('6')
        node_7 = NodoGeneral('7')
        node_8 = NodoGeneral('8')
        node_9 = NodoGeneral('9')
        
        node_1.add_child(node_2)
        node_1.add_child(node_3)
        node_2.add_child(node_4)
        node_4.add_child(node_5)
        node_3.add_child(node_6)
        node_5.add_child(node_7)
        node_5.add_child(node_8)
        node_5.add_child(node_9)

        return tree

    def test_trees_can_be_created_without_root(self):
        tree = ArbolGeneral()

        self.assertTrue(tree.isEmpty)
    
    def test_general_tree_can_allocate_root_node_only_on_init(self):
        root_node, tree = self.set_tree_with_node()
        
        self.assertEqual(root_node, tree.root)

    def test_can_fetch_root_node_data(self):
        root_node, tree = self.set_tree_with_node()
        
        root_data = tree.root_data

        self.assertEqual(root_node.data, root_data)

    def test_can_retrieve_root_sub_trees(self):
        root_node, tree = self.set_tree_with_node()

        expected_sub_trees = []
        for temp_data in ['nodo-1', 'nodo-2', 'nodo-3']:
            temp_node = NodoGeneral(temp_data)
           
            root_node.add_child(temp_node)
            expected_sub_trees.append(temp_node)
        nodes_of_sub_trees = [tree.root for tree in tree.childs]
        
        self.assertListEqual(expected_sub_trees, nodes_of_sub_trees)

    def test_childs_of_tree_returns_root_childs_as_sub_trees(self):
        root_node, tree = self.set_tree_with_node()

        root_node.add_child(NodoGeneral('nodo-1'))
        root_node.add_child(NodoGeneral('nodo-2'))

        tree_childs = tree.childs
        self.assertIsInstance(tree.childs[0], ArbolGeneral)
        self.assertIsInstance(tree.childs[1], ArbolGeneral)

    def test_can_allocate_new_node_to_root_childs_list(self):
        root_node, tree = self.set_tree_with_node()

        root_node.add_child(NodoGeneral('new-node'))
        nodes_of_sub_trees = [tree.root for tree in tree.childs]
        self.assertListEqual(root_node.childs, nodes_of_sub_trees)

        new_tree_child = ArbolGeneral(NodoGeneral('other-new-node'))
        tree.add_child(new_tree_child)
        nodes_of_sub_trees = [tree.root for tree in tree.childs]
        self.assertListEqual(root_node.childs, nodes_of_sub_trees)

    def test_can_delete_a_child(self):
        root_node, tree = self.set_tree_with_node()

        tree_to_delete = ArbolGeneral(NodoGeneral('delete-me'))
        tree.add_child(tree_to_delete)
        tree.delete_child(tree_to_delete)

        self.assertListEqual([], tree.childs)

    def test_tree_root_can_be_leaf(self):
        root_node, tree = self.set_tree_with_node()

        self.assertTrue(tree.isLeaf)

    def test_tree_height_equal_the_distance_to_the_farest_leaf_counting_edges(self):
        tree = self.build_tree()
        
        self.assertEqual(tree.height(), 3)

    def test_tree_finds_for_a_value_in_sub_trees(self):
        tree = self.build_tree()

        matching_tree = tree.include(data='5')
        self.assertEqual(matching_tree.root_data, '5')

    def test_tree_cannot_find_a_value_that_not_exist(self):
        tree = self.build_tree()

        matching_tree = tree.include(data="i don't exist!")
        self.assertIsNone(matching_tree)

    def test_can_know_level_for_given_value(self):
        tree = self.build_tree()

        self.assertEqual(tree.level(data='5'), 3)

    def test_width_of_tree_equal_max_q_of_nodes_per_level(self):
        tree = self.build_big_tree()

        self.assertEqual(tree.width(), 3)