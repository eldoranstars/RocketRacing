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
from nitro import Nitro
from truck import Truck
from finish import Finish
from tractor_move_right import RTractor
from tractor_move_left import LTractor
from car_red import CarRed
from car_green import CarGreen

settings = Settings()
screen = Screen(settings)
road = Road(screen, settings)
finish = Finish(screen, settings)
position = Position(screen, settings)
car_red = CarRed(screen, settings)
car_green = CarGreen(screen, settings)
pause = Text(screen, "PAUSE: P or Start button", screen.rect.centerx, screen.rect.centery)
buttons = [pause]

# Получаем пиксельную маску для обработки коллизий.
def overlap_left(player, enemy):
    player.mask = pygame.mask.from_surface(player.surface)
    enemy.mask = pygame.mask.from_surface(enemy.surface)
    overlap = player.mask.overlap(enemy.mask, (enemy.rect_left.left - player.rect_left.left, enemy.rect_left.top - player.rect_left.top))
    return overlap

# Получаем пиксельную маску для обработки коллизий.
def overlap_right(player, enemy):
    player.mask = pygame.mask.from_surface(player.surface)
    enemy.mask = pygame.mask.from_surface(enemy.surface)
    overlap = player.mask.overlap(enemy.mask, (enemy.rect_right.left - player.rect_left.left, enemy.rect_right.top - player.rect_left.top))
    return overlap

def collision(rect, wm, hm):
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
            if event.type == pygame.JOYBUTTONDOWN and joystick_zero:
                if joystick_zero.get_button(7) == 1:
                    stats.game_active = False
            if event.type == pygame.JOYBUTTONDOWN and joystick_one:
                if joystick_one.get_button(7) == 1:
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
                    if stats.title_active:
                        new_game(stats)
            # нулевой
            if event.type == pygame.JOYBUTTONDOWN and joystick_zero:
                if joystick_zero.get_button(6) == 1:
                    pygame.quit()
                    sys.exit()
                if joystick_zero.get_button(5) == 1:
                    if stats.music_active:
                        stats.music_active = False
                        pygame.mixer.pause()
                    else:
                        stats.music_active = True
                        pygame.mixer.unpause()
                if joystick_zero.get_button(4) == 1:
                    pygame.display.toggle_fullscreen()
                if joystick_zero.get_button(7) == 1:
                    stats.game_active = True
                    if stats.title_active:
                        new_game(stats)
            # первый
            if event.type == pygame.JOYBUTTONDOWN and joystick_one:
                if joystick_one.get_button(6) == 1:
                    pygame.quit()
                    sys.exit()
                if joystick_one.get_button(5) == 1:
                    if stats.music_active:
                        stats.music_active = False
                        pygame.mixer.pause()
                    else:
                        stats.music_active = True
                        pygame.mixer.unpause()
                if joystick_one.get_button(4) == 1:
                    pygame.display.toggle_fullscreen()
                if joystick_one.get_button(7) == 1:
                    stats.game_active = True
                    if stats.title_active:
                        new_game(stats)

# запуск новой игры
def new_game(stats):
    finish.new_game()
    car_red.new_game()
    car_green.new_game()
    settings.new_game()
    stats.title_active = False

def update_cars(joystick_zero, joystick_one):
    # pygame.key.get_pressed() используется для непрерывнной реакции на зажатые клавиши
    key = pygame.key.get_pressed()
    # слева
    if key[pygame.K_w] == 1 and not car_red.crash:
        settings.speed_car_red = min(settings.speed_car_red + settings.sf_car_red, settings.max_speed_car_red)
    if key[pygame.K_a] == 1 and car_red.rect_left.left > screen.rect.left:
        car_red.rect_left.left -= round(settings.speed_car_red / 2)
        car_red.rect_right.left -= round(settings.speed_car_red / 2)
    if key[pygame.K_d] == 1 and car_red.rect_right.right < screen.rect.right:
        car_red.rect_left.left += round(settings.speed_car_red / 2)
        car_red.rect_right.left += round(settings.speed_car_red / 2)
    # справа
    if key[pygame.K_UP] == 1 and not car_green.crash:
        settings.speed_car_green = min(settings.speed_car_green + settings.sf_car_green, settings.max_speed_car_green)
    if key[pygame.K_LEFT] == 1 and car_green.rect_right.left > screen.rect.left:
        car_green.rect_left.left -= round(settings.speed_car_green / 2)
        car_green.rect_right.left -= round(settings.speed_car_green / 2)
    if key[pygame.K_RIGHT] == 1 and car_green.rect_left.right < screen.rect.right:
        car_green.rect_left.left += round(settings.speed_car_green / 2)
        car_green.rect_right.left += round(settings.speed_car_green / 2)
    # нулевой
    if joystick_zero:
        if joystick_zero.get_axis(5) > 0.2 and not car_red.crash:
            settings.speed_car_red = min(settings.speed_car_red + settings.sf_car_red, settings.max_speed_car_red)
        if joystick_zero.get_axis(0) < 0.2 and car_red.rect_left.left > screen.rect.left:
            car_red.rect_left.left -= round(settings.speed_car_red / 2)
            car_red.rect_right.left -= round(settings.speed_car_red / 2)
        if joystick_zero.get_axis(0) > -0.2 and car_red.rect_right.right < screen.rect.right:
            car_red.rect_left.left += round(settings.speed_car_red / 2)
            car_red.rect_right.left += round(settings.speed_car_red / 2)
    # первый
    if joystick_one:
        if joystick_one.get_axis(5) > 0.2 and not car_green.crash:
            settings.speed_car_green = min(settings.speed_car_green + settings.sf_car_green, settings.max_speed_car_green)
        if joystick_one.get_axis(0) < 0.2 and car_green.rect_right.left > screen.rect.left:
            car_green.rect_left.left -= round(settings.speed_car_green / 2)
            car_green.rect_right.left -= round(settings.speed_car_green / 2)
        if joystick_one.get_axis(0) > -0.2 and car_green.rect_left.right < screen.rect.right:
            car_green.rect_left.left += round(settings.speed_car_green / 2)
            car_green.rect_right.left += round(settings.speed_car_green / 2)

# перемещаем объекты исходя из значений скорости
def update_rects(stats):
    finish.update(stats)
    settings.update()
    road.update()
    car_red.update()
    car_green.update()
    position.update()
    car_green.rect_right.top = car_green.rect_right.top - settings.round_speed_car_green + settings.round_speed_car_red
    car_red.rect_right.top = car_red.rect_right.top - settings.round_speed_car_red + settings.round_speed_car_green
    for tractor in settings.tractors_move_right:
        tractor.update()
        if overlap_left(car_red, tractor) and not car_red.crash:
            settings.speed_car_red = 0
            car_red.crash = True
            car_red.bang = True
        if overlap_right(car_green, tractor) and not car_green.crash:
            settings.speed_car_green = 0
            car_green.crash = True
            car_green.bang = True
        for truck in settings.trucks:
            tractor.speed = 0 if truck.rect_left.colliderect(tractor.rect_left) else 5
            tractor.rdy_remove = True if truck.rect_left.collidepoint(tractor.rect_left.center) else False
    for tractor in settings.tractors_move_left:
        tractor.update()
        if overlap_left(car_red, tractor) and not car_red.crash:
            settings.speed_car_red = 0
            car_red.crash = True
            car_red.bang = True
        if overlap_right(car_green, tractor) and not car_green.crash:
            settings.speed_car_green = 0
            car_green.crash = True
            car_green.bang = True
        for truck in settings.trucks:
            tractor.speed = 0 if truck.rect_left.colliderect(tractor.rect_left) else 5
            tractor.rdy_remove = True if truck.rect_left.collidepoint(tractor.rect_left.center) else False
    for oil in settings.oils:
        oil.update()
        if overlap_left(car_red, oil):
            settings.speed_car_red = max(settings.speed_car_red / 2, 2)
        if overlap_right(car_green, oil):
            settings.speed_car_green = max(settings.speed_car_green / 2, 2)
    for nitro in settings.nitros:
        nitro.update()
        if overlap_left(car_red, nitro):
            nitro.rdy_remove = True
            car_red.nitro_timer += 60
        if overlap_right(car_green, nitro):
            nitro.rdy_remove = True
            car_green.nitro_timer += 60
    for truck in settings.trucks:
        truck.update()
        if overlap_left(car_red, truck):
            settings.speed_car_red = 0
            car_red.crash = True
            car_red.bang = True
            truck.rdy_remove = True
        if overlap_right(car_green, truck):
            settings.speed_car_green = 0
            car_green.crash = True
            car_green.bang = True
            truck.rdy_remove = True

# добавляем объекты в списки
def append_rects():
    max_distance = max(settings.distance_car_red,settings.distance_car_green)
    oil_chance_to_appear = (max_distance - settings.oil_chance_increment) / 100
    if random.randrange(0,100) < oil_chance_to_appear:
        oil = Oil(screen, settings)
        settings.oils.append(oil)
        settings.oil_chance_increment += 1000
    tractor_chance_to_appear = (max_distance - settings.tractor_chance_increment) / 100
    if random.randrange(0,100) < tractor_chance_to_appear:
        tractor = RTractor(screen, settings)
        settings.tractors_move_right.append(tractor)
        settings.tractor_chance_increment += 1000
    if random.randrange(0,100) < tractor_chance_to_appear:
        tractor = LTractor(screen, settings)
        settings.tractors_move_left.append(tractor)
        settings.tractor_chance_increment += 1000
    nitro_chance_to_appear = (max_distance - settings.nitro_chance_increment) / 100
    if random.randrange(0,100) < nitro_chance_to_appear:
        nitro = Nitro(screen, settings)
        settings.nitros.append(nitro)
        settings.nitro_chance_increment += 2000
    truck_chance_to_appear = (max_distance - settings.truck_chance_increment) / 100
    if random.randrange(0,100) < truck_chance_to_appear:
        truck = Truck(screen, settings)
        settings.trucks.append(truck)
        settings.truck_chance_increment += 2000

# Обновить расположение объектов на экране.
def update_title_text():
    for message in settings.title_text:
        message.scroll_text()

# Создание объектов в списке
def append_messages():
    for message in settings.messages:
        settings.first_line += 33
        new_message = Text(screen, message, screen.rect.centerx, screen.rect.bottom + settings.first_line)
        settings.title_text.append(new_message)
    settings.messages.clear()

# удаляем объекты из списков
def remove_rects():
    for oil in settings.oils:
        oil.remove()
    for nitro in settings.nitros:
        nitro.remove()
    for truck in settings.trucks:
        truck.remove()
    for tractor in settings.tractors_move_right:
        tractor.remove()
    for tractor in settings.tractors_move_left:
        tractor.remove()

# Вывод изображений на экран.
def blit_screen(stats):
    screen.blitme()
    road.blitme()
    finish.blitme()
    position.blitme()
    for oil in settings.oils:
        oil.blitme()
    for nitro in settings.nitros:
        nitro.blitme()
    for tractor in settings.tractors_move_right:
        tractor.blitme()
    for tractor in settings.tractors_move_left:
        tractor.blitme()
    for truck in settings.trucks:
        truck.blitme()
    car_red.blitme()
    car_green.blitme()
    if not stats.game_active and not stats.title_active:
        for button in buttons:
            button.blitme()
    if stats.title_active:
        for message in settings.title_text:
            message.blitme()
    pygame.display.update()