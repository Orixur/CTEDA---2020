import unittest

from practica3.avl import TreeAVL
from practica3.avl import NodeAVL

class TreeAVLTest(unittest.TestCase):
    def test_avl_can_update_heights_of_all_nodes(self):
        tree = TreeAVL()
        
        tree.add(5)
        self.assertEqual(tree.search(5).root.left_h, 0)
        self.assertEqual(tree.search(5).root.right_h, 0)
        tree.add(4)
        self.assertEqual(tree.search(5).root.left_h, 1)
        tree.add(8)
        self.assertEqual(tree.search(5).root.left_h, 1)
        self.assertEqual(tree.search(5).root.right_h, 1)
        tree.add(3)
        self.assertEqual(tree.search(5).root.left_h, 2)
        self.assertEqual(tree.search(4).root.left_h, 1)

    def test_balance_with_single_right_rotation_on_unblanced_insertion(self):
        tree = TreeAVL()
        
        tree.add(3)
        tree.add(2)
        tree.add(1)

        traverse, n = tree.level_traverse()
        self.assertListEqual(traverse, [2,1,3])

    def test_balance_with_single_left_rotation_on_unblanced_insertion(self):
        tree = TreeAVL()
        
        tree.add(1)
        tree.add(2)
        tree.add(3)

        traverse, n = tree.level_traverse()
        self.assertListEqual(traverse, [2,1,3])
