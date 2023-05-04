class Conjunto:
    __elementos=None
    def __init__(self):
        self.__elementos=[]
    def agregarElemento(self,elemento):
        self.__elementos.append(elemento)
    def __add__(self,otro):
        b=True
        nuevoConjunto=Conjunto()
        for elem in otro.__elementos:
            for k in self.__elementos:
                if elem==k:
                    b=False
            if b==True:
                nuevoConjunto.agregarElemento(k)
        return  

    def __sub__(self):
        pass
    def __eq__(self):
        pass
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