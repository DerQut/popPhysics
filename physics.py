import pygame
import ui_elements


class PhysicsCircle(ui_elements.Ellipse):
    all_physics_circles = []

    def __init__(self, surface, x_cord, y_cord, radius, main_colour, x_velocity, y_velocity, is_visible=True, width=0):
        super().__init__(surface, x_cord, y_cord, radius, radius, main_colour, is_visible, width)

        self.x_velocity = x_velocity
        self.y_velocity = y_velocity

        PhysicsCircle.all_physics_circles.append(self)

    def move(self):
        print("Moved")
        self.x_cord = self.x_cord + self.x_velocity
        self.y_cord = self.y_cord + self.y_velocity

        if self.x_cord < 0 or self.x_cord > self.surface.x_size:
            self.x_velocity = self.x_velocity * -1

        if self.y_cord < 0 or self.y_cord > self.surface.y_size:
            self.y_velocity = self.y_velocity * -1

        self.rect_update()

    @classmethod
    def move_all(cls):
        for obj in cls.all_physics_circles:
            obj.move()
