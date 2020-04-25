from typing import List

from .nodo_general import NodoGeneral

class ArbolGeneral(object):
    def __init__(self, root: NodoGeneral):
        self._root = root

    @property
    def root(self):
        return self._root

    @property
    def root_data(self):
        return self._root.data

    @property
    def childs(self) -> List['ArbolGeneral']:
        return [ArbolGeneral(child) for child in self._root.childs]