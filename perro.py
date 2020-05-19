class Dog():
    def __init__(self):
        self.nombre=""
        self.edad=None
        self.peso=None
    def ladrar(self):
        if self.peso==None:
            print("soy un fantasma")
            
        if self.peso>=8:
            print("GUAU,GUAU")
        else:
            print("guau,guau")
            
class Perro():
    def __init__(self, nombre, edad, peso):
        self.nombre=nombre
        self.edad=edad
        self.peso=peso
    def ladrar(self):#self se puede cambiar por cualquier cosa p.e. me. c es una cadena
        if self.peso>=8:
            print("GUAU,GUAU")
        else:
            print("guau,guau")
    def __str__(self): #Sustituye a <__main__.Perro object at 0x03D3BBD0> cuando le damos a print para imprimir el tipo 
        return "Soy el perro {}, con edad: {} años y peso: {} kg".format(self.nombre, self.edad,self.peso)

class PerroAsistencia(Perro):
    def __init__(self, nombre, edad, peso, amo):
        Perro.__init__(self, nombre, edad, peso)
        self.amo=amo
        self.__trabajando=False #Atributo privado, no puedo acceder desde fuera (desde el Shell) para acceder hay q poner .trabajando()
    def __str__(self): 
        return "perro de asistencia de {}".format(self.amo)
    def pasear(self):
        print("{} ayudo a mi dueño {} a pasear".format(self.nombre, self.amo))

    def ladrar(self):
        if self.trabajando:
            print("shhh, no puedo ladrar")
        else:
            Perro.ladrar(self)
    def trabajando(self, valor=None):
        if valor==None:
            return self.__trabajando
        else:
            self.__trabajando_=valor