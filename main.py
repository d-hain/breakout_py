import pygame
import sys

from Direction import Direction
from GameState import GameState
from PlayerPaddle import PlayerPaddle
from typing import Optional

#     speed = [2, 2]
#
#     ball = pygame.image.load("gigachad-wine.png")
#     ballrect = ball.get_rect()
#
#     while True:
#         ballrect = ballrect.move(speed)
#         if ballrect.left < 0 or ballrect.right > width:
#             speed[0] = -speed[0]
#         if ballrect.top < 0 or ballrect.bottom > height:
#             speed[1] = -speed[1]
#
#         screen.blit(ball, ballrect)

TARGET_UPS = 60
WINDOW_TITLE = "breakout_py"
BACKGROUND_COLOR = (126, 72, 189)
FPS_TEXT_COLOR = (255, 255, 1)


def setup() -> tuple[pygame.Surface, GameState]:
    pygame.init()

    window_size = width, height = 669, 442
    screen: pygame.Surface = pygame.display.set_mode(window_size)
    pygame.display.set_caption(WINDOW_TITLE)

    # setup player
    player_width = width / 10
    player_height = height / 16
    player_pos_x = (width / 2) - (player_width / 2)
    player_pos_y = height - (height / 10)
    game_state = GameState(PlayerPaddle(
        pygame.rect.Rect(player_pos_x, player_pos_y, player_width, player_height),
        10.0,
        pygame.color.Color((255, 255, 50))
    ))

    # setup font
    # game_state.text_font = pygame.font.Font()

    return screen, game_state


def direction_from_key(key: int) -> Optional[Direction]:
    match key:
        case pygame.K_a:
            return Direction.Left
        case pygame.K_LEFT:
            return Direction.Left
        case pygame.K_d:
            return Direction.Right
        case pygame.K_RIGHT:
            return Direction.Right
    return None


def update(screen: pygame.Surface, game_state: GameState) -> None:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                game_state.player.direction = direction_from_key(event.key)
            # if event.key == pygame.K_LEFT:
            #     game_state.player.direction = Direction.Left
            # if event.key == pygame.K_RIGHT:
            #     game_state.player.direction = Direction.Right
        game_state.delta_time = game_state.clock.tick(TARGET_UPS)
        screen.fill(BACKGROUND_COLOR)

        # move player
        game_state.player.move()

        # draw player
        game_state.player.draw(screen)

        pygame.display.update()


if __name__ == "__main__":
    screen, game_state = setup()
    update(screen, game_state)
