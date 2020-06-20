import math

class Ex1:
    def __init__(self, size: int):
        self._data = [[] for i in range(size)]

    @property
    def data(self):
        return self._data
    
    def add(self, d: int):
        i = d%11
        self.data[i].append(d)


class Ex2_lineal(Ex1):
    def __init__(self, size: int):
        self._data = [None] * size

    def add(self, d: int):
        """
            Exploración lineal
        """
        i = d%11
        loops = 0
        visited_indexes = set()
        while True:
            if self.data[i] is None:
                break
            if len(visited_indexes) == len(self._data):
                break
            visited_indexes.add(i)
            i += 1
            loops += 1
            # Calculo nuevo indice (i+1)
            # En este caso si i se pasa del largo de la lista:
            #   - tengo que calcular el indice que tendría luego de dar x vueltas a la lista
            i = abs(len(self.data) * math.floor(i/len(self.data)) - i)
        self.data[i] = d

class Ex2_cuadratica(Ex1):
    def __init__(self, size: int):
        self._data = [None] * size

    def add(self, d: int):
        """
            Exploración lineal
        """
        i = d%11
        loops = 0
        visited_indexes = set()
        while True:
            if self.data[i] is None:
                break
            visited_indexes.add(i)
            # Calculo el nuevo indice (i**2)
            #   - si tengo 5, entonces 5**2 se pasa del largo de la lista...
            #       tendría que calcular el indice posterior a dar varias vueltas a la lista
            i = abs((len(self.data) * math.ceil(i**2 / len(self.data))) - i**2)  # len(data) * i**2/len(data) - i**2
            if len(visited_indexes) == len(self._data):
                break
            loops += 1
        self.data[i] = d
