import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Размеры экрана
WIDTH, HEIGHT = 800, 600

# Создание экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ну, погоди! — Волк ловит яйца")

# Загрузка изображений
wolf_img = pygame.image.load("assets/wolf.png")
egg_img = pygame.image.load("assets/egg.png")
background_img = pygame.image.load("assets/background.png")

# Загрузка музыки
pygame.mixer.music.load("assets/music.mp3")
pygame.mixer.music.play(-1)

# Классы
class Wolf(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = wolf_img
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH // 2
        self.rect.y = HEIGHT - self.rect.height

    def update(self):
        self.rect.x = pygame.mouse.get_pos()[0]
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x + self.rect.width > WIDTH:
            self.rect.x = WIDTH - self.rect.width

class Egg(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = egg_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = -self.rect.height

    def update(self):
        self.rect.y += 3
        if self.rect.y > HEIGHT:
            self.rect.y = -self.rect.height
            self.rect.x = random.randint(0, WIDTH - self.rect.width)

# Группы спрайтов
all_sprites = pygame.sprite.Group()
wolf = Wolf()
all_sprites.add(wolf)
eggs = pygame.sprite.Group()

for _ in range(5):
    egg = Egg()
    all_sprites.add(egg)
    eggs.add(egg)

# Игровой цикл
running = True
clock = pygame.time.Clock()

while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обновление спрайтов
    all_sprites.update()

    # Проверка столкновений
    if pygame.sprite.spritecollide(wolf, eggs, True):
        egg = Egg()
        all_sprites.add(egg)
