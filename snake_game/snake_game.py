import pygame
import random
from user_manager import get_or_create_user, save_score

pygame.init()

# цвета и настройки
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
GRAY = (40, 40, 40)
WIDTH, HEIGHT = 600, 600
CELL = 20
BASE_FPS = 7

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
font = pygame.font.SysFont('Verdana', 20, True)

# объекты
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self, level=1):
        self.body = [Point(10, 10)]
        self.dx = 1
        self.dy = 0
        self.score = 0
        self.level = level
        self.foods_eaten = 0

    def move(self, walls=[]):
        new_head = Point(self.body[0].x + self.dx, self.body[0].y + self.dy)

        if (new_head.x < 0 or new_head.x >= WIDTH // CELL or
            new_head.y < 0 or new_head.y >= HEIGHT // CELL):
            return False

        for segment in self.body:
            if new_head.x == segment.x and new_head.y == segment.y:
                return False

        for wall in walls:
            if new_head.x == wall.x and new_head.y == wall.y:
                return False

        self.body.insert(0, new_head)
        self.body.pop()
        return True

    def grow(self):
        tail = self.body[-1]
        self.body.append(Point(tail.x, tail.y))

    def draw(self):
        pygame.draw.rect(screen, RED, (self.body[0].x * CELL, self.body[0].y * CELL, CELL, CELL))
        for part in self.body[1:]:
            pygame.draw.rect(screen, YELLOW, (part.x * CELL, part.y * CELL, CELL, CELL))

class Food:
    def __init__(self, snake):
        self.randomize_position(snake)

    def randomize_position(self, snake):
        while True:
            self.x = random.randint(0, WIDTH // CELL - 1)
            self.y = random.randint(0, HEIGHT // CELL - 1)
            if not any(p.x == self.x and p.y == self.y for p in snake.body):
                break
        self.weight = random.choice([1,2,3])
        self.color = {1: GREEN, 2: YELLOW, 3: RED}[self.weight]
        self.spawn_time = pygame.time.get_ticks()
        self.lifetime = random.randint(3000, 6000)

    def is_expired(self):
        return pygame.time.get_ticks() - self.spawn_time >= self.lifetime

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x * CELL, self.y * CELL, CELL, CELL))

def draw_grid():
    for x in range(0, WIDTH, CELL):
        pygame.draw.line(screen, GRAY, (x,0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL):
        pygame.draw.line(screen, GRAY, (0,y), (WIDTH, y))

def generate_walls(level):
    return [Point(random.randint(0, WIDTH//CELL-1), random.randint(0, HEIGHT//CELL-1)) for _ in range(level*3)]

# ====== Главная программа ======
username = input("Enter your username: ")
user_id, user_level = get_or_create_user(username)

snake = Snake(level=user_level)
FPS = BASE_FPS + (snake.level - 1) * 2
food = Food(snake)
walls = generate_walls(snake.level)

clock = pygame.time.Clock()
running = True
paused = False

while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake.dy != 1:
        snake.dx, snake.dy = 0, -1
    elif keys[pygame.K_DOWN] and snake.dy != -1:
        snake.dx, snake.dy = 0, 1
    elif keys[pygame.K_LEFT] and snake.dx != 1:
        snake.dx, snake.dy = -1, 0
    elif keys[pygame.K_RIGHT] and snake.dx != -1:
        snake.dx, snake.dy = 1, 0

    if keys[pygame.K_p]:  # пауза и сохранение
        save_score(user_id, snake.score, snake.level)
        paused = True
        pause_text = font.render("Paused and saved! Press any key to continue", True, WHITE)
        screen.blit(pause_text, (50, HEIGHT // 2))
        pygame.display.flip()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    waiting = False
        paused = False

    if not paused:
        if not snake.move(walls):
            running = False

        head = snake.body[0]

        if food.is_expired():
            food.randomize_position(snake)
        elif head.x == food.x and head.y == food.y:
            snake.score += food.weight
            snake.foods_eaten += 1
            for _ in range(food.weight):
                snake.grow()
            food.randomize_position(snake)
            if snake.foods_eaten % 3 == 0:
                snake.level += 1
                FPS += 2
                walls = generate_walls(snake.level)

    draw_grid()
    for wall in walls:
        pygame.draw.rect(screen, GRAY, (wall.x*CELL, wall.y*CELL, CELL, CELL))
    food.draw()
    snake.draw()

    score_text = font.render(f"Score: {snake.score}", True, WHITE)
    level_text = font.render(f"Level: {snake.level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 35))

    pygame.display.flip()
    clock.tick(FPS)

# Конец игры
save_score(user_id, snake.score, snake.level)
screen.fill(BLACK)
end_text = font.render(f"Game Over! Final Score: {snake.score}", True, RED)
screen.blit(end_text, (WIDTH // 2 - 150, HEIGHT // 2))
pygame.display.flip()
pygame.time.wait(3000)
pygame.quit()
