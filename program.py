import random

import ui_elements
import window
import assets

import pygame
from pygame.locals import *

import physics


def loop_action():

    physics.PhysicsCircle.move_all()
    #ball1.colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def button_handler(down, event_key, needs_shifting, is_shifting):

    if down:
        ...
    else:
        ...


program_window = window.Window(1280, 720, DOUBLEBUF, assets.bg_colour, "Paint")

moving_surface = window.Surface(program_window, 80, 80, 1120, 560, assets.bg_colour)
border = ui_elements.Rect(moving_surface, 0, 0, 1120, 560, assets.button_colour_light, True, 2)

while len(physics.PhysicsCircle.all_physics_circles) < 20:
    new = physics.PhysicsCircle(moving_surface, random.randint(50, 1050), random.randint(50, 510), 50, assets.blue, random.randint(-10, 10), random.randint(-10, 10))

