from conjunto import Conjunto
from gestorConjuntos import GestorConjuntos
class Menu:
    __opcion=int
    def __init__(self):
        self.__opcion=4
    def opciones(self,lista):
        while self.__opcion!=0:
            print('1 - Union de conjuntos')
            print('2 - Diferencia de conjuntos')
            print('3 - Verificacion de conjuntos')
            print('0 - Salir\n')
            self.__opcion=int(input('Ingrese opcion a ejecutar: '))
            if self.__opcion==1:
                print('\nPUNTO 1\n')
                print(lista)
                print('\nSeleccione dos conjuntos\n')
                conjunto1=lista.obtenerConjunto(int(input('Conjunto 1: ')))
                conjunto2=lista.obtenerConjunto(int(input('Conjunto 2: ')))
                lista.union(conjunto1,conjunto2)
            if self.__opcion==2:
                print('\nPUNTO 2\n')
            if self.__opcion==3:
                print('\nPUNTO 3\n')
        
        else:
            print('Ha salido del sistema')