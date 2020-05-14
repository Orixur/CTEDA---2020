from typing import List

from .binary_node import BinaryNode
from practica1.cola import Cola

class BinaryTree(object):
    def __init__(self, root: BinaryNode):
        self._root = root

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, new_root):
        self._root = new_root

    @property
    def root_data(self):
        return self.root.data

    @property
    def leftChild(self) -> 'BinaryTree':
        if self.root.leftChild is None:
            return None
        return BinaryTree(self.root.leftChild)
        
    @property
    def rightChild(self) -> 'BinaryTree':
        if self.root.rightChild is None:
            return None
        return BinaryTree(self.root.rightChild)

    @leftChild.setter
    def leftChild(self, new_child: 'BinaryTree'):
        if new_child is None:
            self.root.leftChild = None
        else:
            self.root.leftChild = new_child.root
        
    @rightChild.setter
    def rightChild(self, new_child: 'BinaryTree'):
        if new_child is None:
            self.root.rightChild = None
        else:
            self.root.rightChild = new_child.root

    @property
    def isLeaf(self) -> bool:
        return self.root is not None and self.root.rightChild is None and self.root.leftChild is None

    @property
    def isEmpty(self) -> bool:
        return self.root == None

    def inorder(self) -> List[int]:
        if not self.isEmpty and self.isLeaf:
            return [self.root_data]
        traverse = []
        if self.leftChild is not None:
            traverse += self.leftChild.inorder()
        traverse += [self.root_data]
        if self.rightChild is not None:
            traverse += self.rightChild.inorder()

        return traverse

    def preorder(self) -> List[int]:
        if not self.isEmpty and self.isLeaf:
            return [self.root_data]
        traverse = []
        traverse += [self.root_data]
        if self.leftChild is not None:
            traverse += self.leftChild.preorder()
        if self.rightChild is not None:
            traverse += self.rightChild.preorder()

        return traverse
    
    def postorder(self) -> List[int]:
        if not self.isEmpty and self.isLeaf:
            return [self.root_data]
        traverse = []
        if self.leftChild is not None:
            traverse += self.leftChild.postorder()
        if self.rightChild is not None:
            traverse += self.rightChild.postorder()
        traverse += [self.root_data]

        return traverse

    def level_traverse(self) -> (List[int], int):
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
            traverse.append(current_node.data)
            if current_node.leftChild is not None:
                q.put(current_node.leftChild)
            if current_node.rightChild is not None:
                q.put(current_node.rightChild)

        return traverse, level

    def count_leafs(self) -> int:
        if self.isEmpty:
            return 0
        if self.isLeaf:
            return 1
        counter = 0
        counter += self.leftChild.count_leafs()
        counter += self.rightChild.count_leafs()
        return counter

    def traverse_between_levels(self, n: int, m: int, instance: bool = False) -> List[int]:
        if not self.isEmpty and self.isLeaf:
            return [self.root_data] if n <= 1 <= m else None
        q = Cola()
        q.put(self.root)
        q.put(None)
        level = 1
        traverse = []
        while not q.isEmpty:
            current_node = q.get()
            if current_node is None:
                level += 1
                if q.isEmpty:
                    break
                q.put(None)
                continue
            if n <= level <= m:
                if not instance:
                    traverse.append(current_node.data)
                else:
                    traverse.append(current_node)
            if current_node.leftChild is not None:
                q.put(current_node.leftChild)
            if current_node.rightChild is not None:
                q.put(current_node.rightChild)

        return traverse