import pygame as pg


pg.mixer.init()

size = (500, 500)
screen = pg.display.set_mode(size)

fps = 100
clock = pg.time.Clock()

background = pg.image.load("background.png")
background = pg.transform.scale(background, size)

while True:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()

    screen.blit(background, (0, 0))

    pg.display.flip()
    clock.tick(fps)
