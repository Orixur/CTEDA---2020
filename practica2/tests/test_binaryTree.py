import unittest

from practica2.binary_tree import BinaryTree
from practica2.binary_node import BinaryNode

class BinaryTreeTest(unittest.TestCase):
    def build_basic_tree(self):
        root = BinaryNode('root-node')
        tree = BinaryTree(root)
        left_child = BinaryTree(BinaryNode('left-child'))
        right_child = BinaryTree(BinaryNode('right-child'))

        tree.leftChild = left_child
        tree.rightChild = right_child

        return tree, left_child.root, right_child.root

    def build_mid_tree(self):
        node_1 = BinaryNode(1)
        tree = BinaryTree(node_1)
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
        node_5.leftChild = node_6
        node_5.rightChild = node_7

        return tree

    def test_cannot_instantiate_binary_tree_without_root(self):
        with self.assertRaises(TypeError) as context:
            tree = BinaryTree()

    def test_can_set_and_access_root_childs(self):
        tree, left_child, right_child = self.build_basic_tree()

        self.assertEqual(tree.leftChild.root, left_child)
        self.assertEqual(tree.rightChild.root, right_child)

    def test_tree_can_delete_root_childs(self):
        tree, left_child, right_child = self.build_basic_tree()

        tree.leftChild = None
        self.assertEqual(tree.leftChild, None)

        tree.rightChild = None
        self.assertEqual(tree.rightChild, None)

    def test_tree_is_leaf_when_root_doesnot_have_any_child(self):
        root = BinaryNode('leaf-root')
        tree = BinaryTree(root)

        self.assertTrue(tree.isLeaf)

    def test_inorder_traversal(self):
        tree = self.build_mid_tree() # [1, 2, 3, 4, 5, 6, 7]

        traverse = tree.inorder()
        self.assertListEqual(traverse, [4, 2, 6, 5, 7, 1, 3])

    def test_preorden_traversal(self):
        tree = self.build_mid_tree() # [1, 2, 3, 4, 5, 6, 7]

        traverse = tree.preorder()
        self.assertListEqual(traverse, [1, 2, 4, 5, 6, 7, 3])

    def test_postorder_traversal(self):
        tree = self.build_mid_tree() # [1, 2, 3, 4, 5, 6, 7]

        traverse = tree.postorder()
        self.assertListEqual(traverse, [4, 6, 7, 5, 2, 3, 1])

    def test_level_traverse(self):
        tree = self.build_mid_tree() # [1, 2, 3, 4, 5, 6, 7]

        traverse, level = tree.level_traverse()
        self.assertListEqual(traverse, [1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(level, 4)

    def test_tree_can_count_all_leafs(self):
        tree = self.build_mid_tree() # [1, 2, 3, 4, 5, 6, 7]

        self.assertEqual(tree.count_leafs(), 4)

    def test_tree_can_traverse_between_levels(self):
        tree = self.build_mid_tree() # [1, 2, 3, 4, 5, 6, 7]

        traverse = tree.traverse_between_levels(n=3, m=4)
        self.assertEqual(traverse, [4, 5, 6, 7])

    def test_exercise_5_aritmetic_results(self):
        root = BinaryNode('-')
        tree = BinaryTree(root)
        node_2 = BinaryTree(BinaryNode('+'))
        node_3 = BinaryTree(BinaryNode('+'))
        node_4 = BinaryTree(BinaryNode('A'))
        node_5 = BinaryTree(BinaryNode('B'))
        node_6 = BinaryTree(BinaryNode('*'))
        node_7 = BinaryTree(BinaryNode('E'))
        node_8 = BinaryTree(BinaryNode('C'))
        node_9 = BinaryTree(BinaryNode('D'))

        tree.leftChild = node_2
        tree.rightChild = node_3
        node_2.leftChild = node_4
        node_2.rightChild = node_5
        node_3.leftChild = node_6
        node_3.rightChild = node_7
        node_6.leftChild = node_8
        node_6.rightChild = node_9

        print(tree.preorder())
        print(tree.inorder())
        print(tree.postorder())
