import unittest

from practica4 import hashs

class TablasDeDispersionTest(unittest.TestCase):
    def test_ejercicio_1(self):
        expected = [[], [45], [], [3, 25], [], [5, 27], [], [], [], [20], [1000]]

        table = hashs.Ex1(size=11)
        table.add(5)
        table.add(20)
        table.add(3)
        table.add(1000)
        table.add(45)
        table.add(27)
        table.add(25)

        self.assertEqual(table.data, expected)

    def test_ejercicio_2_lineal(self):
        expected = [None, 45, None, 3, 25, 5, 27, None, None, 20, 1000]

        table = hashs.Ex2_lineal(size=11)
        table.add(5)
        table.add(20)
        table.add(3)
        table.add(1000)
        table.add(45)
        table.add(27)
        table.add(25)

        self.assertEqual(table.data, expected)

    def test_ejercicio_2_cuadratica(self):
        expected = [None, 45, 25, 3, None, 5, None, None, 27, 20, 1000]

        table = hashs.Ex2_cuadratica(size=11)
        table.add(5)
        table.add(20)
        table.add(3)
        table.add(1000)
        table.add(45)
        table.add(27)
        table.add(25)

        self.assertEqual(table.data, expected)
