class Operaciones:
    def __init__(self, numeros):
        self.numeros = numeros

    def calcularMedia(self):
        if not self.numeros:
            raise ValueError("La lista de numeros esta vacia.")
        return sum(self.numeros)/len(self.numeros)

