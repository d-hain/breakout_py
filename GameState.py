import pygame.time
from typing import Optional

from PlayerPaddle import PlayerPaddle


class GameState:
    clock: pygame.time.Clock
    delta_time: int
    text_font: Optional[pygame.font.Font]
    player: PlayerPaddle

    def __init__(self, player: PlayerPaddle) -> None:
        self.clock = pygame.time.Clock()
        self.delta_time = 0
        self.text_font = None
        self.player = player
