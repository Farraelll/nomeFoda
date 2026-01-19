import pygame as pg

pg.init()
janela = pg.display.set_mode((800,600))
pg.display.set_caption("Teste")
clock = pg.time.Clock()

crashed = False

while not crashed:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            crashed = True

    pg.display.flip()
    clock.tick(60)

pg.quit()