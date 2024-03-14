class CarGreen():
    def __init__(self, screen, settings):
        # Атрибуты класса
        self.screen = screen
        self.settings = settings
        # Загрузка изображения и получение прямоугольника
        self.surface = settings.car_green_surface
        self.fire_surface = settings.firelist[-1]
        self.rect_fire_origin = self.fire_surface.get_rect()
        self.rect_fire_mirror = self.fire_surface.get_rect()
        self.rect_left = self.surface.get_rect()
        self.rect_right = self.surface.get_rect()
        # Получение начальных координат изображения
        self.rect_left.centery = screen.rect.centery
        self.new_game()

    def update(self):
        # учитываем торможение
        self.settings.speed_car_green = max(self.settings.speed_car_green - self.settings.bf_car_green, 0)
        # учитываем анимацию взрыва
        if self.bang:
            self.settings.bang_sound.play()
            self.bang = False
        if self.crash and self.crash_reload < self.settings.crash_timer:
            self.rect_fire_origin.center = self.rect_left.center
            self.rect_fire_mirror.center = self.rect_right.center
            self.fire_surface = self.settings.firelist[self.crash_reload]
            self.crash_reload += 1
        else:
            self.fire_surface = self.settings.firelist[-1]
            self.crash_reload = 0
            self.crash = False
        # учитываем скорость с нитро
        if self.surface == self.settings.car_green_surface or self.surface == self.settings.boat_green_surface:
            if self.nitro_reload < self.nitro_timer:
                self.settings.max_speed_car_green = 33
                self.settings.sf_car_green = 1
                self.nitro_reload += 1
            else:
                self.settings.max_speed_car_green = 22
                self.settings.sf_car_green = 0.3
                self.nitro_reload = 0
                self.nitro_timer = 0
        if self.surface == self.settings.car_green_long_surface or self.surface == self.settings.boat_green_long_surface:
            if self.nitro_reload < self.nitro_timer:
                self.settings.max_speed_car_green = 39
                self.settings.sf_car_green = 0.72
                self.nitro_reload += 1
            else:
                self.settings.max_speed_car_green = 26
                self.settings.sf_car_green = 0.24
                self.nitro_reload = 0
                self.nitro_timer = 0

    # Исходная позиция
    def new_game(self):
        self.crash_reload = 0
        self.nitro_reload = 0
        self.nitro_timer = 0
        self.crash = False
        self.bang = False
        self.rect_left.centerx = self.screen.rect.right -  self.screen.rect.centerx / 4
        self.rect_right.centery = self.screen.rect.centery
        self.rect_right.centerx = self.screen.rect.centerx / 2

    # Вывод изображения на экран
    def blitme(self):
        self.screen.surface.blit(self.surface, self.rect_left)
        self.screen.surface.blit(self.surface, self.rect_right)
        if self.crash:
            self.screen.surface.blit(self.fire_surface, self.rect_fire_origin)
            self.screen.surface.blit(self.fire_surface, self.rect_fire_mirror)