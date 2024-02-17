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
    gf.check_events(stats, joystick_zero, joystick_one)
    gf.blit_screen(stats)
    if stats.title_active and not stats.game_active:
        gf.update_title_text()
        gf.append_messages()
    if stats.game_active:
        gf.update_cars(joystick_zero, joystick_one)
        gf.update_rects(stats)
        gf.remove_rects()
        gf.append_rects()