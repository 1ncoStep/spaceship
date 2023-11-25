import pygame as pg
import random


win_size = (1600, 900)
screen = pg.display.set_mode(win_size)
fps = 1
clock = pg.time.Clock()


# def auto_pilot(starship_rect, direction):
#     screen.fill(pg.Color('grey'))
#
#     if direction == 'right':
#         pg.draw.rect(screen, 'blue', starship_rect)
#         starship_rect.x += 1
#         pg.display.flip()
#         clock.tick(fps)
#
#     if direction == 'left':
#         pg.draw.rect(screen, 'blue', starship_rect)
#         starship_rect.x -= 1
#         pg.display.flip()
#         clock.tick(fps)
#
#     if direction == 'up':
#         pg.draw.rect(screen, 'blue', starship_rect)
#         starship_rect.y += 1
#         pg.display.flip()
#         clock.tick(fps)
#
#     if direction == 'down':
#         pg.draw.rect(screen, 'blue', starship_rect)
#         starship_rect.y -= 1
#         pg.display.flip()
#         clock.tick(fps)
#
#
# rect = pg.Rect((0, 0), (50, 50))
# rect.center = (win_size[0] / 2, win_size[1] / 2)
# rect.size = (50, 50)
#
# auto_pilot(rect, 'left')


def laser_shoot(event):
    user_shot = pg.Rect((win_size[0] / 2 - 10, win_size[1] / 2 - 10), (20, 20))

    for event in pg.event.get():
        if event == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                user_shot.center == event.pos

    pg.draw.rect(screen, 'red', user_shot)



print(laser_shoot(1))
pg.display.flip()
clock.tick(fps)




