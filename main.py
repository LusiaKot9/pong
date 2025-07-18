import pygame
import random as r
pygame.init()

szerokosc = 1200
wysokosc = 550
screen = pygame.display.set_mode((szerokosc,wysokosc))
dlugosc_paletki = 90
grubosc_lini = 20
paletka_x = 25
szerokosc_paletki = 20
paletka_prawa_y = wysokosc/2-dlugosc_paletki/2
paletka_lewa_y = wysokosc / 2 - dlugosc_paletki / 2
rozmiar_pileczki = 20
polozenie_pileczki_y = wysokosc / 2 - rozmiar_pileczki / 2
polozenie_pileczki_x = szerokosc / 2 - rozmiar_pileczki / 2

zegarek = pygame.time.Clock()

pileczka_r = r.randint(1, 4)
if pileczka_r == 1 :
    polozenie_pileczki_x -= 8
elif pileczka_r == 2 :
    polozenie_pileczki_x += 8
elif pileczka_r == 3 :
    polozenie_pileczki_y -= 8
elif pileczka_r == 4 :
    polozenie_pileczki_y += 8

while True:
    zegarek.tick(60)
    screen.fill('black')

    #rysowanie obiektów na planszy
    linia = pygame.rect.Rect(szerokosc/2-grubosc_lini/2,0,grubosc_lini,wysokosc)
    pygame.draw.rect(screen,'white', linia)
    paletka_lewa = pygame.rect.Rect(
        paletka_x,
        paletka_lewa_y,
        szerokosc_paletki,
        dlugosc_paletki)
    pygame.draw.rect(screen,'white', paletka_lewa)
    paletka_prawa = pygame.rect.Rect(
        szerokosc-(szerokosc_paletki + paletka_x),
        paletka_prawa_y,
        20,
        dlugosc_paletki)
    pygame.draw.rect(screen,'white', paletka_prawa)
    pileczka = pygame.rect.Rect(
        polozenie_pileczki_x,
        polozenie_pileczki_y,
        rozmiar_pileczki,
        rozmiar_pileczki)
    pygame.draw.rect(screen, 'red', pileczka)

    #obsługa eventów
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    klawa = pygame.key.get_pressed()
    if klawa[pygame.K_DOWN]:
        paletka_prawa_y += 8
        if paletka_prawa_y >= 550 - dlugosc_paletki:
            paletka_prawa_y = 550 - dlugosc_paletki
    if klawa[pygame.K_UP]:
        paletka_prawa_y -= 8
        if paletka_prawa_y <= 0:
            paletka_prawa_y = 0

    if klawa[pygame.K_w]:
        paletka_lewa_y -= 8
        if paletka_lewa_y <= 0:
            paletka_lewa_y = 0
    if klawa[pygame.K_s]:
        paletka_lewa_y += 8
        if paletka_lewa_y >= 550 - dlugosc_paletki:
            paletka_lewa_y = 550 - dlugosc_paletki






















    pygame.display.update()












