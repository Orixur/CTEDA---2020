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
        elif elemento < self.root_data:
            if self.rightChild:
                res = self.rightChild.search(elemento)
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

    def balanceTree(self):
        if self.isLeaf:
            return
        if self.root.balance > 1:  # se desbalanceo el sub-árbol izquierdo
            if self.root.leftChild.balance < 0:
                # Rotación a izquierda
                # Rotación a derecha
                pass
            else:
                # Rotación a derecha
                self.right_rotation()
        elif self.root.balance < -1:  # se desbalanceo el sub-árbol derecho
            if self.root.leftChild.balance > 0:
                # Rotación a derecha
                # Rotación a izquierda
                pass
            else:
                # Rotación a izquierda
                self.left_rotation()
    
    def right_rotation(self):
        a = self.root
        b = self.root.leftChild
        aux = b.rightChild

        self.root = b
        b.rightChild = a
        a.leftChild = aux

    def updateHeight(self):
        if self.isLeaf:
            self.root.left_h = 0
            self.root.right_h = 0
        else:
            if self.leftChild:
                self.leftChild.updateHeight()
                self.root.left_h = self.leftChild.root.left_h + 1
            if self.rightChild:
                self.rightChild.updateHeight()
                self.root.right_h = self.rightChild.root.right_h + 1

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
