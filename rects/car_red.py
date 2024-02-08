class CarRed():
    def __init__(self, screen, settings):
        # Атрибуты класса
        self.screen = screen
        self.settings = settings
        self.crash_reload = 0
        self.crash = False
        # Загрузка изображения и получение прямоугольника
        self.surface = settings.car_red_surface
        self.fire_surface = settings.firelist[-1]
        self.rect_fire_origin = self.fire_surface.get_rect()
        self.rect_fire_mirror = self.fire_surface.get_rect()
        self.rect_origin = self.surface.get_rect()
        self.rect_mirror = self.surface.get_rect()
        # Получение начальных координат изображения
        self.rect_origin.centery = screen.rect.centery
        self.rect_origin.centerx = screen.rect.centerx / 4
        self.rect_mirror.centery = screen.rect.centery
        self.rect_mirror.centerx = screen.rect.centerx + screen.rect.centerx / 2

    # Учитываем торможение
    def update(self):
        if self.crash and self.crash_reload < self.settings.crash_timer:
            self.rect_fire_origin.center = self.rect_origin.center
            self.rect_fire_mirror.center = self.rect_mirror.center
            self.fire_surface = self.settings.firelist[self.crash_reload]
            self.crash_reload += 1
        else:
            self.fire_surface = self.settings.firelist[-1]
            self.crash_reload = 0
            self.crash = False
            self.settings.speed_car_red = max(self.settings.speed_car_red - self.settings.bf_car_red, 0)

    # Вывод изображения на экран
    def blitme(self):
        self.screen.surface.blit(self.surface, self.rect_origin)
        self.screen.surface.blit(self.surface, self.rect_mirror)
        if self.crash:
            self.screen.surface.blit(self.fire_surface, self.rect_fire_origin)
            self.screen.surface.blit(self.fire_surface, self.rect_fire_mirror)