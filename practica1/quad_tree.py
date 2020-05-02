from typing import List
from collections.abc import Iterable

from .arbol_general import ArbolGeneral
from .nodo_general import NodoGeneral

class QuadTree(ArbolGeneral):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def childs(self) -> List['QuadTree']:
        try:
            return [QuadTree(child) for child in self.root.childs]
        except Exception as e:
            print(e)

    def add_child(self, list_of_childs: List[NodoGeneral]):
        for child in list_of_childs:
            self.root.add_child(child)
    
    def pixel_count(self, size: int, color: str):
        if self.isLeaf:
            return size if self.root_data == color else 0
        child_block_size = size / 4
        block_sum = 0
        for c in self.childs:
            block_sum += c.pixel_count(size=child_block_size, color=color)

        return block_sum

