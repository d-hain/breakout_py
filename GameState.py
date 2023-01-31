import pygame.time

from PlayerPaddle import PlayerPaddle


class GameState:
    clock: pygame.time.Clock
    delta_time: int
    text_font: pygame.font.Font | None
    player: PlayerPaddle

    def __init__(self, player: PlayerPaddle) -> None:
        self.clock = pygame.time.Clock()
        self.delta_time = 0
        self.text_font = None
        self.player = player
