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
        self.new_game()

    # Меняем изображения местами, для непрерывной прокрутки дороги
    def update(self):
        self.rect_left_one.top += self.settings.round_speed_car_red
        self.rect_left_two.top += self.settings.round_speed_car_red
        self.rect_right_one.top += self.settings.round_speed_car_green
        self.rect_right_two.top += self.settings.round_speed_car_green
        if self.rect_left_one.top > self.screen.rect.bottom:
            self.rect_left_one.bottom = self.rect_left_two.top
        if self.rect_left_two.top > self.screen.rect.bottom:
            self.rect_left_two.bottom = self.rect_left_one.top
        if self.rect_right_one.top > self.screen.rect.bottom:
            self.rect_right_one.bottom = self.rect_right_two.top
        if self.rect_right_two.top > self.screen.rect.bottom:
            self.rect_right_two.bottom = self.rect_right_one.top

    # Исходная позиция
    def new_game(self):
        self.rect_left_one.bottomleft = self.screen.rect.bottomleft
        self.rect_right_one.bottomright = self.screen.rect.bottomright
        self.rect_left_two.bottomleft = self.rect_left_one.topleft
        self.rect_right_two.bottomright = self.rect_right_one.topright

    # Вывод изображения на экран
    def blitme(self):
        self.screen.surface.blit(self.surface, self.rect_left_one)
        self.screen.surface.blit(self.surface, self.rect_left_two)
        self.screen.surface.blit(self.surface, self.rect_right_one)
        self.screen.surface.blit(self.surface, self.rect_right_two)