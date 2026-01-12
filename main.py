import random
import pygame
import pygame_emojis

pygame.init()

################================---------------- INICJALIZACJA STAŁYCH I ZMIENNYCH ----------------================################
font = pygame.font.Font(size = 60)
font2 = pygame.font.Font(size = 150)
font3 = pygame.font.Font(size = 40)
emoji_size = (40,40)
fire_emoji = pygame_emojis.load_emoji('🔥',emoji_size)

#utawienie trybu gry
tryb_gry = "lobby"  # lobby, game, score, end
wylacz_gre = False

# Ustawiania wielkości okna
SZEROKOSC = 1200
WYSOKOSC = 550
screen = pygame.display.set_mode((SZEROKOSC,WYSOKOSC))

# Ustawienia paletek
DLUGOSC_PALETKI = 90
SZEROKOSC_PALETKI = 20
DYSTANS_PALETKI_OD_SCIANY = 25
paletka_prawa_y = (WYSOKOSC / 2) - (DLUGOSC_PALETKI / 2)
paletka_lewa_y = (WYSOKOSC / 2) - (DLUGOSC_PALETKI / 2)

# Ustawienia linii środkowej
GRUBOSC_LINII = 20
linia = pygame.rect.Rect((SZEROKOSC / 2) - (GRUBOSC_LINII / 2), 0, GRUBOSC_LINII, WYSOKOSC)

# Ustawienia piłeczki
ROZMIAR_PILECZKI = 20
polozenie_pileczki_y = (WYSOKOSC / 2) - (ROZMIAR_PILECZKI / 2)  # Na jakiej wyskości piłeczka się znajduje
polozenie_pileczki_x = (SZEROKOSC / 2) - (ROZMIAR_PILECZKI / 2)  # Jak daleko od ściany piłeczka się znajduje

tryb_spacja = False

# Ustawienia poziomu trudności (szybkość piłeczki i ilość HP)
"""
Żeby można było wybrać poziom trudności klikając w ekranie lobby, musimy przenieść ten kod do nowej funkcji
"""
#M&M no i ziemniak



predkosc_x = 1
predkosc_y = 1


"""Aż dotąd"""

# Ustawienia graczy
nazwa_gracza_lewo = "Player 1"
nazwa_gracza_prawo = "Player 2"
# nazwa_gracza_lewo = input("user name from left side")
# nazwa_gracza_prawo = input("user name from right side")
points_left = 0
points_right = 0

n_player1 = ''
n_player2 = ''

p1_name_set = False
p2_name_set = False

szerokosc_przycisku = 200
wyskosc_przycisku = 80
odstepy_miedzy_przyciskami = 30
odstep_przycisku_od_sciany = 155

replay = False


################================---------------- EKRANY GRY ----------------================################

# Ekran lobby
przycisk_game = pygame.rect.Rect(
    SZEROKOSC - odstep_przycisku_od_sciany - szerokosc_przycisku,
    300,
    szerokosc_przycisku,
    wyskosc_przycisku)

przycisk_esc = pygame.rect.Rect(
    SZEROKOSC - odstepy_miedzy_przyciskami - odstep_przycisku_od_sciany - szerokosc_przycisku * 2,
    300,
    szerokosc_przycisku,
    wyskosc_przycisku)

przycisk_CDL = pygame.rect.Rect(
    SZEROKOSC - odstepy_miedzy_przyciskami * 2 - odstep_przycisku_od_sciany - szerokosc_przycisku * 3,
    300,
    szerokosc_przycisku,
    wyskosc_przycisku)

przycisk_CAN = pygame.rect.Rect(
    odstep_przycisku_od_sciany,
    300,
    szerokosc_przycisku,
    wyskosc_przycisku)

przycisk_one = pygame.rect.Rect(
    odstep_przycisku_od_sciany,
    300,
    szerokosc_przycisku,
    wyskosc_przycisku)


przycisk_two = pygame.rect.Rect(
    SZEROKOSC - odstepy_miedzy_przyciskami * 2 - odstep_przycisku_od_sciany - szerokosc_przycisku * 3,
    300,
    szerokosc_przycisku,
    wyskosc_przycisku)

przycisk_three = pygame.rect.Rect(
    SZEROKOSC - odstepy_miedzy_przyciskami - odstep_przycisku_od_sciany - szerokosc_przycisku * 2,
    300,
    szerokosc_przycisku,
    wyskosc_przycisku)

przycisk_four = pygame.rect.Rect(
    SZEROKOSC - odstep_przycisku_od_sciany - szerokosc_przycisku,
    300,
    szerokosc_przycisku,
    wyskosc_przycisku)

przycisk_accept = pygame.rect.Rect(
    SZEROKOSC /2 - szerokosc_przycisku,
    500,
    szerokosc_przycisku,
    wyskosc_przycisku)

przycisk_replay = pygame.rect.Rect(
    SZEROKOSC /2 - szerokosc_przycisku /2,
    50,
    szerokosc_przycisku,
    wyskosc_przycisku)

def show_globby (screen:pygame.Surface, event_l):
    global tryb_gry, wylacz_gre

    screen.fill('black')
    globby_word_render = font2.render("Lobby", True, 'white')
    szerokosc_globby = globby_word_render.get_width()
    screen.blit(globby_word_render, ((SZEROKOSC - szerokosc_globby) / 2,100), )
    kolor_przyciskow = "white"

    pygame.draw.rect(screen, kolor_przyciskow, przycisk_CAN)
    can_word_render = font3.render("NAME", True, 'black')
    szerokosc_CAN = can_word_render.get_width()
    wysokosc_CAN = can_word_render.get_height()
    screen.blit(can_word_render,(przycisk_CAN.centerx - szerokosc_CAN / 2, przycisk_game.centery - wysokosc_CAN / 2), )

    pygame.draw.rect(screen, kolor_przyciskow, przycisk_game)
    game_word_render = font3.render("GAME", True, 'black')
    szerokosc_game = game_word_render.get_width()
    wysokosc_game = game_word_render.get_height()
    screen.blit(game_word_render, (przycisk_game.centerx - szerokosc_game /2, przycisk_game.centery - wysokosc_game/2), )

    pygame.draw.rect(screen, kolor_przyciskow, przycisk_esc)
    esc_word_render = font3.render("EXIT", True, 'black')
    szerokosc_esc = esc_word_render.get_width()
    wysokosc_esc = esc_word_render.get_height()
    screen.blit(esc_word_render,(przycisk_esc.centerx - szerokosc_esc / 2, przycisk_esc.centery - wysokosc_esc / 2), )

    pygame.draw.rect(screen, kolor_przyciskow, przycisk_CDL)
    cdl_word_render = font3.render("Difficulty".upper(), True, 'black')
    cdl_rect = cdl_word_render.get_rect(center=przycisk_CDL.center)
    screen.blit(cdl_word_render, cdl_rect, )

    for event in event_l:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            possition = pygame.mouse.get_pos()
            if przycisk_game.collidepoint(possition):
                tryb_gry = 'game'
                print('ziemniak')

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            possition = pygame.mouse.get_pos()
            if przycisk_esc.collidepoint(possition):
                wylacz_gre = True
                print('ziemniak')

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            possition = pygame.mouse.get_pos()
            if przycisk_CDL.collidepoint(possition):
               tryb_gry = "CDL"

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            possition = pygame.mouse.get_pos()
            if przycisk_CAN.collidepoint(possition):
                tryb_gry = 'name'
                print('ziemniak')

HP_left = 6
HP_right = 6
def choose_difficulti_level(screen, event_l):
    global predkosc_y,predkosc_x,HP_left,HP_right,tryb_gry

    screen.fill('black')
    cdl_word_render = font2.render("Choose difficulty level", True, 'white')
    szerokosc_cdl = cdl_word_render.get_width()
    screen.blit(cdl_word_render, ((SZEROKOSC - szerokosc_cdl) / 2, 100), )
    kolor_przyciskow = "white"

    pygame.draw.rect(screen, kolor_przyciskow, przycisk_one)
    one_word_render = font3.render("Easy", True, 'black')
    szerokosc_one = one_word_render.get_width()
    wysokosc_one = one_word_render.get_height()
    screen.blit(one_word_render, (przycisk_one.centerx - szerokosc_one / 2, przycisk_one.centery - wysokosc_one / 2), )

    pygame.draw.rect(screen, 'yellow', przycisk_two)
    two_word_render = font3.render("Medium", True, 'black')
    szerokosc_two = two_word_render.get_width()
    wysokosc_two = two_word_render.get_height()
    screen.blit(two_word_render, (przycisk_two.centerx - szerokosc_two / 2, przycisk_two.centery - wysokosc_two / 2), )

    pygame.draw.rect(screen, 'orange', przycisk_three)
    three_word_render = font3.render("Hard", True, 'black')
    szerokosc_three = three_word_render.get_width()
    wysokosc_three = three_word_render.get_height()
    screen.blit(three_word_render, (przycisk_three.centerx - szerokosc_three / 2, przycisk_three.centery - wysokosc_three / 2), )

    pygame.draw.rect(screen, "red", przycisk_four)
    four_word_render = font3.render("HELL", True, 'black')
    szerokosc_four = four_word_render.get_width()
    wysokosc_four = four_word_render.get_height()
    screen.blit(four_word_render, (przycisk_four.centerx - szerokosc_four / 2, przycisk_four.centery - wysokosc_four / 2), )
    screen.blit(fire_emoji, (przycisk_four.centerx - szerokosc_four / 2, przycisk_four.centery - wysokosc_four / 2), )

    # inicjowanie leveli
    predkosc_baza_x = random.choice([-1, 1])
    predkosc_baza_y = random.randint(-1, 1)



    for event in event_l:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            possition = pygame.mouse.get_pos()

            if przycisk_one.collidepoint(possition):
                predkosc_x = predkosc_baza_x * 4
                predkosc_y = predkosc_baza_y * 4
                tryb_gry = 'lobby'

            elif przycisk_two.collidepoint(possition):
                predkosc_x = predkosc_baza_x * 5
                predkosc_y = predkosc_baza_y * 5
                tryb_gry = 'lobby'

            elif przycisk_three.collidepoint(possition):
                predkosc_x = predkosc_baza_x * 6
                predkosc_y = predkosc_baza_y * 6
                tryb_gry = 'lobby'

            elif przycisk_four.collidepoint(possition):
                predkosc_x = predkosc_baza_x * 10
                predkosc_y = predkosc_baza_y * 10
                tryb_gry = 'lobby'

def name (screen, event_l):
    global tryb_gry, n_player1, n_player2
    global nazwa_gracza_lewo, nazwa_gracza_prawo
    global p1_name_set, p2_name_set

    name_word_render = font2.render("Chose a name", True, 'white')
    szerokosc_name = name_word_render.get_width()
    screen.blit(name_word_render, ((SZEROKOSC - szerokosc_name) / 2,100), )

    name_word_render_two = font3.render("click accept to write the second players name and to exit", True, 'white')
    szerokosc_name_two = name_word_render_two.get_width()
    screen.blit(name_word_render_two, ((SZEROKOSC - szerokosc_name_two) / 2, 200), )

    player_1 = font3.render("player1", True, 'white')
    szerokosc_1 = player_1.get_width()
    screen.blit(player_1, (310 + szerokosc_1 / 2, 380), )

    player_2 = font3.render("player2", True, 'white')
    szerokosc_2 = player_2.get_width()
    screen.blit(player_2, (680 + szerokosc_2 / 2, 380), )

    pygame.draw.line(screen, "white", (310, 350), (500, 350))
    pygame.draw.line(screen, "white", (680, 350), (880, 350))


    pygame.draw.rect(screen, 'white', przycisk_accept)
    accept_word_render = font3.render("Accept".upper(), True, 'black')
    accept_rect = accept_word_render.get_rect(center=przycisk_accept.center)
    screen.blit(accept_word_render, accept_rect, )

    for event in event_l:
        if p1_name_set == False:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                        n_player1 = n_player1[0:-1]
                else:
                    n_player1 += event.unicode
                    n_player1 = n_player1[0:10]

        elif p2_name_set == False:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE and p1_name_set == True:
                        n_player2 = n_player2[0:-1]
                else:
                    n_player2 += event.unicode
                    n_player2 = n_player2[0:10]


        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            possition = pygame.mouse.get_pos()
            if przycisk_accept.collidepoint(possition):
                if p1_name_set == False:
                    nazwa_gracza_lewo = n_player1
                    p1_name_set = True
                    print('gotowany ziemniak')
                else:
                    nazwa_gracza_prawo = n_player2
                    p2_name_set = True
                    tryb_gry = 'lobby'
    n_PLAYER_1 = font3.render(n_player1, True, 'white')
    szerokosc_n_p_1 = n_PLAYER_1.get_width()
    screen.blit(n_PLAYER_1, (310,325) )
    n_PLAYER_2 = font3.render(n_player2, True, 'white')
    szerokosc_n_p_2 = n_PLAYER_2.get_width()
    screen.blit(n_PLAYER_2, (680,325) )







# Ekran widoku gry
def game(screen, event_l):
    global paletka_lewa_y, paletka_prawa_y
    global polozenie_pileczki_x, polozenie_pileczki_y
    global points_left, points_right, HP_left, HP_right
    global predkosc_x, predkosc_y
    global replay
    global tryb_spacja




    pygame.draw.rect(screen, 'white', linia)

    paletka_lewa = pygame.rect.Rect(
        DYSTANS_PALETKI_OD_SCIANY,
        paletka_lewa_y,
        SZEROKOSC_PALETKI,
        DLUGOSC_PALETKI)
    paletka_prawa = pygame.rect.Rect(
        SZEROKOSC - (SZEROKOSC_PALETKI + DYSTANS_PALETKI_OD_SCIANY),
        paletka_prawa_y,
        SZEROKOSC_PALETKI,
        DLUGOSC_PALETKI)
    pygame.draw.rect(screen, 'white', paletka_lewa)
    pygame.draw.rect(screen, 'white', paletka_prawa)

    pileczka = pygame.rect.Rect(
        polozenie_pileczki_x,
        polozenie_pileczki_y,
        ROZMIAR_PILECZKI,
        ROZMIAR_PILECZKI)
    pygame.draw.rect(screen, 'red', pileczka)

    # przycisk replay
    for event in event_l:
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                tryb_spacja = not tryb_spacja


        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            possition = pygame.mouse.get_pos()
            if przycisk_replay.collidepoint(possition):
                replay = False
                if points_left >= 5:
                    HP_right -= 1
                elif points_right >= 5:
                    HP_left -= 1
                points_right = 0
                points_left = 0
                polozenie_pileczki_x = SZEROKOSC /2 - ROZMIAR_PILECZKI /2
                polozenie_pileczki_y = WYSOKOSC /2 - ROZMIAR_PILECZKI  /2



    if points_left >= 20 or points_right >= 20:
        replay = True

        pygame.draw.rect(screen, 'white', przycisk_replay)
        replay_word_render = font3.render("REPLAY", True, 'black')
        szerokosc_replay = replay_word_render.get_width()
        wysokosc_replay = replay_word_render.get_height()
        screen.blit(replay_word_render,
                    (przycisk_replay.centerx - szerokosc_replay / 2, przycisk_replay.centery - wysokosc_replay / 2), )



    # Wyświetlanie nicków i punktów
    gracz_lewo_name_render = font.render(f'{nazwa_gracza_lewo} Points: {points_left}', True, 'white')
    gracz_prawo_name_render = font.render(f'{nazwa_gracza_prawo} Points: {points_right}', True, 'white')
    szerokosc_nicku_gracza_prawo = gracz_prawo_name_render.get_width()
    screen.blit(gracz_lewo_name_render, (DYSTANS_PALETKI_OD_SCIANY, 10), )
    screen.blit(gracz_prawo_name_render, (SZEROKOSC - szerokosc_nicku_gracza_prawo - 10, 10), )

    # Wyświetlanie HP
    gracz_prawo_HP_render = font.render(f'HP:{HP_right}', True, 'white')
    szerokosc_HP_gracza_prawo = gracz_prawo_HP_render.get_width()
    gracz_lewo_HP_render = font.render(f'HP:{HP_left}', True, 'white')

    screen.blit(gracz_prawo_HP_render, (SZEROKOSC - szerokosc_HP_gracza_prawo - 10, 60), )
    screen.blit(gracz_lewo_HP_render, (DYSTANS_PALETKI_OD_SCIANY, 60), )

    if replay == True:
        return

#ziemniek

    if tryb_spacja == True:
        return
    #I'm a pancake and potato

    # Poruszanie paletkami
    klawa = pygame.key.get_pressed()
    if klawa[pygame.K_DOWN]:
        paletka_prawa_y += 8
        if paletka_prawa_y >= 550 - DLUGOSC_PALETKI:
            paletka_prawa_y = 550 - DLUGOSC_PALETKI
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
        if paletka_lewa_y >= 550 - DLUGOSC_PALETKI:
            paletka_lewa_y = 550 - DLUGOSC_PALETKI




    # Aktualizacja położenia piłeczki
    polozenie_pileczki_x += predkosc_x
    polozenie_pileczki_y += predkosc_y

    # Sprawdzanie kolizji piłeczki ze ścianami i paletkami
    if polozenie_pileczki_y >= WYSOKOSC - ROZMIAR_PILECZKI:
        predkosc_y = predkosc_y * -1
    elif polozenie_pileczki_y <= 0:
        predkosc_y = predkosc_y * -1

    if polozenie_pileczki_x >= SZEROKOSC - ROZMIAR_PILECZKI:
        predkosc_x = predkosc_x * -1
    elif polozenie_pileczki_x <= 0:
        predkosc_x = predkosc_x * -1

    # Kolizja piłeczki z lewą paletką
    if polozenie_pileczki_x >= DYSTANS_PALETKI_OD_SCIANY and \
            polozenie_pileczki_x <= DYSTANS_PALETKI_OD_SCIANY + SZEROKOSC_PALETKI and \
            polozenie_pileczki_y <= paletka_lewa_y + DLUGOSC_PALETKI and \
            polozenie_pileczki_y >= paletka_lewa_y:
        predkosc_x = predkosc_x * -1
        points_left += 1
        polozenie_pileczki_x = DYSTANS_PALETKI_OD_SCIANY + SZEROKOSC_PALETKI

    # Kolizja piłeczki z prawą paletką
    if polozenie_pileczki_x <= SZEROKOSC - DYSTANS_PALETKI_OD_SCIANY:  # Pileczka po lewo od prawej paletki
        if polozenie_pileczki_x + ROZMIAR_PILECZKI >= SZEROKOSC - DYSTANS_PALETKI_OD_SCIANY - SZEROKOSC_PALETKI:  # Prawa krawędź piłeczki i lewa krawędź paletki
            if polozenie_pileczki_y <= paletka_prawa_y + DLUGOSC_PALETKI:  # Czy piłeczka nie jest poniżej paletki
                if polozenie_pileczki_y + ROZMIAR_PILECZKI >= paletka_prawa_y:  # Czy piłeczka nie jest powyżej paletki
                    predkosc_x = predkosc_x * -1
                    points_right += 1
                    polozenie_pileczki_x =  SZEROKOSC - DYSTANS_PALETKI_OD_SCIANY - SZEROKOSC_PALETKI - ROZMIAR_PILECZKI




##################################################################################################################
################================---------------- GŁÓWNA PĘTLA GRY ----------------================################
##################################################################################################################



zegarek = pygame.time.Clock()
while wylacz_gre == False:
    zegarek.tick(60)
    screen.fill('black')


    event_l = list(pygame.event.get())

    # Obsługa eventów
    for event in event_l:
        if event.type == pygame.QUIT:
            wylacz_gre = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                tryb_gry = "lobby"

    if tryb_gry == "game":
        game(screen,event_l)
    elif tryb_gry == 'lobby':
        show_globby(screen, event_l)
    elif tryb_gry == 'CDL':
        choose_difficulti_level(screen, event_l)
    elif tryb_gry == 'name':
        name(screen, event_l)

    pygame.display.update()

