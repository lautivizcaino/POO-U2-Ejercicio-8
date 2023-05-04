from menu import Menu
from conjunto import Conjunto
from gestorConjuntos import GestorConjuntos
def test():
    lista=GestorConjuntos(4,4)
    lista.leerConjuntos()
    menu=Menu()
    menu.opciones(lista)

if __name__ == '__main__':
    test()