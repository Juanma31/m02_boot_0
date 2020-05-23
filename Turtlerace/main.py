#utilizando la toeria del programa cicloPyGame.py
import pygame, sys
import random 

class Runner():
    __customes = ('turtle','fish','prawn','moray','octopus')
    
    def __init__(self,x=0,y=0): #crear el corredor en la coordenada 0,0 con disfraz (por defecto es tortuga)
        
        ixCustome =random.randint(0,4) #genera un numero random
        
        self.custome = pygame.image.load("images/{}.png".format(self.__customes[ixCustome])) #obtiene un disfraz random 
        self.position = [x,y]
        self.name = "" #para cuando gane que se muestre el nombre del ganador
    
    def avanza (self): #metodo para avanzar los corredores
        self.position[0]+=random.randint(1,6) #lanzar los dados aleatorios del 1 al 6 entero
        
        

class Game():
    runners = []
    __posY=(160, 200,240,280) #posicion de los corredores en Y
    __names=("Speedy","Lucera","Alonso","Torcuato")
    __startLine=5
    __finishLine=620
    
    def __init__(self):
        self.__screen=pygame.display.set_mode((640,480))
        self.__background=pygame.image.load("images/background.png")
        pygame.display.set_caption("Carrera de bichos")
        
        for i in range(4):
            theRunner=Runner(self.__startLine,self.__posY[i]) #Creo una instancia de Runner para el primer corredor
            theRunner.name=self.__names[i] #le doy nombre a cada corredor
            self.runners.append(theRunner)
        
        #self.runners.append(Runner(self.__startLine, 240))
        
    
    def competir(self):
        gameOver=False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #para parar el juego si le damos al boton x de cerrar ventana
                    gameOver=True
                    
            for runner in self.runners:  #Aqui no creo el range(4) por si me dan mas corredores en el range de la class Game
                runner.avanza() #es runner sin self pq es el runner de dentro del for
                if runner.position[0] >= self.__finishLine: #si la posicione x del corredor es igual a la posicion de la linea final
                    print("{} ha ganado".format(runner.name)) #muestra el nombre del ganador
                    gameOver=True
                    break
            self.__screen.blit(self.__background,(0,0)) #el blit sirve para mostrar una imagen (el background) en una posicion (0,0) intermitentemente con muchos fps
            
            #esta es una forma de hacerlo si conocemos cuantos corredores hay
            """self.__screen.blit(self.runners[0].custome,self.runners[0].position)
            self.__screen.blit(self.runners[1].custome,self.runners[1].position)
            self.__screen.blit(self.runners[2].custome,self.runners[2].position)
            self.__screen.blit(self.runners[3].custome,self.runners[3].position)"""
            
            for runner in self.runners:
                 self.__screen.blit(runner.custome,runner.position)   
            
            pygame.display.flip()
            
        while True: #este while es para q cuando llegue el ganador, el programa espere a q le pulse la x para cerrar
            for event in pygame.event.get(): #crear eventos, es decir, q esta cogiendo cada movimiento q hacemos con el raton, teclado...
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
       
            
if __name__=='__main__':
    game=Game()
    pygame.font.init()
    game.competir()