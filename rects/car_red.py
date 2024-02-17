class CarRed():
    def __init__(self, screen, settings):
        # Атрибуты класса
        self.screen = screen
        self.settings = settings
        self.crash_reload = 0
        self.nitro_reload = 0
        self.nitro_timer = 0
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
        self.new_game()

    def update(self):
        # учитываем торможение
        self.settings.speed_car_red = max(self.settings.speed_car_red - self.settings.bf_car_red, 0)
        # учитываем анимацию взрыва
        if self.crash and self.crash_reload < self.settings.crash_timer:
            self.rect_fire_origin.center = self.rect_origin.center
            self.rect_fire_mirror.center = self.rect_mirror.center
            self.fire_surface = self.settings.firelist[self.crash_reload]
            self.crash_reload += 1
        else:
            self.fire_surface = self.settings.firelist[-1]
            self.crash_reload = 0
            self.crash = False
        # учитываем скорость с нитро
        if self.nitro_reload < self.nitro_timer:
            self.settings.max_speed_car_red = 33
            self.settings.sf_car_red = 1
            self.nitro_reload += 1
        else:
            self.settings.max_speed_car_red = 22
            self.settings.sf_car_red = 0.3
            self.nitro_reload = 0
            self.nitro_timer = 0

    # Исходная позиция
    def new_game(self):
        self.rect_origin.centerx = self.screen.rect.centerx / 4
        self.rect_mirror.centerx = self.screen.rect.centerx + self.screen.rect.centerx / 2
        self.rect_mirror.centery = self.screen.rect.centery

    # Вывод изображения на экран
    def blitme(self):
        self.screen.surface.blit(self.surface, self.rect_origin)
        self.screen.surface.blit(self.surface, self.rect_mirror)
        if self.crash:
            self.screen.surface.blit(self.fire_surface, self.rect_fire_origin)
            self.screen.surface.blit(self.fire_surface, self.rect_fire_mirror)