import unittest

from practica2.heaps import MinHeap, HeapMin

class MinHeapTest(unittest.TestCase):
    def test_can_create_heap_from_list(self):
        items = [1,2,3,4,5]
        heap = MinHeap.from_list(items)
        
        recorrido, nivel = heap.level_traverse()

        self.assertEqual(recorrido, items)
        self.assertEqual(nivel, 3)
    
    def test_can_insert_new_item(self):
        heap = MinHeap()
        
        heap.insert(1)
        heap.insert(2)
        heap.insert(3)

        self.assertListEqual(heap.data, [1,2,3])

    def test_heap_filter_up_after_insertion(self):
        heap = MinHeap()
        
        heap.insert(4)
        self.assertListEqual(heap.data, [4])
        heap.insert(3)
        self.assertListEqual(heap.data, [3,4])
        heap.insert(2)
        self.assertListEqual(heap.data, [2,4,3])
        heap.insert(1)
        self.assertListEqual(heap.data, [1,2,3,4])

    def test_heap_filter_down_after_deletion(self):
        heap = MinHeap(data=[1,2,3,4])

        heap.deleteMin()

        self.assertListEqual(heap.data, [2,4,3])

    def test_ejercicio_6(self):
        heap = MinHeap()
        heap.insert(50)
        self.assertListEqual(heap.data, [50])
        heap.insert(52)
        self.assertListEqual(heap.data, [50, 52])
        heap.insert(41)
        self.assertListEqual(heap.data, [41, 52, 50])
        heap.insert(54)
        self.assertListEqual(heap.data, [41, 52, 50, 54])
        heap.insert(46)
        self.assertListEqual(heap.data, [41, 46, 50, 54, 52])

        heap.deleteMin()
        self.assertListEqual(heap.data, [46, 52, 50, 54])
        heap.deleteMin()
        self.assertListEqual(heap.data, [50, 52, 54])
        heap.deleteMin()
        self.assertListEqual(heap.data, [52, 54])

        heap.insert(45)
        self.assertListEqual(heap.data, [45, 54, 52])
        heap.insert(48)
        self.assertListEqual(heap.data, [45, 48, 52, 54])
        heap.insert(55)
        self.assertListEqual(heap.data, [45, 48, 52, 54, 55])
        heap.insert(43)
        self.assertListEqual(heap.data, [43, 48, 45, 54, 55, 52])

class HeapMinTest(unittest.TestCase):
    def test_heap_can_instantiate_with_filter_down(self):
        heap = HeapMin([50,52,41,54,46])

        self.assertListEqual(heap.data, [41, 46, 50, 54, 52])

    def test_heap_can_insert_and_reorder_values(self):
        heap = HeapMin()
        heap.insert(50)
        self.assertListEqual(heap.data, [50])
        heap.insert(52)
        self.assertListEqual(heap.data, [50, 52])
        heap.insert(41)
        self.assertListEqual(heap.data, [41, 52, 50])
        heap.insert(54)
        self.assertListEqual(heap.data, [41, 52, 50, 54])
        heap.insert(46)
        self.assertListEqual(heap.data, [41, 46, 50, 54, 52])

    def test_heap_can_filter_down_on_min_delete(self):
        heap = MinHeap()
        heap.insert(50)
        self.assertListEqual(heap.data, [50])
        heap.insert(52)
        self.assertListEqual(heap.data, [50, 52])
        heap.insert(41)
        self.assertListEqual(heap.data, [41, 52, 50])
        heap.insert(54)
        self.assertListEqual(heap.data, [41, 52, 50, 54])
        heap.insert(46)
        self.assertListEqual(heap.data, [41, 46, 50, 54, 52])

        heap.deleteMin()
        self.assertListEqual(heap.data, [46, 52, 50, 54])
        heap.deleteMin()
        self.assertListEqual(heap.data, [50, 52, 54])
        heap.deleteMin()
        self.assertListEqual(heap.data, [52, 54])
