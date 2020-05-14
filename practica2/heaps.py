import math

from practica1.cola import Cola
from .binary_tree import BinaryTree
from .binary_node import BinaryNode


class MinHeap(BinaryTree):
    """
        Implementación de una MinHeap. Originalmente pensada para que use nodos.

        Esta implementación esta hecha sobre la implementación base de un árbol binario.
        (No aprovecha las funcionalidades de un BinaryTree)
        Para ver la implementación de una Heap, referirse al objeto Heap() en este módulo.

        Attributes:
            root (BinaryNode): En caso de usar la heap con nodos
            data (list): lista de datos, cada elemento "es un nodo"
    """
    def __init__(self, root: BinaryNode = None, data: list = None):
        self._root = root
        self._data = data or list()

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_list: list):
        self.data = new_list

    def insert(self, value):
        """
            Inserta un valor en el atributo 'data' y aplica un reordenamiento hacía arriba.
            Una vez insertado al final, va de padre en padre hasta la raiz, fijandose si el
            valor agregado es menor a su padre, en cada paso hacía la raiz.
        """
        self.data.append(value)
        
        # Going backwards
        current_child = self.data.index(value)
        current_parent = math.ceil(current_child / 2) - 1 # -1 because index starts from 0
        while True:
            # Intercambio la posición del hijo y el padre en caso de que el hijo sea menor
            if self.data[current_child] < self.data[current_parent]:
                aux = self.data[current_parent]
                self.data[current_parent] = self.data[current_child]
                self.data[current_child] = aux
            # Apunto al proximo padre y guardo el hijo actual
            current_child = current_parent
            current_parent = math.ceil(current_child / 2) - 1
            if current_parent == -1:
                break

    def deleteMin(self):
        """
            Elimina el menor valor (raiz) del heap, y aplica un reordenamiento
            hacía abajo.
            Una vez que saca la raiz, pone el ultimo nodo de raiz, y va comparandose
            (en caso de tener hijos) con su hijo mas pequeño. Si aplica, cambia de posición
            y repite, hasta que no se cumpla la condición de tamaño o bien sea una hoja 
            (pase la mitad de la lista de datos).
        """
        deleted_value = self.data[0]
        self.data[0] = self.data[-1]
        del self.data[-1]
        data_len = len(self.data)
        
        current = 0
        while True:
            # Si pasa la mitad de los elementos, es una hoja; ya no puede ser reordenado
            if current > int(len(self.data) / 2)-1:
                break
            # Guardo los indices y datos de los hijos para no repetir
            left_child_formula = (current*2) + 1
            right_child_formula = (current*2) + 2
            min_child = None
            
            if left_child_formula < data_len:
                left_child = self.data[left_child_formula]
            else:
                left_child = None

            if right_child_formula < data_len:
                right_child = self.data[right_child_formula]
            else:
                right_child = None
            
            if right_child is None or left_child < right_child:
                designed = {'index': left_child_formula, 'data': left_child}
            elif left_child is None or right_child < left_child:
                designed = {'index': right_child_formula, 'data': right_child}
            
            # Cambio de lugares al hijo mas chico con la raiz actual (current) solo si el hijo mas pequeño es menor
            if self.data[current] > self.data[designed['index']]:
                aux = designed['data']
                self.data[designed['index']] = self.data[current]
                self.data[current] = aux

                # Como la raiz se mueve a la posición donde estaba su hijo mas pequeño,
                # la proxima raiz se situara allí
                current = designed['index']
            else:
                break

    @staticmethod
    def from_list(data: list):
        """
            Este método generará un arbol de nodos BinaryNode, a partir de una
            lista recibida como parámetro.
        """
        if not data:
            return  # No data provided
        nodes_with_childs = int(len(data) / 2)
        cola = Cola()
        current_n = 0
        root = BinaryNode(data[0])
        cola.put([current_n, root])

        while not cola.isEmpty:
            n = cola.get()
            if n[0] >= nodes_with_childs:
                break
            left = (n[0]*2) + 1  # index from 0
            right = (n[0]*2) + 2  # index from 0

            current = n[1]
            if data[left] is not None:
                current.leftChild = BinaryNode(data[left])
            if data[right] is not None:
                current.rightChild = BinaryNode(data[right])

            if current.leftChild is not None and left <= nodes_with_childs:
                cola.put([left, current.leftChild])
            if current.rightChild is not None and right <= nodes_with_childs:
                cola.put([right, current.rightChild])
        
        return MinHeap(root)


class HeapMin(object):
    def __init__(self, data: list = []):
        self._data = data
        self.make_heap()

    @property
    def data(self):
        return self._data

    def make_heap(self):
        current = int(len(self.data) / 2)-1

        # Recorro desde el ultimo 'nodo' con hojas (el que esta en la mitad)
        # en sentido a la raiz.
        for n in reversed(range(0, current+1)):
            self.filter_down(current=n)

    def insert(self, value):
        """
            Inserta un valor en el atributo 'data' y aplica un reordenamiento hacía arriba.
            Una vez insertado al final, va de padre en padre hasta la raiz, fijandose si el
            valor agregado es menor a su padre, en cada paso hacía la raiz.
        """
        self.data.append(value)
        
        # Going backwards
        current_child = self.data.index(value)
        current_parent = math.ceil(current_child / 2) - 1 # -1 because index starts from 0
        while True:
            # Intercambio la posición del hijo y el padre en caso de que el hijo sea menor
            if self.data[current_child] < self.data[current_parent]:
                aux = self.data[current_parent]
                self.data[current_parent] = self.data[current_child]
                self.data[current_child] = aux
            # Apunto al proximo padre y guardo el hijo actual
            current_child = current_parent
            current_parent = math.ceil(current_child / 2) - 1
            if current_parent == -1:
                break

    def deleteMin(self):
        """
            Elimina el menor valor (raiz) del heap, y aplica un reordenamiento
            hacía abajo.
            Una vez que saca la raiz, pone el ultimo nodo de raiz, y va comparandose
            (en caso de tener hijos) con su hijo mas pequeño. Si aplica, cambia de posición
            y repite, hasta que no se cumpla la condición de tamaño o bien sea una hoja 
            (pase la mitad de la lista de datos).
        """
        deleted_value = self.data[0]
        self.data[0] = self.data[-1]
        del self.data[-1]

        self.filter_down()
        
        return deleted_value
        
    def filter_down(self, current: int = 0):
        data_len = len(self.data)
        while True:
            # Si pasa la mitad de los elementos, es una hoja; ya no puede ser reordenado
            if current > int(len(self.data) / 2)-1:
                break
            # Guardo los indices y datos de los hijos para no repetir
            left_child_formula = (current*2) + 1
            right_child_formula = (current*2) + 2
            min_child = None
            
            if left_child_formula < data_len:
                left_child = self.data[left_child_formula]
            else:
                left_child = None

            if right_child_formula < data_len:
                right_child = self.data[right_child_formula]
            else:
                right_child = None
            
            if right_child is None or left_child < right_child:
                designed = {'index': left_child_formula, 'data': left_child}
            elif left_child is None or right_child < left_child:
                designed = {'index': right_child_formula, 'data': right_child}
            
            # Cambio de lugares al hijo mas chico con la raiz actual (current) solo si el hijo mas pequeño es menor
            if self.data[current] > self.data[designed['index']]:
                aux = designed['data']
                self.data[designed['index']] = self.data[current]
                self.data[current] = aux

                # Como la raiz se mueve a la posición donde estaba su hijo mas pequeño,
                # la proxima raiz se situara allí
                current = designed['index']
            else:
                break
