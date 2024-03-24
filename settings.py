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
        self.mine00 = pygame.image.load(resource_path('media/mine00.png'))
        self.mine01 = pygame.image.load(resource_path('media/mine01.png'))
        self.mine02 = pygame.image.load(resource_path('media/mine02.png'))
        self.mine03 = pygame.image.load(resource_path('media/mine03.png'))
        self.mine04 = pygame.image.load(resource_path('media/mine04.png'))
        self.mine05 = pygame.image.load(resource_path('media/mine05.png'))
        self.mine06 = pygame.image.load(resource_path('media/mine06.png'))
        self.mine07 = pygame.image.load(resource_path('media/mine07.png'))
        self.mine08 = pygame.image.load(resource_path('media/mine08.png'))
        self.mine09 = pygame.image.load(resource_path('media/mine09.png'))
        self.mine10 = pygame.image.load(resource_path('media/mine10.png'))
        self.mine11 = pygame.image.load(resource_path('media/mine11.png'))
        self.mine12 = pygame.image.load(resource_path('media/mine12.png'))
        self.mine13 = pygame.image.load(resource_path('media/mine13.png'))
        self.mine14 = pygame.image.load(resource_path('media/mine14.png'))
        self.mine15 = pygame.image.load(resource_path('media/mine15.png'))
        self.mine16 = pygame.image.load(resource_path('media/mine16.png'))
        self.mine17 = pygame.image.load(resource_path('media/mine17.png'))
        self.mine18 = pygame.image.load(resource_path('media/mine18.png'))
        self.mine19 = pygame.image.load(resource_path('media/mine19.png'))
        self.mine20 = pygame.image.load(resource_path('media/mine20.png'))
        self.mine21 = pygame.image.load(resource_path('media/mine21.png'))
        self.mine22 = pygame.image.load(resource_path('media/mine22.png'))
        self.mine23 = pygame.image.load(resource_path('media/mine23.png'))
        self.mine24 = pygame.image.load(resource_path('media/mine24.png'))
        self.mine25 = pygame.image.load(resource_path('media/mine25.png'))
        self.mine26 = pygame.image.load(resource_path('media/mine26.png'))
        self.mine27 = pygame.image.load(resource_path('media/mine27.png'))
        self.mine28 = pygame.image.load(resource_path('media/mine28.png'))
        self.mine29 = pygame.image.load(resource_path('media/mine29.png'))
        self.mine30 = pygame.image.load(resource_path('media/mine30.png'))
        self.mine31 = pygame.image.load(resource_path('media/mine31.png'))
        self.mine32 = pygame.image.load(resource_path('media/mine32.png'))
        self.mine33 = pygame.image.load(resource_path('media/mine33.png'))
        self.mine34 = pygame.image.load(resource_path('media/mine34.png'))
        self.mine35 = pygame.image.load(resource_path('media/mine35.png'))
        self.mine36 = pygame.image.load(resource_path('media/mine36.png'))
        self.mine37 = pygame.image.load(resource_path('media/mine37.png'))
        self.mine38 = pygame.image.load(resource_path('media/mine38.png'))
        self.mine39 = pygame.image.load(resource_path('media/mine39.png'))
        self.mine40 = pygame.image.load(resource_path('media/mine40.png'))
        self.mine41 = pygame.image.load(resource_path('media/mine41.png'))
        self.mine42 = pygame.image.load(resource_path('media/mine42.png'))
        self.mine43 = pygame.image.load(resource_path('media/mine43.png'))
        self.mine44 = pygame.image.load(resource_path('media/mine44.png'))
        self.mine45 = pygame.image.load(resource_path('media/mine45.png'))
        self.mine46 = pygame.image.load(resource_path('media/mine46.png'))
        self.mine47 = pygame.image.load(resource_path('media/mine47.png'))
        self.mine00 = pygame.transform.scale(self.mine00, (31,31))
        self.mine01 = pygame.transform.scale(self.mine01, (31,31))
        self.mine02 = pygame.transform.scale(self.mine02, (31,31))
        self.mine03 = pygame.transform.scale(self.mine03, (31,31))
        self.mine04 = pygame.transform.scale(self.mine04, (31,31))
        self.mine05 = pygame.transform.scale(self.mine05, (31,31))
        self.mine06 = pygame.transform.scale(self.mine06, (31,31))
        self.mine07 = pygame.transform.scale(self.mine07, (31,31))
        self.mine08 = pygame.transform.scale(self.mine08, (31,31))
        self.mine09 = pygame.transform.scale(self.mine09, (31,31))
        self.mine10 = pygame.transform.scale(self.mine10, (31,31))
        self.mine11 = pygame.transform.scale(self.mine11, (31,31))
        self.mine12 = pygame.transform.scale(self.mine12, (31,31))
        self.mine13 = pygame.transform.scale(self.mine13, (31,31))
        self.mine14 = pygame.transform.scale(self.mine14, (31,31))
        self.mine15 = pygame.transform.scale(self.mine15, (31,31))
        self.mine16 = pygame.transform.scale(self.mine16, (31,31))
        self.mine17 = pygame.transform.scale(self.mine17, (31,31))
        self.mine18 = pygame.transform.scale(self.mine18, (31,31))
        self.mine19 = pygame.transform.scale(self.mine19, (31,31))
        self.mine20 = pygame.transform.scale(self.mine20, (31,31))
        self.mine21 = pygame.transform.scale(self.mine21, (31,31))
        self.mine22 = pygame.transform.scale(self.mine22, (31,31))
        self.mine23 = pygame.transform.scale(self.mine23, (31,31))
        self.mine24 = pygame.transform.scale(self.mine24, (31,31))
        self.mine25 = pygame.transform.scale(self.mine25, (31,31))
        self.mine26 = pygame.transform.scale(self.mine26, (31,31))
        self.mine27 = pygame.transform.scale(self.mine27, (31,31))
        self.mine28 = pygame.transform.scale(self.mine28, (31,31))
        self.mine29 = pygame.transform.scale(self.mine29, (31,31))
        self.mine30 = pygame.transform.scale(self.mine30, (31,31))
        self.mine31 = pygame.transform.scale(self.mine31, (31,31))
        self.mine32 = pygame.transform.scale(self.mine32, (31,31))
        self.mine33 = pygame.transform.scale(self.mine33, (31,31))
        self.mine34 = pygame.transform.scale(self.mine34, (31,31))
        self.mine35 = pygame.transform.scale(self.mine35, (31,31))
        self.mine36 = pygame.transform.scale(self.mine36, (31,31))
        self.mine37 = pygame.transform.scale(self.mine37, (31,31))
        self.mine38 = pygame.transform.scale(self.mine38, (31,31))
        self.mine39 = pygame.transform.scale(self.mine39, (31,31))
        self.mine40 = pygame.transform.scale(self.mine40, (31,31))
        self.mine41 = pygame.transform.scale(self.mine41, (31,31))
        self.mine42 = pygame.transform.scale(self.mine42, (31,31))
        self.mine43 = pygame.transform.scale(self.mine43, (31,31))
        self.mine44 = pygame.transform.scale(self.mine44, (31,31))
        self.mine45 = pygame.transform.scale(self.mine45, (31,31))
        self.mine46 = pygame.transform.scale(self.mine46, (31,31))
        self.mine47 = pygame.transform.scale(self.mine47, (31,31))
        self.minelist = [self.mine00, self.mine01, self.mine02, self.mine03, self.mine04, self.mine05, self.mine06, self.mine07, \
            self.mine08, self.mine09, self.mine10, self.mine11, self.mine12, self.mine13, self.mine14, self.mine15, \
            self.mine16, self.mine17, self.mine18, self.mine19, self.mine20, self.mine21, self.mine22, self.mine23, \
            self.mine24, self.mine25, self.mine26, self.mine27, self.mine28, self.mine29, self.mine30, self.mine31, \
            self.mine32, self.mine33, self.mine34, self.mine35, self.mine36, self.mine37, self.mine38, self.mine39, \
            self.mine40, self.mine41, self.mine42, self.mine43, self.mine44, self.mine45, self.mine46, self.mine47]
        self.road_surface = pygame.image.load(resource_path('media/road.jpg'))
        self.ocean_surface = pygame.image.load(resource_path('media/ocean.jpg'))
        self.finish_surface = pygame.image.load(resource_path('media/finish.png'))
        self.finish_surface_mid = pygame.transform.scale(self.finish_surface, (140,40))
        self.oil_surface = pygame.image.load(resource_path('media/oil.png'))
        self.oil_surface = pygame.transform.scale(self.oil_surface, (85,50))
        self.nitro_surface = pygame.image.load(resource_path('media/nitro.png'))
        self.nitro_surface = pygame.transform.scale(self.nitro_surface, (40,40))
        self.ambulance_surface = pygame.image.load(resource_path('media/truck.png'))
        self.ambulance_surface = pygame.transform.scale(self.ambulance_surface, (45,120))
        self.boat_surface = pygame.image.load(resource_path('media/boat.png'))
        self.boat_surface = pygame.transform.scale(self.boat_surface, (45,120))
        self.truck_surface = self.ambulance_surface
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
        self.medusa_ml1 = pygame.image.load(resource_path('media/medusa1.png'))
        self.medusa_ml2 = pygame.image.load(resource_path('media/medusa2.png'))
        self.medusa_ml3 = pygame.image.load(resource_path('media/medusa3.png'))
        self.medusa_ml4 = pygame.image.load(resource_path('media/medusa4.png'))
        self.medusa_ml1 = pygame.transform.scale(self.medusa_ml1, (61,49))
        self.medusa_ml2 = pygame.transform.scale(self.medusa_ml2, (61,49))
        self.medusa_ml3 = pygame.transform.scale(self.medusa_ml3, (61,49))
        self.medusa_ml4 = pygame.transform.scale(self.medusa_ml4, (61,49))
        self.medusa_mr1 = pygame.transform.flip(self.medusa_ml1, True, False)
        self.medusa_mr2 = pygame.transform.flip(self.medusa_ml2, True, False)
        self.medusa_mr3 = pygame.transform.flip(self.medusa_ml3, True, False)
        self.medusa_mr4 = pygame.transform.flip(self.medusa_ml4, True, False)
        self.medusa_ml = [self.medusa_ml1, self.medusa_ml2, self.medusa_ml3, self.medusa_ml4]
        self.medusa_mr = [self.medusa_mr1, self.medusa_mr2, self.medusa_mr3, self.medusa_mr4]
        self.object_ml = self.tractor_ml
        self.object_mr = self.tractor_mr
        self.car_red_surface = pygame.image.load(resource_path('media/car_red.png'))
        self.car_green_surface = pygame.image.load(resource_path('media/car_green.png'))
        self.car_red_surface = pygame.transform.scale(self.car_red_surface, (51,51))
        self.car_green_surface = pygame.transform.scale(self.car_green_surface, (51,51))
        self.car_red_long_surface = pygame.image.load(resource_path('media/car_red_long.png'))
        self.car_green_long_surface = pygame.image.load(resource_path('media/car_green_long.png'))
        self.car_red_long_surface = pygame.transform.scale(self.car_red_long_surface, (51,66))
        self.car_green_long_surface = pygame.transform.scale(self.car_green_long_surface, (51,66))
        self.boat_red_surface = pygame.image.load(resource_path('media/boat_red.png'))
        self.boat_green_surface = pygame.image.load(resource_path('media/boat_green.png'))
        self.boat_red_surface = pygame.transform.scale(self.boat_red_surface, (51,51))
        self.boat_green_surface = pygame.transform.scale(self.boat_green_surface, (51,51))
        self.boat_red_long_surface = pygame.image.load(resource_path('media/boat_red_long.png'))
        self.boat_green_long_surface = pygame.image.load(resource_path('media/boat_green_long.png'))
        self.boat_red_long_surface = pygame.transform.scale(self.boat_red_long_surface, (51,66))
        self.boat_green_long_surface = pygame.transform.scale(self.boat_green_long_surface, (51,66))
        self.position_red_surface = pygame.transform.scale(self.car_red_surface, (25,25))
        self.position_green_surface = pygame.transform.scale(self.car_green_surface, (25,25))
        self.start_light_surface = pygame.Surface((self.screen_height / 10, self.screen_height / 10))
        self.screen_surface = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.SCALED)
        # Параметры аудио
        self.bang_sound = pygame.mixer.Sound(resource_path('media/bang.mp3'))
        self.start_sound = pygame.mixer.Sound(resource_path('media/start.mp3'))
        self.intro_sound = pygame.mixer.Sound(resource_path('media/intro.mp3'))
        self.outro_sound = pygame.mixer.Sound(resource_path('media/outro.mp3'))
        self.intro_sound.set_volume(0.1)
        self.music_active = True
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
        self.max_speed_car_red = 22
        self.max_speed_car_green = 22
        self.speed_car_red = 0
        self.speed_car_green = 0
        self.round_speed_car_red = 0
        self.round_speed_car_green = 0
        self.distance_car_red = 0
        self.distance_car_green = 0
        self.distance_car_offset = 0
        self.distance_factor = 100
        self.oils = []
        self.nitros = []
        self.trucks = []
        self.mines = []
        self.tractors_move_right = []
        self.tractors_move_left = []
        self.oil_chance_increment = 0
        self.tractor_chance_increment = 0
        self.nitro_chance_increment = 0
        self.truck_chance_increment = 0
        self.mine_chance_increment = 0
        self.crash_timer = len(self.firelist)
        self.mine_timer = len(self.minelist)
        self.intro_sound.stop()
        self.outro_sound.stop()
        # Титры
        self.first_line = 0
        self.title_text = []
        self.messages = ['Producer:', 'eldoranstars', '', \
            'Project Manager:', 'eldoranstars', '', \
            'Game Developer:', 'eldoranstars', '', \
            'Game Designer:', 'eldoranstars', '', \
            'Sound Designer:', 'eldoranstars', '', \
            'Quality Assurance:', 'eldoranstars', '', \
            'Lead DevOps:', 'eldoranstars']