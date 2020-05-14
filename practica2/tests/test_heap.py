import unittest

from practica2.heaps import MinHeap

class MinHeapTest(unittest.TestCase):
    def test_can_create_heap_from_list(self):
        items = [1,2,3,4,5]
        heap = MinHeap.from_list(items)
        
        recorrido, nivel = heap.level_traverse()

        self.assertEqual(recorrido, items)
        self.assertEqual(nivel, 3)