import random

import macos_ui
import ui_elements
import window
import assets

import pygame
from pygame.locals import *

import physics

MAX_SPEED = 4
RADIUS = 20

pygame.mixer.music.play()


def loop_action():

    physics.PhysicsCircle.collide_check()
    physics.PhysicsCircle.move_all()


def button_handler(down, event_key, needs_shifting, is_shifting):

    if down:
        if event_key == pygame.K_SPACE:
            new = physics.PhysicsCircle(moving_surface, random.randint(50, 750), random.randint(50, 510), RADIUS,
                                        (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                                        random.randint(1, MAX_SPEED), random.randint(1, MAX_SPEED))
        elif event_key == pygame.K_m:
            if music_button.is_playing:
                pygame.mixer.music.pause()
                music_button.label.change_text("Muzyka: wyłączona")
                music_button.is_playing = False
            else:
                pygame.mixer.music.unpause()
                music_button.label.change_text("Muzyka: włączona")
                music_button.is_playing = True
            music_button.center_text()
    else:
        ...


program_window = window.Window(1280, 720, DOUBLEBUF, assets.bg_colour, "Physics sim")

input_surface = window.Surface(program_window, 0, 0, 280, 720, assets.bg_colour)

add_button = macos_ui.RoundedLabelledButton(input_surface, 20, 80, 240, 40, assets.blue, pygame.K_SPACE, assets.dark_blue, "Dodaj kulkę", assets.text_colour, assets.SF_Pro_Medium_18, assets.dark_blue)
music_button = macos_ui.RoundedLabelledButton(input_surface, 20, 130, 240, 40, assets.blue, pygame.K_m, assets.dark_blue, "Muzyka: włączona", assets.text_colour, assets.SF_Pro_Medium_18, assets.dark_blue)
music_button.is_playing = True

moving_surface = window.Surface(program_window, 280, 80, 920, 560, assets.bg_colour)
border = ui_elements.Rect(moving_surface, 0, 0, moving_surface.x_size, moving_surface.y_size, assets.button_colour_light, True, 2)

while len(physics.PhysicsCircle.all_physics_circles) < 5:
    new = physics.PhysicsCircle(moving_surface, random.randint(50, 750), random.randint(50, 510), RADIUS, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), random.randint(1, MAX_SPEED), random.randint(1, MAX_SPEED))

