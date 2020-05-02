class Cola(object):
    """
        Esta implementación representa una cola (FIFO). Podría utilizarse la clase
        que provee Python, queue.Queue
    """
    def __init__(self):
        self._data = []

    def put(self, _data):
        self._data.append(_data)

    def head(self):
        return self._data[0]

    def get(self):
        head = self._data[0]
        del self._data[0]
        return head

    @property
    def queue(self):
        return self._data

    @property
    def isEmpty(self):
        return not self._data