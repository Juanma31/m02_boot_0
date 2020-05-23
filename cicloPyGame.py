import pygame, sys

width = 640
height= 480

screen=pygame.display.set_mode((width,height)) #medidas de la pantalla
screen.fill((255,0,0)) #color rojo 255,0,0
pygame.display.set_caption("Ciclo basico de pygame") #muestra titulo

pygame.font.init() #el font es para los sistemas mas antiguos, con el imit solo ya vale

gameOver =False #variable que termina el juego
while not gameOver:
    for event in pygame.event.get(): #crear eventos, es decir, q esta cogiendo cada movimiento q hacemos con el raton, teclado...
        if event.type == pygame.QUIT: # Si le damos al boton x de cerrar ventana
            gameOver=True
    pygame.display.flip() #refresca la pantalla

pygame.quit() #para cerrar el juego
sys.exit() #con esto tarda menos en cerrar, pq cierra el sistema python del tiron
        