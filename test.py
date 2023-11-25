# Круг, жёлтый, в точке 400 400, радиус 300
#
# Круг, оранжевый, в точке 500 150, радиус 20
#
# Круг, оранжевый, в точке 600 340, радиус 60
#
# Круг, оранжевый, в точке 200 500, радиус 60
#
# Круг, оранжевый, в точке 400 370, радиус 20
#
# Круг, оранжевый, в точке 300 200, радиус 50

# Круг, оранжевый, в точке 500 640, радиус 20


# import pygame as pg
#
#
# win_size = (1600, 900)
# screen = pg.display.set_mode(win_size)

# rect = pg.Rect((0, 0), (50, 50))
# rect.center = (win_size[0] / 2, win_size[1] / 2)
# rect.size = (200, 200)
#
# left_eye = pg.Rect((win_size[0] / 2, win_size[1] / 2), (30, 30))
# right_eye = pg.Rect((win_size[0] / 2 + rect.top / 4, win_size[1] / 2), (30, 30))
#
# fps = 60
# clock = pg.time.Clock()
#
# direct = 'right'
#
# while True:
#     if rect.left == 0:
#         direct = 'right'
#
#     if rect.right == win_size[0]:
#         direct = 'left'
#
#     if direct == 'right':
#         rect.x += 1
#         left_eye.x += 1
#         right_eye.x += 1
#
#     if direct == 'left':
#         rect.x -= 1
#         left_eye.x -= 1
#         right_eye.x -= 1
#
#     screen.fill(pg.Color('grey'))
#
#     pg.draw.rect(screen, 'red', rect)
#     pg.draw.rect(screen, 'white', left_eye)
#     pg.draw.rect(screen, 'white', right_eye)
#
#     pg.display.flip()
#     clock.tick(fps)


# #
# win_size = (500, 500)
# screen = pg.display.set_mode(win_size)


#
# def draw_signals():
#     pg.draw.circle(screen, 'yellow', (400, 400), 300)
#     pg.draw.circle(screen, 'orange', (500, 150), 20)
#     pg.draw.circle(screen, 'orange', (600, 340), 60)
#     pg.draw.circle(screen, 'orange', (200, 500), 60)
#     pg.draw.circle(screen, 'orange', (400, 370), 20)
#     pg.draw.circle(screen, 'orange', (300, 200), 50)
#     pg.draw.circle(screen, 'orange', (500, 640), 20)
#
#
# while True:
#     draw_signals()
#     pg.display.flip()


import pygame as pg
pg.mixer.init()


win_size = (1600, 900)
screen = pg.display.set_mode(win_size)

clock = pg.time.Clock()
fps = 1

test_ship = pg.image.load('Spaceship-PNG-File.png')
test_ship = pg.transform.scale(test_ship, (300, 300))

test_ship_rect = test_ship.get_rect(center=(win_size[0] / 2, win_size[1] / 2))

# pg.mixer.music.load('Музыка для игры на pygame.mp3')
# pg.mixer.music.set_volume(0.05)
#
# pg.mixer.music.play()
#
# pg.mixer.music.load('04410.mp3')
# pg.mixer.music.play()
rect = pg.Rect((0, 0), (50, 50))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()

        keys = pg.key.get_pressed()

        if keys[pg.K_w]:
            test_ship_rect.y += 10

        if keys[pg.K_s]:
            test_ship_rect.y -= 10

        if keys[pg.K_a]:
            test_ship_rect.x += 10

        if keys[pg.K_d]:
            test_ship_rect.x -= 10

        if event == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                print(event.pos)
                rect.center = event.pos

    screen.blit(test_ship, test_ship_rect)

    pg.display.flip()
    clock.tick(fps)

# if event.type == pg.KEYDOWN:
#     if event.type == pg.K_w:
#         test_ship_rect.y += 10
#
#     if event.type == pg.K_s:
#         test_ship_rect.y -= 10
#
#     if event.type == pg.K_d:
#         test_ship_rect.x += 10
#
#     if event.type == pg.K_a:
#         test_ship_rect.x -= 10
#
# if event == pg.MOUSEBUTTONDOWN:
#     if event.button == 1:
#         print(event.pos)
#         rect.center = event.pos


# Глав