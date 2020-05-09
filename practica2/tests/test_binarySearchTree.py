import unittest

from practica2.binary_serach_tree import BinarySearchTree
from practica2.binary_node import BinaryNode


class BinarySearchTreeTest(unittest.TestCase):
    def make_BTS(self):
        root = BinaryNode(5)
        tree = BinarySearchTree(root)
        seq = [10,3,1,4,2,6,12]
        
        for data in seq:
            tree.add(data)
        
        return tree

    def test_binary_search_tree_can_insert_new_value_with_existing_root(self):
        root = BinaryNode(5)
        tree = BinarySearchTree(root)

        tree.add(10)
        self.assertEqual(tree.root.rightChild.data, 10)

        tree.add(3)
        self.assertEqual(tree.root.leftChild.data, 3)

        tree.add(1)
        root_left_child = tree.root.leftChild
        self.assertEqual(root_left_child.leftChild.data, 1)

        tree.add(4)
        root_left_child = tree.root.leftChild
        self.assertEqual(root_left_child.rightChild.data, 4)

        tree.add(6)
        root_right_child = tree.root.rightChild
        self.assertEqual(root_right_child.leftChild.data, 6)

        tree.add(12)
        root_right_child = tree.root.rightChild
        self.assertEqual(root_right_child.rightChild.data, 12)

        tree.add(2)
        root_left_child_left_child = tree.root.leftChild.leftChild
        self.assertEqual(root_left_child_left_child.rightChild.data, 2)

    def test_cannot_add_a_repeated_value(self):
        tree = self.make_BTS()

        res = tree.add(5)

        self.assertFalse(res)

    def test_tree_can_search_for_a_value(self):
        tree = self.make_BTS()

        res = tree.searchValue(data=12)

        self.assertTrue(res)
    
    def test_cannot_find_a_value_that_donot_exist(self):
        tree = self.make_BTS()

        res = tree.searchValue(data=10000000)

        self.assertFalse(res)

    def test_all_traversals_works_properly(self):
        tree = self.make_BTS()

        inorder = tree.inorder()
        preorder = tree.preorder()
        postorder = tree.postorder()

        self.assertListEqual(inorder, [1,2,3,4,5,6,10,12])
        self.assertListEqual(preorder, [5,3,1,2,4,10,6,12])
        self.assertListEqual(postorder, [2,1,4,3,6,12,10,5])