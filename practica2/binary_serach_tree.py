from practica1.cola import Cola
from .binary_tree import BinaryTree
from .binary_node import BinaryNode

def new_tree_from_data(data) -> BinaryTree:
    return BinaryTree(BinaryNode(data))

class BinarySearchTree(BinaryTree):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def add(self, elemento):
        """
            Este método deberá implementar la lógica de insertado de un árbol BST:
                - Si no hay raiz, el nodo a insertar se vuelve raiz
                - En caso de que haya raiz, se comienza la inserción por ahí
                - Siempre se comparará por si es mayor o menor a la raiz del árbol actual
                - En caso de ser menor se compara con el hijo izquierdo
                - En caso de ser mayor se compara con el hijo derecho
                - El ciclo termina cuando llega a una hoja, situandose o bien a la derecha;
                - ... o bien a la izquierda

            Versión iterativa
        """
        if self.isEmpty:
            self.root = BinaryNode(elemento)
        current = self
        while not current.isLeaf:  # Cuando termina en una hoja
            if elemento < current.root_data:
                if current.leftChild is not None:
                    current = current.leftChild
                else:
                    break
            else:
                if current.rightChild is not None:
                    current = current.rightChild
                else:
                    break

        if elemento < current.root_data:
            current.leftChild = new_tree_from_data(elemento)
        elif elemento > current.root_data:
            current.rightChild = new_tree_from_data(elemento)

    def searchValue(self, data) -> bool:
        if self.isEmpty:
            return False
        cola = Cola()
        cola.put(self)
        while not cola.isEmpty:
            current = cola.get()
            if current is not None:
                if data == current.root_data:
                    return True
                cola.put(current.leftChild)
                cola.put(current.rightChild)
        return False            
