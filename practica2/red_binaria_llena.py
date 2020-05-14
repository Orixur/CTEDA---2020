from .binary_tree import BinaryTree


class RedBinariaLlena(BinaryTree):
    @property
    def leftChild(self) -> 'RedBinariaLlena':
        if self.root.leftChild is None:
            return None
        return RedBinariaLlena(self.root.leftChild)

    @property
    def rightChild(self) -> 'RedBinariaLlena':
        if self.root.rightChild is None:
            return None
        return RedBinariaLlena(self.root.rightChild)

    @leftChild.setter
    def leftChild(self, new_child: 'RedBinariaLlena'):
        if new_child is None:
            self.root.leftChild = None
        else:
            self.root.leftChild = new_child.root
        
    @rightChild.setter
    def rightChild(self, new_child: 'RedBinariaLlena'):
        if new_child is None:
            self.root.rightChild = None
        else:
            self.root.rightChild = new_child.root

    def isFull(self, tree: int = 1) -> bool:
        """
            Verifica si un árbol o sub árbol esta lleno.
            Args:
                - tree (int): por defecto es 1, indicando que evaluará si el arbol h-1 esta lleno o no.
                Si Tree es 0, evaluará si todo el árbol esta completo; en caso de ser mayor a 1 evaluará sub-árboles
        """
        _, bottom_level = self.level_traverse()
        nodes = self.traverse_between_levels(n=bottom_level-tree,m=bottom_level-tree)
        
        return len(nodes) == 2**((bottom_level-tree) - 1)

    def isComplete(self):
        if not self.isFull:
            return False
        _, bottom_level = self.level_traverse()
        penultimate_nodes = self.traverse_between_levels(n=bottom_level-1,m=bottom_level-1, instance=True)
        
        strikes = 0
        for node in penultimate_nodes:
            if node.leftChild is None and node.rightChild is not None:
                strikes += 1
            elif node.leftChild is not None and node.rightChild is None:
                strikes += 1
            
            if strikes >= 2:
                break
        
        return True if strikes < 2 else False

    def redirect_delay(self) -> int:
        if self.isEmpty:
            return 0
        if self.isLeaf:
            return self.root_data
        total = self.root_data

        if self.leftChild is not None:
            sum_left = self.leftChild.redirect_delay()
        if self.rightChild is not None:
            sum_right = self.rightChild.redirect_delay()

        total += max(sum_left, sum_right)
        
        return total