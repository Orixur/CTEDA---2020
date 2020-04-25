class NodoGeneral(object):
    def __init__(self, data):
        self._data = data
        self._childs = [] # type: List[NodoGeneral]

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def childs(self):
        return self._childs
