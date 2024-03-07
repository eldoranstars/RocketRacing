import pygame
import game_functions as gf
import stats

pygame.init()
pygame.mouse.set_visible(False)
pygame.display.set_caption("Rocket Racing")
pygame.display.toggle_fullscreen()
clock = pygame.time.Clock()
stats = stats.GameStats()

while True:
    clock.tick(30)
    joystick_zero = pygame.joystick.Joystick(0) if pygame.joystick.get_count() > 0 else ''
    joystick_one = pygame.joystick.Joystick(1) if pygame.joystick.get_count() > 1 else ''
    gf.blit_screen()
    if stats.game == "game_active":
        gf.events_game_active(stats, joystick_zero, joystick_one)
        gf.update_cars(joystick_zero, joystick_one)
        gf.update_rects(stats)
        gf.remove_rects()
        gf.append_rects()
    if stats.game == "not_game_active":
        gf.blit_screen_not_game_active()
        gf.events_not_game_active(stats, joystick_zero, joystick_one)
    if stats.game == "title_active":
        gf.blit_screen_title_active()
        gf.events_title_active(stats, joystick_zero, joystick_one)
        gf.update_title_text()
        gf.append_messages()