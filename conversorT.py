class Termometro():
    def __init__(self):
        self.__unidadM='C' #privado
        self.__temperatura=0 #privado
        
    def __conversor(self, temperatura, unidad): #privada
        if unidad == 'C': # si es en centigrados q la convierta en F
            return "{}º F".format(temperatura*9/5+32)
        elif unidad=='F':
            return  "{}ª C".format((temperatura-32)*5/9)
        else:
            return "unidad incorrecta"
    def __str__(self):
        return "{}º {}".format(self.__temperatura, self.__unidadM)
    def unidadMedida(self, uniM=None): #Getter y setter de la unidad de medida
        if uniM== None:
            return self.__unidadM
        else:
            if uniM=='F' or uniM=='C':
                self.__unidadM=uniM
    def temp(self, temperatura=None): #Getter y setter de la temperatura
        if temperatura==None:
            return self.__temperatura
        else:
            self.__temperatura=temperatura
    def mide(self, uniM=None):      #va a devolver el estado en la unidad que le pida
        if uniM==None or uniM==self.__unidadM:
            return self.__str__()
        else:
            return self.__conversor(self.__temperatura, self.__unidadM)