import random

class Nitro():
    def __init__(self, screen, settings):
        # Атрибуты класса
        self.screen = screen
        self.settings = settings
        self.rdy_remove = False
        # Загрузка изображения и получение прямоугольника
        self.surface = settings.nitro_surface
        self.rect_left = self.surface.get_rect()
        self.rect_right = self.surface.get_rect()
        # Получение начальных координат изображения
        self.rect_left.centerx = random.randrange(120, 600, 80)
        self.rect_right.left = self.rect_left.left + 1200
        self.rect_left.bottom = - 1200
        if settings.distance_car_red > settings.distance_car_green:
            self.rect_left.bottom = 0
            self.rect_right.bottom = - settings.distance_car_offset
        else:
            self.rect_left.bottom = - settings.distance_car_offset
            self.rect_right.bottom = 0

    def remove(self):
        if self.rdy_remove:
            self.settings.nitros.remove(self)
        elif self.rect_left.top > self.screen.rect.bottom:
            if self.rect_right.top > self.screen.rect.bottom:
                self.settings.nitros.remove(self)

    # Вывод изображения на экран
    def blitme(self):
        self.screen.surface.blit(self.surface, self.rect_left)
        self.screen.surface.blit(self.surface, self.rect_right)