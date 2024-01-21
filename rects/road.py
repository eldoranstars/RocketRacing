class Road():
    def __init__(self, screen, settings):
        # Атрибуты класса
        self.screen = screen
        self.settings = settings
        # Загрузка изображения и получение прямоугольника
        self.surface = settings.road_surface
        self.rect_left = self.surface.get_rect()
        self.rect_right = self.surface.get_rect()
        # Получение начальных координат изображения
        self.rect_left.bottomleft = screen.rect.bottomleft
        self.rect_right.bottomright = screen.rect.bottomright

    def update(self):
        if not self.rect_left.collidepoint(self.screen.rect.topleft):
            self.rect_left.bottomleft = self.screen.rect.bottomleft
        # баг, почему то self.rect_right.topright всегда меньше self.screen.rect.topright на 1 по оси Х
        # if not self.rect_right.collidepoint(self.screen.rect.topright):
        if not self.rect_right.collidepoint(self.screen.rect.width - 1, 0):
            self.rect_right.bottomright = self.screen.rect.bottomright

    # Вывод изображения на экран
    def blitme(self):
        self.screen.surface.blit(self.surface, self.rect_left)
        self.screen.surface.blit(self.surface, self.rect_right)