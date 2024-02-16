import random

class RTractor():
    def __init__(self, screen, settings):
        # Атрибуты класса
        self.screen = screen
        self.settings = settings
        self.speed = random.randrange(2,6)
        # Загрузка изображения и получение прямоугольника
        self.surface = random.choice(settings.tractor_mr)
        self.rect_left = self.surface.get_rect()
        self.rect_right = self.surface.get_rect()
        # Получение начальных координат изображения
        self.rect_left.left = random.randrange(0, 360, self.rect_left.width)
        self.rect_right.left = self.rect_left.left + 1200
        if settings.distance_car_red > settings.distance_car_green:
            self.rect_left.bottom = 0
            self.rect_right.bottom = - settings.distance_car_offset
        else:
            self.rect_left.bottom = - settings.distance_car_offset
            self.rect_right.bottom = 0

    def remove(self):
        if self.rect_left.centerx > 720:
            self.settings.tractors_move_right.remove(self)

    def update(self):
        self.rect_left.top += self.settings.round_speed_car_red
        self.rect_right.top += self.settings.round_speed_car_green
        self.rect_left.left += self.speed
        self.rect_right.left += self.speed

    # Вывод изображения на экран
    def blitme(self):
        self.screen.surface.blit(self.surface, self.rect_left)
        self.screen.surface.blit(self.surface, self.rect_right)