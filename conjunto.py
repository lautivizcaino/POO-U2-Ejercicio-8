class Conjunto:
    __elementos=None
    def __init__(self):
        self.__elementos=[]
    def agregarElemento(self,elemento):
        self.__elementos.append(elemento)
    def eliminarEl(self,elemento):
        self.__elementos.remove(elemento)
    def obtenerConjunto(self):
        return self.__elementos
    def __add__(self,otro):
        nuevoConjunto=Conjunto()
        for el in self.__elementos:
            nuevoConjunto.agregarElemento(el)
        for elem in otro.__elementos:
            if elem not in self.__elementos:
                nuevoConjunto.agregarElemento(elem)
                
        return  nuevoConjunto

    def __sub__(self,otro):
        nuevoConjunto=Conjunto()
        for el in self.__elementos:
            nuevoConjunto.agregarElemento(el)
        for elem in otro.__elementos:
            if elem in nuevoConjunto.obtenerConjunto():
                nuevoConjunto.eliminarEl(elem)
        return  nuevoConjunto
    
    def __eq__(self,otro):
        iguales=True
        if len(self.__elementos)==len(otro.__elementos):
            for elem in self.__elementos:
                if elem not in otro.__elementos:
                    iguales=False
            for elem in otro.__elementos:
                if elem not in self.__elementos:
                    iguales=False
        else:
            iguales=False
        return iguales
                
        
    def __str__(self):
        s='{'
        i=0
        for elem in self.__elementos:
            s+= str(elem)
            if i==len(self.__elementos)-1:
                s+= '}'
            else:
                s+=', '
            i+=1
        return s