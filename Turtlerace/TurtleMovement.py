import pygame, sys
from pygame.locals import * #importar todos los botones K_UP,K_DOWN...
import random


class Runner():
    __customes = ('turtle','fish','prawn','moray','octopus')
    
    def __init__(self,x=0,y=0): #crear el corredor en la coordenada 0,0 con disfraz (por defecto es tortuga)
        
        ixCustome =random.randint(0,4) #genera un numero random
        
        self.custome = pygame.image.load("images/{}.png".format(self.__customes[ixCustome])) #obtiene un disfraz random 
        self.position = [x,y]
        self.name = "" #para cuando gane que se muestre el nombre del ganador
        
class Game():
    def __init__(self):
        self.__screen=pygame.display.set_mode((640,480))
        self.__background=pygame.image.load("images/background.png")
        pygame.display.set_caption("Carrera de bichos")
        
        self.runner=Runner(320,240)
    def start(self):
        gameOver=False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #para parar el juego si le damos al boton x de cerrar ventana
                    pygame.quit()
                    sys.exit()
                #https://www.pygame.org/docs/ref/key.html
                elif event.type==KEYDOWN: #si se ha pulsado una tecla
                    if  event.key == K_UP: #si pulso el boton flecha arriba
                        """
                        runnerY=self.runner.position[1] #posicion de Y
                        runnerY+=5 #aumento la posicion Y 
                        self.runner.position[1]=runnerY #le asigno la nueva posicion aumentada a la posicion actual
                        """
                        self.runner.position[1]-=10 #el equivalente al comentario anterior
                        
                    elif event.key == K_DOWN:#si pulso el boton flecha abajo
                        self.runner.position[1]+=10
                    elif event.key == K_LEFT:#si pulso el boton flecha izquierda
                        self.runner.position[0]-=10
                    elif event.key == K_RIGHT:#si pulso el boton flecha derecha
                        self.runner.position[0]+=10
                    else:
                        pass
                        
            self.__screen.blit(self.__background,(0,0)) #el blit sirve para mostrar una imagen (el background) en una posicion (0,0) intermitentemente con muchos fps
            self.__screen.blit(self.runner.custome, self.runner.position)
            
            pygame.display.flip()
            
if __name__=='__main__':
    game=Game()
    pygame.font.init()
    game.start()