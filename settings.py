import pygame
import sys
import os

# Get absolute path to resource, works for dev and for PyInstaller
def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

class Settings():
    def __init__(self):
        pygame.init()
        # Параметры экрана
        self.screen_width = 1920
        self.screen_height = 1200
        self.screen_color = (100, 100, 100)
        self.car_red_color = (255, 0, 0)
        self.car_green_color = (0, 255, 0)
        # Параметры изображений
        self.road_surface = pygame.image.load(resource_path('media/road.jpg'))
        self.oil_surface = pygame.image.load(resource_path('media/oil.png'))
        self.oil_surface = pygame.transform.scale(self.oil_surface, (85,50))
        self.tractor_ml1 = pygame.image.load(resource_path('media/tractor1.png'))
        self.tractor_ml2 = pygame.image.load(resource_path('media/tractor2.png'))
        self.tractor_ml3 = pygame.image.load(resource_path('media/tractor3.png'))
        self.tractor_ml4 = pygame.image.load(resource_path('media/tractor4.png'))
        self.tractor_ml1 = pygame.transform.scale(self.tractor_ml1, (61,49))
        self.tractor_ml2 = pygame.transform.scale(self.tractor_ml2, (61,49))
        self.tractor_ml3 = pygame.transform.scale(self.tractor_ml3, (61,49))
        self.tractor_ml4 = pygame.transform.scale(self.tractor_ml4, (61,49))
        self.tractor_mr1 = pygame.transform.flip(self.tractor_ml1, True, False)
        self.tractor_mr2 = pygame.transform.flip(self.tractor_ml2, True, False)
        self.tractor_mr3 = pygame.transform.flip(self.tractor_ml3, True, False)
        self.tractor_mr4 = pygame.transform.flip(self.tractor_ml4, True, False)
        self.tractor_ml = [self.tractor_ml1, self.tractor_ml2, self.tractor_ml3, self.tractor_ml4]
        self.tractor_mr = [self.tractor_mr1, self.tractor_mr2, self.tractor_mr3, self.tractor_mr4]
        self.car_red_surface = pygame.image.load(resource_path('media/car_red.png'))
        self.car_green_surface = pygame.image.load(resource_path('media/car_green.png'))
        self.car_red_surface = pygame.transform.scale(self.car_red_surface, (51,51))
        self.car_green_surface = pygame.transform.scale(self.car_green_surface, (51,51))
        self.position_red_surface = pygame.transform.scale(self.car_red_surface, (25,25))
        self.position_green_surface = pygame.transform.scale(self.car_green_surface, (25,25))
        self.screen_surface = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.SCALED)
        # Параметры аудио
        # self.intro_sound = pygame.mixer.Sound(resource_path('media/intro.mp3'))
        # self.outro_sound = pygame.mixer.Sound(resource_path('media/outro.mp3'))
        # Динамические параметры игры
        self.new_game()

    def update(self):
        self.round_speed_car_red = round(self.speed_car_red)
        self.round_speed_car_green = round(self.speed_car_green)

    # Сбросить параметры для новой игры
    def new_game(self):
        self.bf_car_red = 0.1
        self.bf_car_green = 0.1
        self.sf_car_red = 0.3
        self.sf_car_green = 0.3
        self.speed_car_red = 0
        self.speed_car_green = 0
        self.round_speed_car_red = 0
        self.round_speed_car_green = 0
        self.max_speed_car_red = 22
        self.max_speed_car_green = 22
        self.distance_car_red = 0
        self.distance_car_green = 0
        self.distance_car_offset = 0
        self.oil_chance_increment = 0
        self.oils = []
        self.tractor_chance_increment = 0
        self.tractors_move_right = []
        self.tractors_move_left = []