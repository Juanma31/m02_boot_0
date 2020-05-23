#utilizando la toeria del programa cicloPyGame.py
import pygame, sys

class Game():
    runners=[]
    __starlLine=20
    __finishLine=620
    
    def __init__(self):
        self.__screen=pygame.display.set_mode((640,480))
        self.__background=pygame.image.load("images/background.png")
        pygame.display.set_caption("Carrera de bichos")
    def competir(self):
        gameOver=False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver=True
            
            self.__screen.blit(self.__background,(0,0)) #el blit sirve para mostrar una imagen (el background) en una posicion (0,0) intermitentemente con muchos fps
            pygame.display.flip()
            
        pygame.quit()
        sys.exit()
            
if __name__=='__main__':
    game=Game()
    pygame.font.init()
    game.competir()