class BinaryNode(object):
    def __init__(self, data):
        self._data = data
        self._leftChild = None
        self._rightChild = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def leftChild(self):
        return self._leftChild

    @leftChild.setter
    def leftChild(self, new_node: 'BinaryNode'):
        self._leftChild = new_node

    @property
    def rightChild(self):
        return self._rightChild

    @rightChild.setter
    def rightChild(self, new_node: 'BinaryNode'):
        self._rightChild = new_node