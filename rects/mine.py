import random

class Mine():
    def __init__(self, screen, settings):
        # Атрибуты класса
        self.screen = screen
        self.settings = settings
        self.rdy_remove = False
        self.status = "rise"
        self.mine_reload = 0
        self.blowup_reload = 0
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
        # мина всплывает
        if self.status == "rise" and self.mine_reload < self.settings.mine_timer:
            self.surface = self.settings.minelist[self.mine_reload]
            self.mine_reload += 1
        elif self.status == "rise":
            self.status = "drift"
        # мина дрейфует
        if self.status == "drift" and self.blowup_reload < self.settings.mine_timer:
            self.blowup_reload += 1
        elif self.status == "drift":
            self.status = "down"
        # мина тонет
        if self.status == "down" and self.mine_reload > 0:
            self.mine_reload -= 1
            self.surface = self.settings.minelist[self.mine_reload]
        elif self.status == "down":
            self.mine_reload = 0
            self.status = "rise"

    # Вывод изображения на экран
    def blitme(self):
        self.screen.surface.blit(self.surface, self.rect_left)
        self.screen.surface.blit(self.surface, self.rect_right)