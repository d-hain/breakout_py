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
        7.5,
        pygame.color.Color((255, 255, 50))),
        Ball(
            pygame.math.Vector2(width / 2.0, height / 2.0),
            20.0,
            pygame.math.Vector2(7.0, 7.0),
            pygame.color.Color((255, 255, 50)),
        ),
    )

    # setup font
    game_state.text_font = pygame.font.SysFont("Arial", 26)

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


def force_player_boundaries(player: PlayerPaddle, screen: pygame.Surface) -> None:
    """
    Keep player on the screen
    :param player: The player paddle
    :param screen: The pygame.Surface of the window
    """

    # Left Border
    if player.rect.x <= 0.0:
        player.rect.x = 0.0
        return

    # Right Border
    window_width = screen.get_width()
    if (player.rect.x + player.rect.w) >= window_width:
        player.rect.x = window_width - player.rect.w


def ball_wall_collisions(ball: Ball, screen: pygame.Surface) -> None:
    """
    Wall collisions of the Ball
    :param ball: The Ball to check collisions on
    :param screen: The pygame.Surface of the window
    """

    window_width = screen.get_width()

    # Left & Right border
    if (ball.position.x - ball.radius) <= 0.0 or (ball.position.x + ball.radius) >= window_width:
        ball.speed.x = -ball.speed.x

    # Right border
    if (ball.position.y - ball.radius) <= 0.0:
        ball.speed.y = -ball.speed.y


def ball_paddle_collisions(ball: Ball, paddle: PlayerPaddle) -> None:
    """
    Collisions of the Ball with the PlayerPaddle
    :param ball: The Ball to check collisions against
    :param paddle: The PlayerPaddle to check collisions on
    """

    if paddle.rect.colliderect(pygame.rect.Rect(ball.position.x, ball.position.y, ball.radius, ball.radius)):
        ball.position.y -= ball.radius / 2
        ball.speed.y = -ball.speed.y


def draw_fps(fps: float, game_state: GameState, screen: pygame.Surface) -> None:
    """
    Draw the games fps in the top left corner
    :param fps: Frames per Second
    :param game_state: The games current GameState
    :param screen: The pygame.Surface of the window
    """

    fps_text_rect = game_state.text_font.render(str(fps), True, FPS_TEXT_COLOR)
    screen.blit(fps_text_rect, (0, 0))


def draw(game_state: GameState, screen: pygame.Surface) -> None:
    """
    Draw everything in the game
    :param screen: The pygame.Surface of the window
    :param game_state: The current GameState
    """

    # draw fps
    draw_fps("{:.2f}".format(1000/game_state.delta_time), game_state, screen)

    # draw player
    game_state.player.draw(screen)

    # draw ball
    game_state.ball.draw(screen)


def update(game_state: GameState, screen: pygame.Surface) -> None:
    """
    Update everything in the game
    :param screen: The pygame.Surface of the window
    :param game_state: The current GameState
    """

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
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
    ball_wall_collisions(game_state.ball, screen)
    ball_paddle_collisions(game_state.ball, game_state.player)

    # draw game
    draw(game_state, screen)

    pygame.display.update()


if __name__ == "__main__":
    screen, game_state = setup()

    # Game loop
    while True:
        game_state.delta_time = game_state.clock.tick(TARGET_UPS)
        update(game_state, screen)
