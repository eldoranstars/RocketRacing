class Position():
    def __init__(self, screen, settings):
        # Атрибуты класса
        self.screen = screen
        self.settings = settings
        # Загрузка изображения и получение прямоугольника
        self.surface_left = settings.position_red_surface
        self.surface_right = settings.position_green_surface
        self.rect_left = self.surface_left.get_rect()
        self.rect_right = self.surface_right.get_rect()
        # Получение начальных координат изображения
        self.rect_left.centerx = screen.rect.centerx - 36
        self.rect_right.centerx = screen.rect.centerx + 36
        # self.new_game()

    # двигаемся к финишу
    def update(self):
        self.rect_left.top = self.screen.rect.h - round(self.settings.distance_car_red / self.settings.distance_factor)
        self.rect_right.top = self.screen.rect.h - round(self.settings.distance_car_green / self.settings.distance_factor)

    # исходная позиция
    def new_game(self):
        self.update()

    # вывод изображения на экран
    def blitme(self):
        self.screen.surface.blit(self.surface_left, self.rect_left)
        self.screen.surface.blit(self.surface_right, self.rect_right)