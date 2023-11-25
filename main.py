import pygame as pg
from characters import Spaceship, TestObjects
pg.mixer.init()


win_size = (750, 1000)
screen = pg.display.set_mode(win_size)

fps = 100
clock = pg.time.Clock()

background = pg.image.load('background.png')
background = pg.transform.scale(background, win_size)

character = Spaceship()

star = pg.sprite.Group()
star.add(TestObjects())
star.add(TestObjects())
star.add(TestObjects())
star.add(TestObjects())
star.add(TestObjects())

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()

    character.update()
    # character.resize()
    print(f'Координаты корабля: {character.show_coords()}.')
    star.update()

    screen.blit(background, (0, 0))
    screen.blit(character.image, character.rect)
    star.draw(screen)

    pg.display.flip()
    clock.tick(fps)


