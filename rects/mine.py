import random

class Mine():
    def __init__(self, screen, settings):
        # Атрибуты класса
        self.screen = screen
        self.settings = settings
        self.rdy_remove = False
        self.rdy_blowup = False
        self.crash_reload = 0
        # Загрузка изображения и получение прямоугольника
        self.surface = settings.mine00
        self.rect_left = self.surface.get_rect()
        self.rect_right = self.surface.get_rect()
        # Получение начальных координат изображения
        self.rect_left.centerx = random.randrange(120, 600, 40)
        self.rect_right.left = self.rect_left.left + 1200
        if settings.distance_car_red > settings.distance_car_green:
            self.rect_left.bottom = 0
            self.rect_right.bottom = - settings.distance_car_offset
        else:
            self.rect_left.bottom = - settings.distance_car_offset
            self.rect_right.bottom = 0

    def remove(self):
        if self.rdy_remove:
            self.settings.mines.remove(self)
        elif self.rect_left.top > self.screen.rect.bottom:
            if self.rect_right.top > self.screen.rect.bottom:
                self.settings.mines.remove(self)

    def update(self):
        self.rect_left.top += self.settings.round_speed_car_red
        self.rect_right.top += self.settings.round_speed_car_green
        if not self.rdy_blowup and self.crash_reload < self.settings.crash_timer:
            self.surface = self.settings.minelist[self.crash_reload]
            self.crash_reload += 1
        else:
            self.rdy_blowup = True

    # Вывод изображения на экран
    def blitme(self):
        self.screen.surface.blit(self.surface, self.rect_left)
        self.screen.surface.blit(self.surface, self.rect_right)