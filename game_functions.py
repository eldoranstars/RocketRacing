import sys
import pygame
import random
sys.path.append('rects')

from settings import Settings
from screen import Screen
from text import Text
from road import Road
from position import Position
from oil import Oil
from car_red import CarRed
from car_green import CarGreen

settings = Settings()
screen = Screen(settings)
road = Road(screen, settings)
position = Position(screen, settings)
car_red = CarRed(screen, settings)
car_green = CarGreen(screen, settings)
pause = Text(screen, "PAUSE: P or Start button", screen.rect.centerx, screen.rect.centery)
buttons = [pause]

# Получаем пиксельную маску для обработки коллизий.
def overlap_left(player, enemy):
    player.mask = pygame.mask.from_surface(player.surface)
    enemy.mask = pygame.mask.from_surface(enemy.surface)
    overlap = player.mask.overlap(enemy.mask, (enemy.rect_left.left - player.rect_origin.left, enemy.rect_left.top - player.rect_origin.top))
    return overlap

# Получаем пиксельную маску для обработки коллизий.
def overlap_right(player, enemy):
    player.mask = pygame.mask.from_surface(player.surface)
    enemy.mask = pygame.mask.from_surface(enemy.surface)
    overlap = player.mask.overlap(enemy.mask, (enemy.rect_right.left - player.rect_origin.left, enemy.rect_right.top - player.rect_origin.top))
    return overlap

def collision(self, rect, wm, hm):
    # Получаем дополнительный прямоугольник для обработки коллизий.
    collision = pygame.Rect(rect.center, (rect.width * wm, rect.height * hm))
    collision.center = rect.center
    return collision

# Вывод коллизий на экран.
def collision_test(object, wm, hm):
    screen.surface.blit(pygame.Surface((collision(object.rect, wm, hm).width,collision(object.rect, wm, hm).height)), collision(object.rect, wm, hm))

# Отслеживание нажатий клавиатуры и джойстика.
def check_events(stats, joystick_zero, joystick_one):
    if stats.game_active:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    stats.game_active = False
            if event.type == pygame.JOYBUTTONDOWN:
                if joystick.get_button(7) == 1:
                    stats.game_active = False
    if not stats.game_active:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_m:
                    if stats.music_active:
                        stats.music_active = False
                        pygame.mixer.pause()
                    else:
                        stats.music_active = True
                        pygame.mixer.unpause()
                if event.key == pygame.K_f:
                    pygame.display.toggle_fullscreen()
                if event.key == pygame.K_p:
                    stats.game_active = True
            if event.type == pygame.JOYBUTTONDOWN:
                if joystick.get_button(6) == 1:
                    pygame.quit()
                    sys.exit()
                if joystick.get_button(5) == 1:
                    if stats.music_active:
                        stats.music_active = False
                        pygame.mixer.pause()
                    else:
                        stats.music_active = True
                        pygame.mixer.unpause()
                if joystick.get_button(4) == 1:
                    pygame.display.toggle_fullscreen()
                if joystick.get_button(7) == 1:
                    stats.game_active = True

def update_cars(stats, joystick_zero, joystick_one):
    # pygame.key.get_pressed() используется для непрерывнной реакции на зажатые клавиши
    key = pygame.key.get_pressed()
    if key[pygame.K_w] == 1:
        settings.speed_car_red = min(settings.speed_car_red + settings.sf_car_red, settings.max_speed_car_red)
    if key[pygame.K_a] == 1 and car_red.rect_origin.left > screen.rect.left:
        car_red.rect_origin.x -= (round(settings.speed_car_red) / 2)
        car_red.rect_mirror.x -= (round(settings.speed_car_red) / 2)
    if key[pygame.K_d] == 1 and car_red.rect_mirror.right < screen.rect.right:
        car_red.rect_origin.x += (round(settings.speed_car_red) / 2)
        car_red.rect_mirror.x += (round(settings.speed_car_red) / 2)
    if key[pygame.K_UP] == 1:
        settings.speed_car_green = min(settings.speed_car_green + settings.sf_car_green, settings.max_speed_car_green)
    if key[pygame.K_LEFT] == 1 and car_green.rect_mirror.left > screen.rect.left:
        car_green.rect_origin.x -= (round(settings.speed_car_green) / 2)
        car_green.rect_mirror.x -= (round(settings.speed_car_green) / 2)
    if key[pygame.K_RIGHT] == 1 and car_green.rect_origin.right < screen.rect.right:
        car_green.rect_origin.x += (round(settings.speed_car_green) / 2)
        car_green.rect_mirror.x += (round(settings.speed_car_green) / 2)
    # перемещаем объекты исходя из значений скорости
    for oil in settings.oils:
        if overlap_left(car_red, oil):
            settings.speed_car_red = max(settings.speed_car_red / 2, 1)
        if overlap_right(car_green, oil):
            settings.speed_car_green = max(settings.speed_car_red / 2, 1)
        oil.rect_left.y += round(settings.speed_car_red)
        oil.rect_right.y += round(settings.speed_car_green)
        oil.update()
    road.rect_left_one.y += round(settings.speed_car_red)
    road.rect_left_two.y += round(settings.speed_car_red)
    road.rect_right_one.y += round(settings.speed_car_green)
    road.rect_right_two.y += round(settings.speed_car_green)
    settings.distance_car_red += round(settings.speed_car_red)
    settings.distance_car_green += round(settings.speed_car_green)
    settings.distance_car_offset = abs(settings.distance_car_red - settings.distance_car_green)
    car_green.rect_mirror.y = car_green.rect_mirror.y - round(settings.speed_car_green) + round(settings.speed_car_red)
    car_red.rect_mirror.y = car_red.rect_mirror.y - round(settings.speed_car_red) + round(settings.speed_car_green)

    # if joystick_zero:
    #     if joystick_zero.get_axis(0) and joystick_zero.get_axis(0) > 0.2:
    #         pass
    #     if joystick_zero.get_axis(0) and joystick_zero.get_axis(0) < -0.2:
    #         pass
    #     if joystick_zero.get_axis(1) and joystick_zero.get_axis(1) < -0.2:
    #         pass
    #     if joystick_zero.get_axis(1) and joystick_zero.get_axis(1) > 0.2:
    #         pass
    #     if joystick_zero.get_axis(5) > 0.2 and settings.bullet_left > 0:
    #         pass

def update_rects():
    road.update()
    car_red.update()
    car_green.update()
    position.update()

# Создание объектов в списке
def append_oil():
    if random.randrange(0,100) == 0 and len(settings.oils) <5:
        oil = Oil(screen, settings)
        settings.oils.append(oil)

# Вывод изображений на экран.
def blit_screen(stats):
    screen.blitme()
    road.blitme()
    position.blitme()
    for oil in settings.oils:
        oil.blitme()
    car_red.blitme()
    car_green.blitme()
    if not stats.game_active:
        for button in buttons:
            button.blitme()
    pygame.display.update()