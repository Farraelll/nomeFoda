import pygame, sys
from source.config import *

class Jogo:
    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
        self.relogio = pygame.time.Clock()
        pygame.display.set_caption("Super Renato Adventures")

    def iniciar(self):
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.tela.fill(COR_FUNDO)
    
            pygame.display.update()
            self.relogio.tick(FPS)

if __name__ == '__main__':
    Jogo().iniciar()