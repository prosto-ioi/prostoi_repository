import pygame
import time
pygame.init()
screen = pygame.display.set_mode((900, 800))
pygame.display.set_caption("AAAAAAAAAA")

running = True
x = 450
y = 400

a = 0
def zaderzhka():
    global a
    if time.time() - a > 0.1:
        a = time.time()
        return True
    return False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    screen.fill("White")

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 25 and zaderzhka():
        x -= 25
    if keys[pygame.K_RIGHT] and x < 875 and zaderzhka():
        x += 25
    if keys[pygame.K_UP] and y > 25 and zaderzhka():
        y -= 25
    if keys[pygame.K_DOWN] and y < 775 and zaderzhka():
        y += 25
    
    pygame.draw.circle(screen, "red", (x, y), 50)

    pygame.display.update()
