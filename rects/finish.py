class Finish():
    def __init__(self, screen, settings):
        # Атрибуты класса
        self.screen = screen
        self.settings = settings
        # Загрузка изображения и получение прямоугольника
        self.surface = settings.finish_surface
        self.surface_mid = settings.finish_surface_mid
        self.surface_position = settings.position_red_surface
        self.surface_car = settings.car_red_surface
        self.rect_left = self.surface.get_rect()
        self.rect_right = self.surface.get_rect()
        self.rect_mid = self.surface_mid.get_rect()
        self.rect_position = self.surface_position.get_rect()
        self.rect_car = self.surface_car.get_rect()
        # Получение начальных координат изображения
        self.new_game()
        self.rect_left.left = screen.rect.left
        self.rect_right.right = screen.rect.right
        self.rect_mid.top = screen.rect.top
        self.rect_mid.centerx = screen.rect.centerx

    # двигаемся к финишу
    def update(self, stats):
        self.rect_left.top += self.settings.round_speed_car_red
        self.rect_right.top += self.settings.round_speed_car_green
        if self.rect_left.bottom > self.screen.rect.h / 2 or self.rect_right.bottom > self.screen.rect.h / 2:
            stats.game = "title_active"
            self.settings.intro_sound.stop()
            self.settings.outro_sound.play(-1)

    # Исходная позиция
    def new_game(self):
        self.distance_to_finish = (self.screen.rect.h - self.rect_mid.h - self.rect_position.h) * self.settings.distance_factor
        self.rect_left.bottom = self.screen.rect.h / 2 - self.rect_car.h / 2 - self.distance_to_finish
        self.rect_right.bottom = self.screen.rect.h / 2 - self.rect_car.h / 2 - self.distance_to_finish

    # Вывод изображения на экран
    def blitme(self):
        self.screen.surface.blit(self.surface, self.rect_left)
        self.screen.surface.blit(self.surface, self.rect_right)
        self.screen.surface.blit(self.surface_mid, self.rect_mid)