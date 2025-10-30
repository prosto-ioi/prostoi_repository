import pygame, time

pygame.init()


WIDTH, HEIGHT = 1410 , 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

clock_face = pygame.image.load("base_micky.jpg").convert_alpha()   
minute_hand = pygame.image.load("minute.png").convert_alpha()      
second_hand = pygame.image.load("second.png").convert_alpha()      



center = (WIDTH // 2, HEIGHT // 2)


mw, mh = minute_hand.get_size()
sw, sh = second_hand.get_size()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    screen.blit(clock_face, (0, 0))

    now = time.localtime()
    sec = now.tm_sec
    minute = now.tm_min

    second_angle = -sec * 6       
    minute_angle = -minute * 6 - sec * 0.1  

    rot_minute = pygame.transform.rotate(minute_hand, minute_angle)
    rot_second = pygame.transform.rotate(second_hand, second_angle)

    min_rect = rot_minute.get_rect(center=center)
    sec_rect = rot_second.get_rect(center=center)

    screen.blit(rot_minute, min_rect.topleft)
    screen.blit(rot_second, sec_rect.topleft)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
