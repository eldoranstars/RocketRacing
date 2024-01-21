import pygame
import random

class Cone():
    def __init__(self, screen, settings):
        # Атрибуты класса
        self.screen = screen
        self.settings = settings
        # Загрузка изображения и получение прямоугольника
        self.surface = settings.cone_surface
        self.rect_origin = self.surface.get_rect()
        self.rect_mirror = self.surface.get_rect()
        # Получение начальных координат изображения
        if settings.score_player_left > settings.score_player_right:
            self.rect_origin.centerx = random.randrange(0, settings.screen_width, self.rect.width)
            self.rect_origin.centery = 0
        else:
            self.rect_origin.centerx = random.randrange(self.rect.width, settings.screen_width, self.rect.width)
            self.rect_origin.centery = 0

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_w] == 1:
            self.rect_left.y += self.settings.speed_player_left
        if key[pygame.K_UP] == 1:
            self.rect_right.y += self.settings.speed_player_right

    # Вывод изображения на экран
    def blitme(self):
        self.screen.surface.blit(self.surface, self.rect_left)
        self.screen.surface.blit(self.surface, self.rect_right)