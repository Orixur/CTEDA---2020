from typing import List

from .nodo_general import NodoGeneral
from .cola import Cola

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
        """
            Esta función se encarga de hacer un recorrido preorden, para encontrar la altura (= height = h) para la instancia del árbol
        """
        if self.isLeaf:
            return 0 # Si quisiera contar por nodos y no por aristas, debería devolver 1 cuando encuentro una arista
        heights = []
        for c in self.childs:
            heights.append(c.height())
        return 1 + max(heights)

    def include(self, data) -> bool:
        """
            Esta función chequea si un valor se haya en sus sub árboles. Esta función NO verifica por posibles datos duplicados, se
            asume que la estructura de datos no almacena duplicados.
        """
        if self.root_data == data:
            return self
        matching_tree = None
        for c in self.childs:
            matching_tree = c.include(data=data)
            if matching_tree is not None:
                break
        return matching_tree

    def level(self, data) -> int:
        """
            Esta función encontrará la distancia entre la Raiz y el Dato provisto como parámetro. El calculo se realiza contando arista.
        """
        matching_tree = self.include(data=data)
        if not matching_tree:
            return
        if matching_tree == self:
            return 0
        q = Cola()
        q.put(self.root)
        level = 0
        while not q.isEmpty:
            current_node = q.get()
            if current_node is None:
                level += 1
                continue
            elif current_node.data == data:
                break
            for child in current_node.childs:
                q.put(child)
            q.put(None) # Sentinel value, marca de fin de nivel
        
        return level