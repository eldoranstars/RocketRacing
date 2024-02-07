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
        self.fire11 = pygame.image.load(resource_path('media/fire11.png'))
        self.fire12 = pygame.image.load(resource_path('media/fire12.png'))
        self.fire13 = pygame.image.load(resource_path('media/fire13.png'))
        self.fire14 = pygame.image.load(resource_path('media/fire14.png'))
        self.fire15 = pygame.image.load(resource_path('media/fire15.png'))
        self.fire16 = pygame.image.load(resource_path('media/fire16.png'))
        self.fire17 = pygame.image.load(resource_path('media/fire17.png'))
        self.fire18 = pygame.image.load(resource_path('media/fire18.png'))
        self.fire21 = pygame.image.load(resource_path('media/fire21.png'))
        self.fire22 = pygame.image.load(resource_path('media/fire22.png'))
        self.fire23 = pygame.image.load(resource_path('media/fire23.png'))
        self.fire24 = pygame.image.load(resource_path('media/fire24.png'))
        self.fire25 = pygame.image.load(resource_path('media/fire25.png'))
        self.fire26 = pygame.image.load(resource_path('media/fire26.png'))
        self.fire27 = pygame.image.load(resource_path('media/fire27.png'))
        self.fire28 = pygame.image.load(resource_path('media/fire28.png'))
        self.fire31 = pygame.image.load(resource_path('media/fire31.png'))
        self.fire32 = pygame.image.load(resource_path('media/fire32.png'))
        self.fire33 = pygame.image.load(resource_path('media/fire33.png'))
        self.fire34 = pygame.image.load(resource_path('media/fire34.png'))
        self.fire35 = pygame.image.load(resource_path('media/fire35.png'))
        self.fire36 = pygame.image.load(resource_path('media/fire36.png'))
        self.fire37 = pygame.image.load(resource_path('media/fire37.png'))
        self.fire38 = pygame.image.load(resource_path('media/fire38.png'))
        self.fire41 = pygame.image.load(resource_path('media/fire41.png'))
        self.fire42 = pygame.image.load(resource_path('media/fire42.png'))
        self.fire43 = pygame.image.load(resource_path('media/fire43.png'))
        self.fire44 = pygame.image.load(resource_path('media/fire44.png'))
        self.fire45 = pygame.image.load(resource_path('media/fire45.png'))
        self.fire46 = pygame.image.load(resource_path('media/fire46.png'))
        self.fire47 = pygame.image.load(resource_path('media/fire47.png'))
        self.fire48 = pygame.image.load(resource_path('media/fire48.png'))
        self.fire51 = pygame.image.load(resource_path('media/fire51.png'))
        self.fire52 = pygame.image.load(resource_path('media/fire52.png'))
        self.fire53 = pygame.image.load(resource_path('media/fire53.png'))
        self.fire54 = pygame.image.load(resource_path('media/fire54.png'))
        self.fire55 = pygame.image.load(resource_path('media/fire55.png'))
        self.fire56 = pygame.image.load(resource_path('media/fire56.png'))
        self.fire57 = pygame.image.load(resource_path('media/fire57.png'))
        self.fire58 = pygame.image.load(resource_path('media/fire58.png'))
        self.fire61 = pygame.image.load(resource_path('media/fire61.png'))
        self.fire62 = pygame.image.load(resource_path('media/fire62.png'))
        self.fire63 = pygame.image.load(resource_path('media/fire63.png'))
        self.fire64 = pygame.image.load(resource_path('media/fire64.png'))
        self.fire65 = pygame.image.load(resource_path('media/fire65.png'))
        self.fire66 = pygame.image.load(resource_path('media/fire66.png'))
        self.fire67 = pygame.image.load(resource_path('media/fire67.png'))
        self.fire68 = pygame.image.load(resource_path('media/fire68.png'))
        self.firelist = [self.fire11, self.fire12, self.fire13, self.fire14, self.fire15, self.fire16, self.fire17, self.fire18, \
            self.fire21, self.fire22, self.fire23, self.fire24, self.fire25, self.fire26, self.fire27, self.fire28, \
            self.fire31, self.fire32, self.fire33, self.fire34, self.fire35, self.fire36, self.fire37, self.fire38, \
            self.fire41, self.fire42, self.fire43, self.fire44, self.fire45, self.fire46, self.fire47, self.fire48, \
            self.fire51, self.fire52, self.fire53, self.fire54, self.fire55, self.fire56, self.fire57, self.fire58, \
            self.fire61, self.fire62, self.fire63, self.fire64, self.fire65, self.fire66, self.fire67, self.fire68]
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
        self.crash_reload = 47