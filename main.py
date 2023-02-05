import pygame
import sys

from Ball import Ball
from Direction import Direction
from GameState import GameState
from PlayerPaddle import PlayerPaddle
from typing import Optional, Sequence

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
    player_width = width / 8
    player_height = height / 18
    player_pos_x = (width / 2) - (player_width / 2)
    player_pos_y = height - (height / 10)

    game_state = GameState(PlayerPaddle(
        pygame.rect.Rect(player_pos_x, player_pos_y, player_width, player_height),
        6.5,
        pygame.color.Color((255, 255, 50))),
        Ball(
            pygame.math.Vector2(width / 2.0, height / 2.0),
            20.0,
            pygame.math.Vector2(7.0, 7.0),
            pygame.color.Color((255, 255, 50)),
        ),
    )

    # setup font
    # game_state.text_font = pygame.font.Font()

    return screen, game_state


def direction_from_keys(keys: Sequence[bool]) -> Optional[Direction]:
    # Left
    if keys[pygame.K_a]:
        return Direction.Left
    elif keys[pygame.K_LEFT]:
        return Direction.Left

    # Right
    if keys[pygame.K_d]:
        return Direction.Right
    elif keys[pygame.K_RIGHT]:
        return Direction.Right

    return None


def force_player_boundaries(player: PlayerPaddle, surface: pygame.Surface) -> None:
    """
    Keep player on the screen
    :param player: The player paddle
    :param surface: The pygame.Surface of the window
    """

    # Left Border
    if player.rect.x <= 0.0:
        player.rect.x = 0.0
        return

    # Right Border
    window_width = surface.get_width()
    if (player.rect.x + player.rect.w) >= window_width:
        player.rect.x = window_width - player.rect.w


def draw(screen: pygame.Surface, game_state: GameState) -> None:
    """
    Draw everything in the game
    :param screen: The pygame.Surface of the window
    :param game_state: The current GameState
    """

    # draw player
    game_state.player.draw(screen)

    # draw ball
    game_state.ball.draw(screen)


def update(screen: pygame.Surface, game_state: GameState) -> None:
    """
    Update everything in the game
    :param screen: The pygame.Surface of the window
    :param game_state: The current GameState
    """

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        game_state.delta_time = game_state.clock.tick(TARGET_UPS)
        screen.fill(BACKGROUND_COLOR)

        # change player direction from pressed keys
        pressed_keys = pygame.key.get_pressed()
        game_state.player.direction = direction_from_keys(pressed_keys)

        # move player
        game_state.player.move()

        # move ball # TODO: TEMP
        game_state.ball.position.x += game_state.ball.speed.x
        game_state.ball.position.y -= game_state.ball.speed.y

        force_player_boundaries(game_state.player, screen)

        # draw game
        draw(screen, game_state)

        pygame.display.update()


if __name__ == "__main__":
    screen, game_state = setup()
    update(screen, game_state)
