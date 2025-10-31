import pygame
import time

pygame.init()

screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("play list")

music_list = ["Filatov & Karas - Иногда.mp3","TASSO - Таю.mp3","Маракеш & 3-ий Январь - Милая.mp3","Пабло & Mr Lambo - Love Is.mp"]

i = 0
running = True
playing = True

pygame.mixer.music.load(music_list[i])
pygame.mixer.music.play()


a = time.time()
def zaderzhka():
    global a
    if time.time() - a > 0.5:
        a = time.time()
        return True
    return False


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and zaderzhka():
        if playing:
            pygame.mixer.music.pause()
            playing = False
        else:
            pygame.mixer.music.unpause()
            playing = True

    if keys[pygame.K_LEFT] and zaderzhka():
        i = (i - 1) % 4
        pygame.mixer.music.load(music_list[i])
        pygame.mixer.music.play()
        playing = True

    if keys[pygame.K_RIGHT] and zaderzhka():
        i = (i + 1) % 4
        pygame.mixer.music.load(music_list[i])
        pygame.mixer.music.play()
        playing = True

    pygame.display.update()
