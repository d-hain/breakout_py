import pygame
from typing import Optional

from Direction import Direction


class PlayerPaddle:
    rect: pygame.Rect
    speed: float
    direction: Optional[Direction]
    color: pygame.Color

    def __init__(self, rect: pygame.Rect, speed: float, color: pygame.Color) -> None:
        self.rect = rect
        self.speed = speed
        self.direction = None
        self.color = color

    def move(self) -> None:
        match self.direction:
            case Direction.Left:
                self.rect.x -= self.speed
            case Direction.Right:
                self.rect.x += self.speed
        self.direction = None

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.rect(surface, self.color, self.rect)
