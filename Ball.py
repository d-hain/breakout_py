import pygame
from pygame.math import Vector2


class Ball:
    position: Vector2
    radius: float
    speed: Vector2
    color: pygame.color.Color

    def __init__(self, position: Vector2, radius: float, speed: Vector2, color: pygame.color.Color):
        self.position = position
        self.radius = radius
        self.speed = speed
        self.color = color

    def draw(self, surface: pygame.Surface):
        pygame.draw.circle(
            surface,
            self.color,
            self.position,
            self.radius,
        )
