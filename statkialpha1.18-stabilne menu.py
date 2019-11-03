import pygame
import sys
import random

pygame.init()  # musi być
pygame.display.set_caption('Statki')
a = pygame.image.load('Grafa/Logo.png')
pygame.display.set_icon(a)

#moduł ze zmiennymi
wysokoscOkna=720
szerokoscOkna=1280
rozmiargracza_1=50
rozmiargracza_2=50
rozmiarOkna=(szerokoscOkna,wysokoscOkna)
obraz = pygame.display.set_mode(rozmiarOkna)
statek_1 = pygame.Rect(0, wysokoscOkna/2, rozmiargracza_1, rozmiargracza_1)
statek_2 = pygame.Rect(szerokoscOkna-rozmiargracza_2-40, (wysokoscOkna/2), rozmiargracza_2, rozmiargracza_2)
zyciegracza1=0
zyciegracza2=szerokoscOkna-200
timer_strzalu=0
timer_strzalu2=0
opcjemenu=0
zmiennabreak=0
pociskikolor=[]
my_missile_list=[]

killRed = 0
killBlue = 0
kolorNapisu = (255, 255, 0)
czcionka = pygame.font.SysFont("Comic Sans MS", 60)

background = pygame.image.load("Grafa/background.jpg").convert()
menu = pygame.image.load("Grafa/backgroundmenu.jpg").convert()
settings= pygame.image.load('Grafa/settings.jpg').convert()
przyciskback= pygame.image.load('Grafa/przyciskback.png')
przycisksettings=pygame.image.load('Grafa/przycisksettings.png')
przyciskstart=pygame.image.load('Grafa/przyciskstart.png')
przyciskexit=pygame.image.load('Grafa/przyciskexit.png')
pustemenu=pygame.image.load('Grafa/pustemenu.jpg')
tabela=pygame.image.load('Grafa/tabela.png')
statekGrafika_1 = pygame.image.load("Grafa/Statek1-Blue1.png")
statekGrafika_1_mask=pygame.mask.from_surface(statekGrafika_1)
statekGrafika_1_rect=statekGrafika_1.get_rect()
statekGrafika_2 = pygame.image.load("Grafa/Statek1-Red1.png")
statekGrafika_2_mask=pygame.mask.from_surface(statekGrafika_2)
pociskGrafika = pygame.image.load('Grafa/pocisk.png').convert_alpha()
pociskikolor.append(pygame.image.load('Grafa/pocisk.png'))
pociskikolor.append(pygame.image.load('Grafa/pocisk2.png'))
pociskikolor.append(pygame.image.load('Grafa/pocisk3.png'))


pociskGrafika_mask=pygame.mask.from_surface(pociskGrafika)
life = pygame.image.load('Grafa/life.png')
music = pygame.mixer.music.load("Dźwięki/pif.mp3")




#moduł resetowania pozycji
def granicePlanszyX(pozycja):
    if pozycja >= szerokoscOkna:
        pozycja = 0
    if pozycja < 0:
        pozycja = szerokoscOkna
    return pozycja
def granicePlanszyY(pozycja):
    if pozycja >= wysokoscOkna:
        pozycja = 0
    if pozycja < 0:
        pozycja = wysokoscOkna
    return pozycja

#moduł poruszania sie
def ruchxAD():
    if pygame.key.get_pressed()[pygame.K_a]:
        return -1
    elif pygame.key.get_pressed()[pygame.K_d]:
        return 1
    else:
        return 0
def ruchyWS():
    if pygame.key.get_pressed()[pygame.K_w]:
        return -1
    elif pygame.key.get_pressed()[pygame.K_s]:
        return 1
    else:
        return 0
def ruchxLR():
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        return -1
    elif pygame.key.get_pressed()[pygame.K_RIGHT]:
        return 1
    else:
        return 0
def ruchyUD():
    if pygame.key.get_pressed()[pygame.K_UP]:
        return -1
    elif pygame.key.get_pressed()[pygame.K_DOWN]:
        return 1
    else:
        return 0

def off():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

##Moduł funkcji od strzelania

class gracz(pygame.sprite.Sprite):
    def __init__(self,x,y,vx,vy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pociskGrafika
        self.rect = pociskGrafika.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
    def missile(self):
        self.x += self.vx
        self.y += self.vy
        obraz.blit(self.image, [self.x, self.y])

#NAJWAZNIEJSZA KLASA TUTAJ NIC NIE RUSZAC!!!
class Projectile():
    def __init__(self,x,y,vx,vy,rozrzut):
        self.x = x
        self.kolizja1 = 0
        self.kolizja2 = 0
        self.y = y
        self.rozrzut=rozrzut
        self.vx = vx
        self.vy = vy +(rozrzut/150)
        #self.image = pociskGrafika
        self.image = pociskikolor[rand]
        self.rect = self.image.get_rect()
        self.istnieje=1
    def missile(self):
        if (self.istnieje==1):
            self.x += self.vx
            self.y += self.vy
            obraz.blit(self.image, [self.x, self.y])
    def siongracz1(self):
        if (self.istnieje == 1):
            if statek_1.x<(self.x+12)<(statek_1.x+rozmiargracza_1+17) and statek_1.y<(self.y)<(statek_1.y+rozmiargracza_1) and self.vx<0:
                self.kolizja1=1
    def siongracz2(self):
        if (self.istnieje == 1):
            if statek_2.x+30<(self.x)<(statek_2.x++rozmiargracza_2) and statek_2.y<(self.y)<(statek_2.y+rozmiargracza_2)and self.vx>0:
                self.kolizja2=1
    def outofmap(self):
        if self.x>szerokoscOkna or self.x<0:
            self.y = 2*wysokoscOkna+20
            self.istnieje=0
        if self.y>wysokoscOkna or self.y<0:
            self.y = 2*wysokoscOkna+20
            self.istnieje=0

def wynikNapis(killRed, killBlue):#funckja od wyswietlania wyniku
    killRed = str(killRed)
    killBlue = str(killBlue)
    napis = killRed + " : " + killBlue
    label = czcionka.render(napis, 1, kolorNapisu)
    obraz.blit(label, (szerokoscOkna / 2 - 60, 10))



################Pętla programu całego#######################
while True:
    #########################################################################################################
    # MENU GLOWNE
    if opcjemenu ==0:
        while True:
            obraz.blit(menu, [0, 0])
            obraz.blit(przyciskstart, [0, 0])
            obraz.blit(przycisksettings, [0, 40])
            obraz.blit(przyciskexit,[szerokoscOkna-220,wysokoscOkna-36])
            mouse = pygame.mouse.get_pos()
            obraz.blit(pociskGrafika, [mouse[0], mouse[1]])
            click = pygame.mouse.get_pressed()
            pociskGrafika_rect = pociskGrafika.get_rect()
            przyciskstart_rect = przyciskstart.get_rect()
            if pygame.Rect.collidepoint(przyciskstart_rect, mouse[0], mouse[1]):
                if click[0]:
                    opcjemenu = 1
                    break
            if 0<mouse[0]<220 and 40<mouse[1]<76:
                if click[0]:
                    opcjemenu = 2
                    break
            if 0<mouse[0]<220 and 80<mouse[1]<116:
                if click[0]:
                    opcjemenu = 3
                    break
            if szerokoscOkna-220 < mouse[0] < szerokoscOkna and wysokoscOkna-36 < mouse[1] < wysokoscOkna:
                if click[0]:
                    sys.exit(0)

            pygame.display.flip()
            off()

    #########################################################################################################
    #menu ustawienia
    if opcjemenu == 2:
        while True:
            obraz.blit(settings, [0, 0])
            obraz.blit(przyciskback,[szerokoscOkna-220,wysokoscOkna-36])
            mouse = pygame.mouse.get_pos()
            obraz.blit(pociskGrafika, [mouse[0], mouse[1]])
            click = pygame.mouse.get_pressed()


            #tutaj idzie kod do pustego menu
            #tutaj idzie kod do pustego menu
            #tutaj idzie kod do pustego menu
            #tutaj idzie kod do pustego menu


            if szerokoscOkna-220 < mouse[0] < szerokoscOkna and wysokoscOkna-36 < mouse[1] < wysokoscOkna:
                if click[0]:
                    opcjemenu=0
                    break
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                opcjemenu=0
                break
            pygame.display.flip()
            off()

    #########################################################################################################
    #puste menu
    if opcjemenu == 3:
        while True:
            obraz.blit(pustemenu, [0, 0])
            obraz.blit(przyciskback,[szerokoscOkna-220,wysokoscOkna-36])
            mouse = pygame.mouse.get_pos()
            obraz.blit(pociskGrafika, [mouse[0], mouse[1]])
            click = pygame.mouse.get_pressed()


            #tutaj idzie kod do pustego menu
            #tutaj idzie kod do pustego menu
            #tutaj idzie kod do pustego menu
            #tutaj idzie kod do pustego menu


            if szerokoscOkna-220 < mouse[0] < szerokoscOkna and wysokoscOkna-36 < mouse[1] < wysokoscOkna:
                if click[0]:
                    opcjemenu=0
                    break
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                opcjemenu=0
                break
            pygame.display.flip()
            off()




    ##########################################################################################################
    ##########################################################################################################
    #BODY GRY Głównej CALE!!!
    if opcjemenu == 1:
        while True:
            obraz.blit(background, [0, 0])
            #timer strzalu gracza 1
            if timer_strzalu >0:
                timer_strzalu -=1

            #timer strzalu gracza2
            if timer_strzalu2 > 0:
                timer_strzalu2 -= 1


            rozrzut = random.randint(-20, 20)#róra randomizacja rorzuty góra dół
            rand = random.randint(1, 1)#randomizacja koloru pocisków


            # poruszanie sie
            statek_1.x += ruchxAD()
            statek_1.y += ruchyWS()
            statek_2.x += ruchxLR()
            statek_2.y += ruchyUD()

            # teleportacja na granicach mapy na przeciwną stronę
            statek_1.x = granicePlanszyX(statek_1.x)
            statek_1.y = granicePlanszyY(statek_1.y)
            statek_2.x = granicePlanszyX(statek_2.x)
            statek_2.y = granicePlanszyY(statek_2.y)

            #moduł pod pozycje skąd mają wystrzelić pociski
            shotplayer1x = statek_1.x + rozmiargracza_1
            shotplayer1y = statek_1.y + rozmiargracza_1 / 2
            shotplayer2x = statek_2.x + rozmiargracza_2 / 2
            shotplayer2y = statek_2.y + rozmiargracza_2 / 2

            #sprawdzanie zderzenia statków
            offset=(statek_1.x-statek_2.x,statek_1.y-statek_2.y)
            kolizja=statekGrafika_1_mask.overlap(statekGrafika_2_mask, offset)
            if kolizja:#<-------------co sie dzieje kiedy sie zderzą
                zyciegracza1-=1
                zyciegracza2+=1

            obraz.blit(tabela,[szerokoscOkna/2-100, 10])
            wynikNapis(killRed,killBlue)#wywołanie wyniku

            obraz.blit(statekGrafika_1, [statek_1.x, statek_1.y])#to tutaj sa nasze statki, pamiętaj
            obraz.blit(statekGrafika_2, [statek_2.x, statek_2.y])#to tutaj sa nasze statki, pamiętaj

            #Updatuje wszystkie pociski z clasy Projectile
            for b in my_missile_list:
                b.missile()
                b.siongracz1()
                if b.kolizja1==1:
                    zyciegracza1-=5
                    b.kolizja1=0
                    b.istnieje=0
                    #killRed += 1 #<-------------Odplala licznik kolizji
                b.siongracz2()
                if b.kolizja2 == 1:
                    zyciegracza2 += 5
                    b.kolizja2 = 0
                    b.istnieje=0
                    #killBlue += 1#<-------------Odplala licznik kolizji
                b.outofmap()
                if b.istnieje==0:
                    my_missile_list.remove(b)

            #zycie i co sie dzieje po smierci
            if zyciegracza1 <= -200:
                zyciegracza1 = 0
                killRed += 1
                statek_1 = pygame.Rect(0, 100, rozmiargracza_1, rozmiargracza_1)

            if zyciegracza2 >= szerokoscOkna:
                zyciegracza2 = szerokoscOkna - 200
                killBlue += 1
                statek_2 = pygame.Rect(szerokoscOkna - rozmiargracza_2 - 40, (wysokoscOkna - 100), rozmiargracza_2, rozmiargracza_2)

        #moduł wystrzeliwania pocisków, dźwięki, trajektorie ilości etc.
            #gracz 1
            if pygame.key.get_pressed()[pygame.K_f] and timer_strzalu < 2:
                my_missile_list.append(Projectile(shotplayer1x, shotplayer1y, 2.7, 0, rozrzut+(75*ruchyWS())))
                pygame.mixer.music.play(0)
                pygame.mixer.music.play(1)
                timer_strzalu += 0
            #gracz 2)
            if pygame.key.get_pressed()[pygame.K_p] and timer_strzalu2 < 2:
                rand = random.randint(0,0)
                my_missile_list.append(Projectile(shotplayer2x, shotplayer2y - 6, -2.6, 0, rozrzut+(75*ruchyUD())))
                my_missile_list.append(Projectile(shotplayer2x, shotplayer2y - 16, -2.54, 0, rozrzut-0.2+(75*ruchyUD())))
                my_missile_list.append(Projectile(shotplayer2x, shotplayer2y + 13, -2.6, 0, rozrzut+(75*ruchyUD())))
                my_missile_list.append(Projectile(shotplayer2x, shotplayer2y + 23, -2.54, 0, rozrzut+0.2+(75*ruchyUD())))
                pygame.mixer.music.play(0)
                pygame.mixer.music.play(1)
                timer_strzalu2 += 20

            obraz.blit(life, [zyciegracza1, 0])
            obraz.blit(life, [zyciegracza2, 0])
            pygame.display.flip()
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:#<------------Powrót do menu
                opcjemenu=0
                break
            off()