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

        self.rect_update()
        self.frame.rect_update()

    def collide(self, obstacle):

        v1 = (self.x_velocity, self.y_velocity)
        v2 = (obstacle.x_velocity, obstacle.y_velocity)

        self.x_velocity = v2[0]
        self.y_velocity = v2[1]

        obstacle.x_velocity = v1[0]
        obstacle.y_velocity = v1[1]

    def shove(self, x, y):
        self.x_cord = self.x_cord + x
        self.y_cord = self.y_cord + y

        self.frame.x_cord = self.frame.x_cord + x
        self.frame.y_cord = self.frame.y_cord + y

        self.rect_update()
        self.frame.rect_update()

    @classmethod
    def collide_check(cls):
        for obj in cls.all_physics_circles:
            for obstacle in cls.all_physics_circles:
                if obj != obstacle and not obstacle.has_collided and not obj.has_collided:
                    if obstacle.radius + obj.radius >= math.sqrt((obstacle.x_cord-obj.x_cord)**2 + (obstacle.y_cord-obj.y_cord)**2):
                        obj.collide(obstacle)
                        obj.has_collided = True
                        obstacle.has_collided = True
                        while obstacle.radius + obj.radius >= math.sqrt((obstacle.x_cord - obj.x_cord) ** 2 + (obstacle.y_cord - obj.y_cord) ** 2):
                            obj.move()
                            obstacle.move()

            if obj.y_cord < 0 or obj.y_cord+obj.y_size > obj.surface.y_size:
                obj.y_velocity = -obj.y_velocity
                while obj.y_cord < 0 or obj.y_cord+obj.y_size > obj.surface.y_size:
                    obj.move()

            if obj.x_cord < 0 or obj.x_cord+obj.x_size > obj.surface.x_size:
                obj.x_velocity = -obj.x_velocity
                while obj.x_cord < 0 or obj.x_cord+obj.x_size > obj.surface.x_size:
                    obj.move()

    @classmethod
    def move_all(cls):
        for obj in cls.all_physics_circles:
            if not obj.has_collided:
                obj.move()
            obj.has_collided = False
