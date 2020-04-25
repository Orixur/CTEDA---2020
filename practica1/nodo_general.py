from typing import List

class NodoGeneral(object):
    def __init__(self, data: object):
        self._data: object = data
        self._childs = [] # type: List[NodoGeneral]

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def childs(self) -> List:
        return self._childs

    def add_child(self, new_child):
        self._childs.append(new_child)