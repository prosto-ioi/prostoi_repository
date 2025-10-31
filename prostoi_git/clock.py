import pygame, datetime

pygame.init()

screen = pygame.display.set_mode((900 , 900))

pygame.display.set_caption("clock,  clock, clock")

clock = pygame.image.load("base_micky.png")
secundy = pygame.image.load("second.png")
minyty = pygame.image.load("minute.png")
center = (450 , 450)

clock = pygame.transform.scale(clock , (800 , 600))
secundy = pygame.transform.scale(secundy , ( 60, 500))
minyty = pygame.transform.scale(minyty , (600 , 600))

def peremeshenie(kartina, ygl, center):
    kry = pygame.transform.rotate(kartina, ygl)
    pryamoygol = kry.get_rect(center = center)
    return kry,  pryamoygol

go = True

clock_tick = pygame.time.Clock()

while go:
    for vremya in pygame.event.get():
        if vremya.type == pygame.QUIT:
            go = False

    screen.fill("white")
    seychas = datetime.datetime.now()
    sec = seychas.second + seychas.microsecond/ 1000000
    min = seychas.minute + sec / 60
    sec_ygl = sec*6
    min_ygl = min*6

    sec_anime, sec_r_anime = peremeshenie(secundy,-sec_ygl, center)
    min_anime, min_r_anime = peremeshenie(minyty,-min_ygl, center)

    screen.blit(clock, clock.get_rect(center=center))
    screen.blit(min_anime, min_r_anime)
    screen.blit(sec_anime, sec_r_anime)

    pygame.display.update()
    clock_tick.tick(99)

pygame.quit()




    
