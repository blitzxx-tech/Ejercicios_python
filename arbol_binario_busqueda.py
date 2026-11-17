class Nodo:
    def __init__(self, clave):
        self.clave = clave
        self.izq = None
        self.der = None


class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, clave):
        if self.raiz is None:
            self.raiz = Nodo(clave)
        else:
            self._insertar_recursivo(self.raiz, clave)

    def _insertar_recursivo(self, actual, clave):
        if clave < actual.clave:
            if actual.izq is None:
                actual.izq = Nodo(clave)
            else:
                self._insertar_recursivo(actual.izq, clave)
        elif clave > actual.clave:
            if actual.der is None:
                actual.der = Nodo(clave)
            else:
                self._insertar_recursivo(actual.der, clave)

    def buscar(self, clave):
        return self._buscar_recursivo(self.raiz, clave)

    def _buscar_recursivo(self, actual, clave):
        if actual is None:
            return False
        if clave == actual.clave:
            return True
        elif clave < actual.clave:
            return self._buscar_recursivo(actual.izq, clave)
        else:
            return self._buscar_recursivo(actual.der, clave)

    def preorden(self):
        resultado = []
        self._preorden_rec(self.raiz, resultado)
        return resultado

    def _preorden_rec(self, actual, lista):
        if actual:
            lista.append(actual.clave)
            self._preorden_rec(actual.izq, lista)
            self._preorden_rec(actual.der, lista)

    def inorden(self):
        resultado = []
        self._inorden_rec(self.raiz, resultado)
        return resultado

    def _inorden_rec(self, actual, lista):
        if actual:
            self._inorden_rec(actual.izq, lista)
            lista.append(actual.clave)
            self._inorden_rec(actual.der, lista)

    def postorden(self):
        resultado = []
        self._postorden_rec(self.raiz, resultado)
        return resultado

    def _postorden_rec(self, actual, lista):
        if actual:
            self._postorden_rec(actual.izq, lista)
            self._postorden_rec(actual.der, lista)
            lista.append(actual.clave)


if __name__ == "__main__":
    abb = ArbolBinarioBusqueda()

    valores = [50, 30, 70, 20, 40, 60, 80]
    for val in valores:
        abb.insertar(val)

    print("Existe 40:", abb.buscar(40))
    print("Existe 99:", abb.buscar(99))

    print("Preorden :", abb.preorden())
    print("Inorden  :", abb.inorden())
    print("Postorden:", abb.postorden())
