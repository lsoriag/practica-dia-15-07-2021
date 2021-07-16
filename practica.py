#taller en clase POO
#fecha 15-07-2021
#luis Fernando SOria 

class Logica:
    def __init__(self,lista=None):
        self.__lista=lista

    @property
    def lista(self):
        return self.__lista

    @lista.setter
    def lista(self,value):
        self.__lista=value

    def parImpar(self,numero):
        rec=numero%2
        if rec == 0:
            print("{} es par ".format(numero))
        else:
            print("{} es inpar ".format(numero))

    def perfecto(self,numero):
        acu=1
        for contador in range(1,numero):
            rec = numero % contador
            if rec == 0:
                acu=acu+contador

        if acu == numero:
            print("{} es perfecto ".format(numero))
        else:
            print("{} No es perfecto ".format(numero))

class Ejercicio(Logica):
    def __init__(self,lista,numeros):
        super().__init__(lista)
        self.dato=numeros

    def sumar(self,n1,n2):
        return n1+n2

    def parImpar(selft,numero):
        super().parImpar(numero)
        return numero % 2

ejer=Ejercicio([1])
# if ejer.parImpar(6)==0:
#     print ("par")
# else:
#     print("Impar")
