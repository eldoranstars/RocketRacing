class CarGreen():
    def __init__(self, screen, settings):
        # Атрибуты класса
        self.screen = screen
        self.settings = settings
        # Загрузка изображения и получение прямоугольника
        self.surface = settings.car_green_surface
        self.rect_origin = self.surface.get_rect()
        self.rect_mirror = self.surface.get_rect()
        # Получение начальных координат изображения
        self.rect_origin.centery = screen.rect.centery
        self.rect_origin.centerx = screen.rect.right -  screen.rect.centerx / 4
        self.rect_mirror.centery = screen.rect.centery
        self.rect_mirror.centerx = screen.rect.centerx / 2

    # Вывод изображения на экран
    def blitme(self):
        self.screen.surface.blit(self.surface, self.rect_origin)
        self.screen.surface.blit(self.surface, self.rect_mirror)