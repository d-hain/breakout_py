import pygame.time
from typing import Optional

from Ball import Ball
from PlayerPaddle import PlayerPaddle


class GameState:
    clock: pygame.time.Clock
    delta_time: int
    text_font: Optional[pygame.font.Font]
    player: PlayerPaddle
    ball: Ball

    def __init__(self, player: PlayerPaddle, ball: Ball) -> None:
        self.clock = pygame.time.Clock()
        self.delta_time = 0
        self.text_font = None
        self.player = player
        self.ball = ball
