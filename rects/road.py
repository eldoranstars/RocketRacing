class Road():
    def __init__(self, screen, settings):
        # Атрибуты класса
        self.screen = screen
        self.settings = settings
        # Загрузка изображения и получение прямоугольника
        self.surface = settings.road_surface
        self.rect_left_one = self.surface.get_rect()
        self.rect_right_one = self.surface.get_rect()
        self.rect_left_two = self.surface.get_rect()
        self.rect_right_two = self.surface.get_rect()
        # Получение начальных координат изображения
        self.rect_left_one.bottomleft = screen.rect.bottomleft
        self.rect_right_one.bottomright = screen.rect.bottomright
        self.rect_left_two.bottomleft = self.rect_left_one.topleft
        self.rect_right_two.bottomright = self.rect_right_one.topright

    # Меняем изображения местами, для непрерывной прокрутки дороги
    def update(self):
        if self.rect_left_one.top > self.screen.rect.bottom:
            self.rect_left_one.bottom = self.rect_left_two.top
        if self.rect_left_two.top > self.screen.rect.bottom:
            self.rect_left_two.bottom = self.rect_left_one.top
        if self.rect_right_one.top > self.screen.rect.bottom:
            self.rect_right_one.bottom = self.rect_right_two.top
        if self.rect_right_two.top > self.screen.rect.bottom:
            self.rect_right_two.bottom = self.rect_right_one.top

    # Вывод изображения на экран
    def blitme(self):
        self.screen.surface.blit(self.surface, self.rect_left_one)
        self.screen.surface.blit(self.surface, self.rect_left_two)
        self.screen.surface.blit(self.surface, self.rect_right_one)
        self.screen.surface.blit(self.surface, self.rect_right_two)