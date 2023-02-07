import pygame.time
from typing import Optional

from Ball import Ball
from PlayerPaddle import PlayerPaddle


class GameState:
    clock: pygame.time.Clock
    delta_time: int
    has_won: Optional[bool]
    text_font: Optional[pygame.font.Font]
    player: PlayerPaddle
    ball: Ball
    blocks: list[int]
    block_rects: dict[int, pygame.rect.Rect]

    def __init__(self, player: PlayerPaddle, ball: Ball, blocks: list[int]) -> None:
        self.clock = pygame.time.Clock()
        self.delta_time = 0
        self.has_won = None
        self.text_font = None
        self.player = player
        self.ball = ball
        self.blocks = blocks
        self.block_rects = {}
