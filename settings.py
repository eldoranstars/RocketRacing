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
        pygame.mixer.pre_init(44100,-16,2, 1024)
        # Параметры экрана
        self.screen_width = 1920
        self.screen_height = 1200
        self.screen_color = (100, 100, 100)
        self.car_red_color = (255, 0, 0)
        self.car_green_color = (0, 255, 0)
        # Параметры изображений
        self.fire00 = pygame.image.load(resource_path('media/fire00.png'))
        self.fire01 = pygame.image.load(resource_path('media/fire01.png'))
        self.fire02 = pygame.image.load(resource_path('media/fire02.png'))
        self.fire03 = pygame.image.load(resource_path('media/fire03.png'))
        self.fire04 = pygame.image.load(resource_path('media/fire04.png'))
        self.fire05 = pygame.image.load(resource_path('media/fire05.png'))
        self.fire06 = pygame.image.load(resource_path('media/fire06.png'))
        self.fire07 = pygame.image.load(resource_path('media/fire07.png'))
        self.fire08 = pygame.image.load(resource_path('media/fire08.png'))
        self.fire09 = pygame.image.load(resource_path('media/fire09.png'))
        self.fire10 = pygame.image.load(resource_path('media/fire10.png'))
        self.fire11 = pygame.image.load(resource_path('media/fire11.png'))
        self.fire12 = pygame.image.load(resource_path('media/fire12.png'))
        self.fire13 = pygame.image.load(resource_path('media/fire13.png'))
        self.fire14 = pygame.image.load(resource_path('media/fire14.png'))
        self.fire15 = pygame.image.load(resource_path('media/fire15.png'))
        self.fire16 = pygame.image.load(resource_path('media/fire16.png'))
        self.fire17 = pygame.image.load(resource_path('media/fire17.png'))
        self.fire18 = pygame.image.load(resource_path('media/fire18.png'))
        self.fire19 = pygame.image.load(resource_path('media/fire19.png'))
        self.fire20 = pygame.image.load(resource_path('media/fire20.png'))
        self.fire21 = pygame.image.load(resource_path('media/fire21.png'))
        self.fire22 = pygame.image.load(resource_path('media/fire22.png'))
        self.fire23 = pygame.image.load(resource_path('media/fire23.png'))
        self.fire24 = pygame.image.load(resource_path('media/fire24.png'))
        self.fire25 = pygame.image.load(resource_path('media/fire25.png'))
        self.fire26 = pygame.image.load(resource_path('media/fire26.png'))
        self.fire27 = pygame.image.load(resource_path('media/fire27.png'))
        self.fire28 = pygame.image.load(resource_path('media/fire28.png'))
        self.fire29 = pygame.image.load(resource_path('media/fire29.png'))
        self.fire30 = pygame.image.load(resource_path('media/fire30.png'))
        self.fire31 = pygame.image.load(resource_path('media/fire31.png'))
        self.fire32 = pygame.image.load(resource_path('media/fire32.png'))
        self.fire33 = pygame.image.load(resource_path('media/fire33.png'))
        self.fire34 = pygame.image.load(resource_path('media/fire34.png'))
        self.fire35 = pygame.image.load(resource_path('media/fire35.png'))
        self.fire36 = pygame.image.load(resource_path('media/fire36.png'))
        self.fire37 = pygame.image.load(resource_path('media/fire37.png'))
        self.fire38 = pygame.image.load(resource_path('media/fire38.png'))
        self.fire39 = pygame.image.load(resource_path('media/fire39.png'))
        self.fire40 = pygame.image.load(resource_path('media/fire40.png'))
        self.fire41 = pygame.image.load(resource_path('media/fire41.png'))
        self.fire42 = pygame.image.load(resource_path('media/fire42.png'))
        self.fire43 = pygame.image.load(resource_path('media/fire43.png'))
        self.fire44 = pygame.image.load(resource_path('media/fire44.png'))
        self.fire45 = pygame.image.load(resource_path('media/fire45.png'))
        self.fire46 = pygame.image.load(resource_path('media/fire46.png'))
        self.fire47 = pygame.image.load(resource_path('media/fire47.png'))
        self.firelist = [self.fire00, self.fire01, self.fire02, self.fire03, self.fire04, self.fire05, self.fire06, self.fire07, \
            self.fire08, self.fire09, self.fire10, self.fire11, self.fire12, self.fire13, self.fire14, self.fire15, \
            self.fire16, self.fire17, self.fire18, self.fire19, self.fire20, self.fire21, self.fire22, self.fire23, \
            self.fire24, self.fire25, self.fire26, self.fire27, self.fire28, self.fire29, self.fire30, self.fire31, \
            self.fire32, self.fire33, self.fire34, self.fire35, self.fire36, self.fire37, self.fire38, self.fire39, \
            self.fire40, self.fire41, self.fire42, self.fire43, self.fire44, self.fire45, self.fire46, self.fire47]
        self.road_surface = pygame.image.load(resource_path('media/road.jpg'))
        self.finish_surface = pygame.image.load(resource_path('media/finish.png'))
        self.finish_surface_mid = pygame.transform.scale(self.finish_surface, (140,40))
        self.oil_surface = pygame.image.load(resource_path('media/oil.png'))
        self.oil_surface = pygame.transform.scale(self.oil_surface, (85,50))
        self.nitro_surface = pygame.image.load(resource_path('media/nitro.png'))
        self.nitro_surface = pygame.transform.scale(self.nitro_surface, (40,40))
        self.truck_surface = pygame.image.load(resource_path('media/truck.png'))
        self.truck_surface = pygame.transform.scale(self.truck_surface, (45,120))
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
        self.wheel_sound = pygame.mixer.Sound(resource_path('media/wheel.mp3'))
        # self.intro_sound = pygame.mixer.Sound(resource_path('media/intro.mp3'))
        # self.outro_sound = pygame.mixer.Sound(resource_path('media/outro.mp3'))
        # Динамические параметры игры
        self.new_game()

    def update(self):
        self.round_speed_car_red = round(self.speed_car_red)
        self.round_speed_car_green = round(self.speed_car_green)
        self.distance_car_red += self.round_speed_car_red
        self.distance_car_green += self.round_speed_car_green
        self.distance_car_offset = abs(self.distance_car_red - self.distance_car_green)

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
        self.distance_factor = 5
        self.oil_chance_increment = 0
        self.oils = []
        self.nitros = []
        self.trucks = []
        self.tractor_chance_increment = 0
        self.nitro_chance_increment = 0
        self.truck_chance_increment = 0
        self.tractors_move_right = []
        self.tractors_move_left = []
        self.crash_timer = len(self.firelist)
        # Титры
        self.first_line = 0
        self.final_text = []
        self.messages = ['Producer:', 'eldoranstars', '', \
            'Project Manager:', 'eldoranstars', '', \
            'Game Developer:', 'eldoranstars', '', \
            'Game Designer:', 'eldoranstars', '', \
            'Sound Designer:', 'eldoranstars', '', \
            'Quality Assurance:', 'eldoranstars', '', \
            'Lead DevOps:', 'eldoranstars']