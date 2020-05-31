from practica1.cola import Cola
from practica2.binary_serach_tree import BinarySearchTree
from practica2.binary_node import BinaryNode


class NodeAVL(BinaryNode):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._left_h = 0
        self._right_h = 0
    
    @property
    def balance(self):
        return self.left_h - self.right_h

    @property
    def left_h(self):
        return self._left_h
    
    @left_h.setter
    def left_h(self, value: int):
        self._left_h = value

    @property
    def right_h(self):
        return self._right_h
    
    @right_h.setter
    def right_h(self, value: int):
        self._right_h = value


class TreeAVL:
    def __init__(self, root: NodeAVL = None):
        self._root = root

    @property
    def root(self):
        return self._root
    
    @root.setter
    def root(self, value: NodeAVL):
        self._root = value

    @property
    def leftChild(self):
        if self.root.leftChild is None:
            return None
        return TreeAVL(self.root.leftChild)

    @leftChild.setter
    def leftChild(self, value):
        self.root.leftChild = value

    @property
    def rightChild(self):
        if self.root.rightChild is None:
            return None
        return TreeAVL(self.root.rightChild)
        
    @rightChild.setter
    def rightChild(self, value):
        self.root.rightChild = value

    @property
    def root_data(self):
        return self._root.data

    @property
    def isEmpty(self):
        return True if self._root is None else False

    @property
    def isLeaf(self):
        return True if self._root.leftChild is None and self._root.rightChild is None else False

    def search(self, elemento):
        if self.isEmpty:
            return
        if elemento == self.root_data:
            return self
        if elemento < self.root_data:
            if self.leftChild:
                res = self.leftChild.search(elemento)
        elif elemento > self.root_data:
            if self.rightChild:
                res = self.rightChild.search(elemento)
        return res

    def search_parent(self, elemento):
        if self.isLeaf:
            return
        if elemento == self.leftChild.root_data or elemento == self.rightChild.root_data:
            return self
        if elemento < self.root_data:
            res = self.leftChild.search_parent(elemento)
        if elemento > self.root_data:
            res = self.rightChild.search_parent(elemento)
        return res

    def add(self, elemento):
        if self.isEmpty:
            self.root = NodeAVL(elemento)
        elif elemento < self.root_data:
            if self.leftChild is None:
                self.leftChild = NodeAVL(elemento)
            else:
                self.leftChild.add(elemento)
        elif elemento > self.root_data:
            if self.rightChild is None:
                self.rightChild = NodeAVL(elemento)
            else:
                self.rightChild.add(elemento)
        self.updateHeight()
        self.balanceTree()

    @staticmethod
    def predecessor(tree):
        z = tree.leftChild
        while not z.rightChild is None:
            z = z.rightChild
        
        return z.root

    @staticmethod
    def successor(tree):
        z = tree.rightChild
        while not z.leftChild is None:
            z = z.leftChild
        
        return z.root

    def delete(self, elemento):        
        parent_of_element = self.search_parent(elemento)
        if elemento < parent_of_element.root_data:
            if parent_of_element.leftChild.isLeaf:
                # Just delete
                parent_of_element.leftChild = None
            elif parent_of_element.leftChild.leftChild is not None and parent_of_element.leftChild.rightChild is None:
                aux = parent_of_element.leftChild.leftChild.root
                parent_of_element.leftChild = None
                parent_of_element.leftChild = aux
            elif parent_of_element.leftChild.leftChild is None and parent_of_element.leftChild.rightChild is not None:
                aux = parent_of_element.leftChild.rightChild.root
                parent_of_element.leftChild = None
                parent_of_element.leftChild = aux
            elif parent_of_element.leftChild.leftChild is not None and parent_of_element.leftChild.rightChild is not None:
                # Como tiene 2 hijos, puedo tomar una de las siguientes opciones:
                #   1. Hago un swap entre el mas grande del árbol izquierdo;
                #   2. Hago un swap entre el mas chico del árbol derecho
                predecessor = self.predecessor(parent_of_element.leftChild)
                aux_right_of_delete = parent_of_element.leftChild.rightChild.root
                predecessor.rightChild = aux_right_of_delete
                parent_of_element.leftChild = predecessor
        elif elemento > parent_of_element.root_data:
            if parent_of_element.rightChild.isLeaf:
                # Just delete
                parent_of_element.rightChild = None
            elif parent_of_element.rightChild.leftChild is not None and parent_of_element.rightChild.rightChild is None:
                aux = parent_of_element.leftChild.leftChild.root
                parent_of_element.rightChild = None
                parent_of_element.rightChild = aux
            elif parent_of_element.rightChild.leftChild is None and parent_of_element.rightChild.rightChild is not None:
                aux = parent_of_element.rightChild.rightChild.root
                parent_of_element.rightChild = None
                parent_of_element.rightChild = aux
            elif parent_of_element.rightChild.leftChild is not None and parent_of_element.rightChild.rightChild is not None:
                # Como tiene 2 hijos, puedo tomar una de las siguientes opciones:
                #   1. Hago un swap entre el mas grande del árbol izquierdo;
                #   2. Hago un swap entre el mas chico del árbol derecho
                predecessor = self.predecessor(parent_of_element.rightChild)
                aux_right_of_delete = parent_of_element.rightChild.rightChild.root
                predecessor.rightChild = aux_right_of_delete
                parent_of_element.rightChild = predecessor
        self.updateHeight()
        self.balanceTree()

    def balanceTree(self):
        if self.isLeaf:
            return
        if self.root.balance > 1:  # se desbalanceo el sub-árbol izquierdo
            if self.root.leftChild.balance < 0:
                self.leftChild = self.leftChild.left_rotation()
                self.right_rotation()
            else:
                self.right_rotation()
        elif self.root.balance < -1:  # se desbalanceo el sub-árbol derecho
            if self.root.rightChild.balance > 0:
                self.rightChild = self.rightChild.right_rotation()
                self.left_rotation()
            else:
                self.left_rotation()
    
    def right_rotation(self):
        a = self.root
        b = a.leftChild
        aux = b.rightChild

        self.root = b
        b.rightChild = a
        a.leftChild = aux
        return self.root
    
    def left_rotation(self):
        a = self.root
        b = a.rightChild
        aux = b.leftChild

        self.root = b
        b.leftChild = a
        a.rightChild = aux
        return self.root

    def updateHeight(self):
        if self.isLeaf:
            self.root.left_h = 0
            self.root.right_h = 0
        else:
            if self.leftChild:
                self.leftChild.updateHeight()
                self.root.left_h = max(self.leftChild.root.left_h, self.leftChild.root.right_h) + 1
            else:
                self.root.left_h = 0
            if self.rightChild:
                self.rightChild.updateHeight()
                self.root.right_h = max(self.rightChild.root.left_h, self.rightChild.root.right_h) + 1
            else:
                self.root.right_h = 0

    def level_traverse(self):
        if not self.isEmpty and self.isLeaf:
            return [self.root_data], 1
        q = Cola()
        q.put(self.root)
        q.put(None)
        level = 0
        traverse = []
        while not q.isEmpty:
            current_node = q.get()
            if current_node is None:
                level += 1
                if q.isEmpty:
                    break
                q.put(None)
                continue
            # print(current_node.data, current_node.balance, current_node.left_h, current_node.right_h)
            traverse.append(current_node.data)
            if current_node.leftChild is not None:
                q.put(current_node.leftChild)
            if current_node.rightChild is not None:
                q.put(current_node.rightChild)

        return traverse, level
