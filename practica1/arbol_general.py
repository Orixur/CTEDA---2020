from typing import List

from .nodo_general import NodoGeneral

class ArbolGeneral(object):
    def __init__(self, root: NodoGeneral = None):
        self._root = root

    @property
    def root(self):
        return self._root

    @property
    def root_data(self):
        return self.root.data

    @property
    def childs(self) -> List['ArbolGeneral']:
        return [ArbolGeneral(child) for child in self.root.childs]
    
    def add_child(self, new_tree: 'ArbolGeneral'):
        self.root.add_child(new_tree.root)

    def delete_child(self, tree_child: 'ArbolGeneral'):
        self.root.childs.remove(tree_child.root)

    @property
    def isEmpty(self) -> bool:
        return self.root == None

    @property
    def isLeaf(self) -> bool:
        return self.root != None and not self.childs

    def height(self) -> int:
        pass
    
    def level(self) -> int:
        pass