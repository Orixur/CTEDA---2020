import unittest

from practica1.cola import Cola

class ColaTest(unittest.TestCase):
    def test_queuing_data_first_in_first_out(self):
        q = Cola()
        q.put('1')
        q.put('2')
        q.put('3')

        self.assertEqual(q.head(), '1')

    def test_dequeuing_data_returns_head_of_queue(self):
        q = Cola()
        q.put('2')
        q.put('1')
        q.put('3')

        self.assertEqual(q.get(), '2')
        self.assertListEqual(q.queue, ['1','3'])