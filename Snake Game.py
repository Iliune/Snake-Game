import pygame, sys
from pygame.math import Vector2
import random

pygame.init()
rozm_kratki = 20
ilosc_kratek = 25

class Food:
    def __init__(self):
        self.position = self.pos_random()

    def draw(self):
        food_rect = pygame.Rect(self.position.x * rozm_kratki,self.position.y * rozm_kratki, rozm_kratki, rozm_kratki)
        pygame.draw.rect(screen,(40,50,20), food_rect)

    def pos_random(self):
        x = random.randint(0, ilosc_kratek-1)
        y = random.randint(0, ilosc_kratek-1)
        return Vector2(x,y)

class Snake:
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direction = Vector2(1,0)

    def draw(self):
        for block in self.body:
            block_rect = pygame.Rect(block.x * rozm_kratki, block.y * rozm_kratki, rozm_kratki, rozm_kratki)
            pygame.draw.rect(screen, (255, 255, 255), block_rect)

    def move(self):
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]

    def add_block(self):
        self.body.append(self.body[-1])

    def reset(self):
        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direction = Vector2(1,0)

    def check_collision(self):
        if not 0 <= self.body[0].x < ilosc_kratek or not 0 <= self.body[0].y < ilosc_kratek:
            return True
        for block in self.body[1:]:
            if block == self.body[0]:
                return True
        return False

screen = pygame.display.set_mode((ilosc_kratek * rozm_kratki, ilosc_kratek * rozm_kratki))
pygame.display.set_caption("Sssssssnake Game")
clock = pygame.time.Clock()

food = Food()
snake = Snake()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if snake.direction.y != 1:
                    snake.direction = Vector2(0,-1)
            elif event.key == pygame.K_DOWN:
                if snake.direction.y != -1:
                    snake.direction = Vector2(0,1)
            elif event.key == pygame.K_LEFT:
                if snake.direction.x != 1:
                    snake.direction = Vector2(-1,0)
            elif event.key == pygame.K_RIGHT:
                if snake.direction.x != -1:
                    snake.direction = Vector2(1,0)

    screen.fill((170,200,90))
    food.draw()
    snake.move()
    snake.draw()

    if snake.body[0] == food.position:
        food.position = food.pos_random()
        snake.add_block()

    if snake.check_collision():
        snake.reset()

    pygame.display.update()
    clock.tick(10)
