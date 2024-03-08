class StartLight():
    def __init__(self, screen, settings):
        # Атрибуты класса
        self.screen = screen
        self.settings = settings
        # Загрузка изображения и получение прямоугольника
        self.surface = self.settings.start_light_surface
        self.rect_top = self.surface.get_rect()
        self.rect_mid = self.surface.get_rect()
        self.rect_bot = self.surface.get_rect()
        self.new_game()
        # Получение начальных координат изображения
        self.rect_top.centerx = screen.rect.centerx
        self.rect_top.centery = screen.rect.centery - self.rect_mid.height * 1.5
        self.rect_mid.centerx = screen.rect.centerx
        self.rect_mid.centery = screen.rect.centery
        self.rect_bot.centerx = screen.rect.centerx
        self.rect_bot.centery = screen.rect.centery + self.rect_mid.height * 1.5

    # Исходная позиция
    def new_game(self):
        self.surface.fill(self.settings.screen_color)
        self.start_light_timer = 0
        self.start_light = True
        self.start_light_red = False
        self.start_light_yellow = False
        self.start_light_green = False

    # таймер светофора
    def update(self):
        if self.start_light:
            self.start_light_timer += 1
            if self.start_light_timer > 30 and not self.start_light_red:
                self.surface.fill((196, 30, 30))
                self.start_light_red = True
            if self.start_light_timer > 60 and not self.start_light_yellow:
                self.surface.fill((196, 196, 30))
                self.start_light_yellow = True
            if self.start_light_timer > 90 and not self.start_light_green:
                self.surface.fill((30, 196, 30))
                self.start_light_green = True
            if self.start_light_timer > 120:
                self.surface.fill(self.settings.screen_color)
                self.start_light = False

    # Вывод изображения на экран
    def blitme(self):
        if self.start_light:
            self.screen.surface.blit(self.surface, self.rect_top)
            self.screen.surface.blit(self.surface, self.rect_mid)
            self.screen.surface.blit(self.surface, self.rect_bot)