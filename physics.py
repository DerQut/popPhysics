import math

import pygame
import ui_elements


class PhysicsCircle(ui_elements.Ellipse):
    all_physics_circles = []

    def __init__(self, surface, x_cord, y_cord, radius, main_colour, x_velocity, y_velocity, is_visible=True, width=1):
        
        self.frame = ui_elements.Ellipse(surface, x_cord-width, y_cord-width, 2*(radius+width), 2*(radius+width), (255, 255, 255))
        
        super().__init__(surface, x_cord, y_cord, 2*radius, 2*radius, main_colour, is_visible)

        self.x_velocity = x_velocity
        self.y_velocity = y_velocity

        self.radius = radius

        self.has_collided = False

        PhysicsCircle.all_physics_circles.append(self)

    def move(self):
        self.x_cord = self.x_cord + self.x_velocity
        self.frame.x_cord = self.frame.x_cord + self.x_velocity

        self.y_cord = self.y_cord + self.y_velocity
        self.frame.y_cord = self.frame.y_cord + self.y_velocity

        if self.x_cord < 0 or self.x_cord+self.x_size > self.surface.x_size:
            self.x_velocity = self.x_velocity * -1

        if self.y_cord < 0 or self.y_cord+self.y_size > self.surface.y_size:
            self.y_velocity = self.y_velocity * -1

        self.rect_update()
        self.frame.rect_update()

    def collide(self, obstacle):

        self.x_velocity = -self.x_velocity
        self.y_velocity = -self.y_velocity

        obstacle.x_velocity = -obstacle.x_velocity
        obstacle.y_velocity = -obstacle.y_velocity

    @classmethod
    def collide_check(cls):
        for obj in cls.all_physics_circles:
            for obstacle in cls.all_physics_circles:
                if obj != obstacle and not obstacle.has_collided and not obj.has_collided:
                    if obstacle.radius + obj.radius >= math.sqrt((obstacle.x_cord-obj.x_cord)**2 + (obstacle.y_cord-obj.y_cord)**2):
                        obj.collide(obstacle)
                        obj.has_collided = True
                        obstacle.has_collided = True

    @classmethod
    def move_all(cls):
        for obj in cls.all_physics_circles:
            obj.move()
            obj.has_collided = False
