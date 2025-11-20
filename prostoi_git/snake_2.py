import pygame
import random

pygame.init()

# цвет, размер, скорость 
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
GRAY = (40, 40, 40)
WIDTH, HEIGHT = 600, 600
CELL = 20
FPS = 7 

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# шрифт
font = pygame.font.SysFont('Verdana', 20, True)

# классы
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Snake:
    def __init__(self):
        self.body = [Point(10, 10)]
        self.dx = 1
        self.dy = 0
        self.score = 0
        self.level = 1
        self.foods_eaten = 0

    def move(self):
        new_head = Point(self.body[0].x + self.dx, self.body[0].y + self.dy)

# Проверка на столкновение со стеной
        if (new_head.x < 0 or new_head.x >= WIDTH // CELL or
            new_head.y < 0 or new_head.y >= HEIGHT // CELL):
            return False  

# Проверка на столкновение с собой
        for segment in self.body:
            if new_head.x == segment.x and new_head.y == segment.y:
                return False

# движение тело
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

# еда не должна появляться на змее
            if not any(p.x == self.x and p.y == self.y for p in snake.body):
                break
        
# вес еды
        self.weight = random.choice([1, 2, 3])

# цвет еды по весу
        self.color = {1: GREEN, 2: YELLOW, 3: RED}[self.weight]

# таймер жизни
        self.spawn_time = pygame.time.get_ticks()   
        self.lifetime = random.randint(3000, 6000)  

    def is_expired(self):
        return pygame.time.get_ticks() - self.spawn_time >= self.lifetime

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x * CELL, self.y * CELL, CELL, CELL))

def draw_grid():
    for x in range(0, WIDTH, CELL):
        pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL):
        pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y))


# оьекты 
snake = Snake()
food = Food(snake)
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BLACK) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# управление
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake.dy != 1:
        snake.dx, snake.dy = 0, -1
    elif keys[pygame.K_DOWN] and snake.dy != -1:
        snake.dx, snake.dy = 0, 1
    elif keys[pygame.K_LEFT] and snake.dx != 1:
        snake.dx, snake.dy = -1, 0
    elif keys[pygame.K_RIGHT] and snake.dx != -1:
        snake.dx, snake.dy = 1, 0

# движение змеи и окончание игры
    if not snake.move():
        running = False  
# проверка еды
    head = snake.body[0]

    # еда исчезает по таймеру
    if food.is_expired():
        food.randomize_position(snake)

    # змея съела еду
    elif head.x == food.x and head.y == food.y:
        snake.score += food.weight
        snake.foods_eaten += 1

    # растёт на вес еды
        for _ in range(food.weight):
            snake.grow()

        food.randomize_position(snake)

    # логика ускорения
        if snake.foods_eaten % 3 == 0:
            snake.level += 1
            FPS += 2

# вызов основных функций
    draw_grid()
    food.draw()
    snake.draw()

# показ очков и уровеня 
    score_text = font.render(f"Score: {snake.score}", True, WHITE)
    level_text = font.render(f"Level: {snake.level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 35))

    pygame.display.flip()
    clock.tick(FPS)

# заканчивает игру и выжидает паузу 
screen.fill(BLACK)
end_text = font.render(f"Game Over! Final Score: {snake.score}", True, RED)
screen.blit(end_text, (WIDTH // 2 - 150, HEIGHT // 2))
pygame.display.flip()
pygame.time.wait(3000)
pygame.quit()
