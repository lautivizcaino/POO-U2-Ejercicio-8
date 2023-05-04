import numpy as np
from conjunto import Conjunto
import csv
class GestorConjuntos:
    __listaConjuntos=None
    __dimension=int
    __incremento=int
    __cantidad=int
    def __init__(self,dimension,incremento=1):
        self.__listaConjuntos = np.empty(dimension, dtype=Conjunto)
        self.__incremento=incremento
        self.__dimension=dimension
        self.__cantidad=0
    def agregarConjunto(self,conjunto):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__listaConjuntos.resize(self.__dimension)
        self.__listaConjuntos[self.__cantidad]=conjunto
        self.__cantidad+=1
    def leerConjuntos(self):
        for i in range(self.__dimension):
            unConjunto=Conjunto()
            dim=int(input('\nIngrese la dimension del conjunto %d: '%(self.__cantidad+1)))
            for k in range(dim):
                unConjunto.agregarElemento(int(input('Ingrese el numero entero %d: '%(k+1))))
            self.agregarConjunto(unConjunto)
    def obtenerConjunto(self,num):
        return self.__listaConjuntos[num-1]
    def union(self,c1,c2):
        nuevoConjunto=c1+c2
        print(nuevoConjunto)
    def diferencia(self):
        pass
    def verificar(self):
        pass
    def __str__(self) -> str:
        s=''
        i=1
        for conj in self.__listaConjuntos:
            s+= str(conj) + '\n'
            i+=1
        return s