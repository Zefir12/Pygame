import pygame
import sys

pygame.init() #musi być
wielkoscOkna = (900,900)
obraz = pygame.display.set_mode(wielkoscOkna)
statek_1 = pygame.Rect(50,450,50,50)
statek_2 = pygame.Rect(800,450,50,50)
pocisk_1 = pygame.Rect(901,50,10,10)
pocisk_2 = pygame.Rect(50,901,10,10)
x = 10
while True:
    strzał_1 = 0
    strzał_2 = 0
    obraz.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_f:
            strzał_1 = 1
            pocisk_1.x = statek_1.x + 20
            pocisk_1.y = statek_1.y + 20
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            strzał_2 = 2
            pocisk_2.x = statek_2.x + 20
            pocisk_2.y = statek_2.y + 20
    if strzał_1 == 1 or pocisk_1.x < 900:
        pygame.draw.rect(obraz, (255, 0, 0), pocisk_1)
        pocisk_1.x += 1
    if strzał_2 == 2 or pocisk_2.x < 900:
        pygame.draw.rect(obraz, (0, 0, 255), pocisk_2)
        pocisk_2.x -= 1
    if (statek_1.x + 50 > pocisk_2.x and statek_1.x < pocisk_2.x)and\
            (statek_1.y + 50 > pocisk_2.y and statek_1.y < pocisk_2.y):
        statek_1.x = 0
        statek_1.y = 0
    if (statek_2.x + 50 > pocisk_1.x and statek_2.x < pocisk_1.x)and\
            (statek_2.y + 50 > pocisk_1.y and statek_2.y < pocisk_1.y):
        statek_2.x = 850
        statek_2.y = 0
    #sprawdzanie czy klawisz jest trzymany
    if pygame.key.get_pressed()[pygame.K_w]:
        statek_1.y -= 1

    if pygame.key.get_pressed()[pygame.K_s]:
        statek_1.y += 1

    if pygame.key.get_pressed()[pygame.K_a]:
        statek_1.x -= 1

    if pygame.key.get_pressed()[pygame.K_d]:
        statek_1.x += 1

    if pygame.key.get_pressed()[pygame.K_UP]:
        statek_2.y -= 1

    if pygame.key.get_pressed()[pygame.K_DOWN]:
        statek_2.y += 1

    if pygame.key.get_pressed()[pygame.K_LEFT]:
        statek_2.x -= 1

    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        statek_2.x += 1

    #if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
       # statek_1 = pygame.Rect(450,450,50,50)

   # if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
    #    statek_1 = pygame.Rect(450,450,50,50)

    #if pygame.key.get_pressed()[pygame.K_k]:
     #   x += 1

      #  statek_1 = pygame.Rect(statek_1.x,statek_1.y,x,x)

    #if pygame.key.get_pressed()[pygame.K_l]:
     #   if x > 0:
      #      x -= 1
       # statek_1 = pygame.Rect(statek_1.x,statek_1.y,x,x)
    if statek_1.x >= 900:
        statek_1.x = 0

    if statek_1.y >= 900:
        statek_1.y = 0

    if statek_1.x < 0:
            statek_1.x = 900

    if statek_1.y < 0:
            statek_1.y = 900

    if statek_2.x >= 900:
        statek_2.x = 0

    if statek_2.y >= 900:
        statek_2.y = 0

    if statek_2.x < 0:
        statek_2.x = 900

    if statek_2.y < 0:
        statek_2.y = 900

    #pocisk_1.x += 1
    #rysunek

    pygame.draw.rect(obraz, (255, 0, 0), statek_1)
    pygame.draw.rect(obraz, (0, 0, 255), statek_2)
    pygame.display.flip()