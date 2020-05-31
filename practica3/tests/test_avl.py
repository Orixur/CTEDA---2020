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

    def test_balance_with_left_right_rotation_on_unblanced_insertion(self):
        tree = TreeAVL()
        
        tree.add(3)
        tree.add(1)
        tree.add(2)
        
        a = tree.search(1)

        traverse, n = tree.level_traverse()
        self.assertListEqual(traverse, [2,1,3])

    def test_balance_with_right_left_rotation_on_unblanced_insertion(self):
        tree = TreeAVL()
        
        tree.add(1)
        tree.add(3)
        tree.add(2)
        
        a = tree.search(1)

        traverse, n = tree.level_traverse()
        self.assertListEqual(traverse, [2,1,3])
    
    def test_deletion_of_a_leaf_node_with_no_change_to_balance(self):
        tree = TreeAVL()

        tree.add(6)
        tree.add(3)
        tree.add(10)
        tree.add(4)
        tree.add(2)
        tree.delete(4)

        traverse, n = tree.level_traverse()
        self.assertListEqual(traverse, [6,3,10,2])

    def test_deletion_of_a_leaf_node_and_rebalance_case1(self):
        """
            Caso 1:
                - El arbol izquierdo de la raiz tiene 2 ramas de altura igual
                - Elimino un elemento del arbol derecho de la raiz, haciendo que se desbalancee
                    - El elemento a eliminar es una hoja, por lo tanto solo la elimino
                    - Tengo que hacer una rotación simple izquierda
        """
        tree = TreeAVL()

        tree.add(6)
        tree.add(3)
        tree.add(10)
        tree.add(4)
        tree.add(2)
        tree.delete(10)

        traverse, n = tree.level_traverse()
        self.assertListEqual(traverse, [3,2,6,4])

    def test_deletion_of_a_node_with_one_child_and_rebalance_case2(self):
        """
            Caso 2:
                - El arbol izquierdo de la raiz tiene 2 ramas de altura igual
                - Elimino un elemento del arbol derecho de la raiz, haciendo que se desbalancee
                    - El elemento tiene 1 solo hijo (derecho o izquierdo)
                    - Tengo que hacer un swap entre el nodo a eliminar y la raiz del único subárbol que tiene
                    - Rebalanceo
        """
        tree = TreeAVL()

        tree.add(6)
        tree.add(10)
        tree.add(3)
        tree.add(11)
        tree.add(4)
        tree.delete(3)

        traverse, n = tree.level_traverse()
        self.assertListEqual(traverse, [6,4,10,11])

    def test_deletion_of_a_node_with_two_childs_and_rebalance_case3(self):
        """
            Caso 2:
                - El arbol izquierdo de la raiz tiene 2 ramas de altura igual
                - Elimino un elemento del arbol derecho de la raiz, haciendo que se desbalancee
                    - El elemento tiene 2 solo hijo (derecho o izquierdo)
                    - Cambio de lugares con el predecesor o sucesor (in-orden) y elimino
                    - Rebalanceo
        """
        tree = TreeAVL()

        tree.add(6)
        tree.add(3)
        tree.add(10)
        tree.add(2)
        tree.add(4)
        tree.add(8)
        tree.add(11)
        tree.add(7)
        tree.add(9)
        tree.delete(3)

        traverse, n = tree.level_traverse()
        self.assertListEqual(traverse, [6,2,10,4,8,11,7,9])

        tree = TreeAVL()

        tree.add(6)
        tree.add(3)
        tree.add(9)
        tree.add(2)
        tree.add(4)
        tree.add(8)
        tree.add(11)
        tree.add(7)
        tree.delete(9)

        traverse, n = tree.level_traverse()
        self.assertListEqual(traverse, [6,3,8,2,4,7,11])
