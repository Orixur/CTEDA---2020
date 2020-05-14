from practica1.cola import Cola
from .binary_tree import BinaryTree
from .binary_node import BinaryNode

class MinHeap(BinaryTree):
    def __init__(self, root: BinaryNode = None):
        self._root = root

    def from_list(self, data: list):
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
            left = (n[0]*2) + 1
            right = (n[0]*2) + 2

            current = n[1]
            if data[left] is not None:
                current.leftChild = BinaryNode(data[left])
            if data[right] is not None:
                current.rightChild = BinaryNode(data[right])

            if current.leftChild is not None and left <= nodes_with_childs:
                cola.put([left, current.leftChild])
            if current.rightChild is not None and right <= nodes_with_childs:
                cola.put([right, current.rightChild])
        
        self.root = root
