from .binary_tree import BinaryTree

class ProfundidadDeArbolBinario(BinaryTree):
    def sumOnDeep(self, level: int) -> int:
        nodes_in_disered_level = self.traverse_between_levels(n=level , m=level)
        if not nodes_in_disered_level:
            return False  # El nivel pasado como parámetro no es valido
        return sum(nodes_in_disered_level)
