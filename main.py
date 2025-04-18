from map import Map
from snake import Snake
from eat import Eat
from stone import Stone
from snake_head import SnakeHead
from snake_body import SnakeBody


def start_console():
    map = Map()
    snake = Snake("Snake1")
    map.add_snake(snake)
    map.add_new_eat()
    map.show()

    while True:
        com = input()
        if com == "q":
            break
        elif com == "s":
            result = snake.move("left")
        elif com == "f":
            result = snake.move("right")
        elif com == "e":
            result = snake.move("up")
        elif com == "d":
            result = snake.move("down")
        else:
            result = snake.move()

        if result is not None:
            map.show()
        else:
            return


def start_gui():
    import pygame

    MAP_WIDTH = 10
    MAP_HEIGHT = 10

    map = Map(MAP_WIDTH, MAP_HEIGHT)
    snake = Snake("Snake1")
    map.add_snake(snake)
    map.add_new_eat()
    map.show()

    BLOCK_SIZE = 20
    SCREEN_WIDTH = MAP_WIDTH * BLOCK_SIZE
    SCREEN_HEIGHT = MAP_HEIGHT * BLOCK_SIZE
    FPS = 60
    GAME_SPEED = 500

    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    WHITE = (255, 255, 255)

    # GAME_STATE_FILENAME = "game_state"

    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()
    TIMEREVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(TIMEREVENT, GAME_SPEED)


    def update_screen():
        screen.fill(BLACK)
        x = 0
        y = 0
        for h in range(MAP_HEIGHT):
            for w in range(MAP_WIDTH):
                content = map.map[h][w].content
                if content is not None:
                    if isinstance(content, Stone):
                        pygame.draw.rect(screen, RED, pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE))
                    elif isinstance(content, Eat):
                        pygame.draw.rect(screen, GREEN, pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE))
                    elif isinstance(content, SnakeHead):
                        pygame.draw.rect(screen, WHITE, pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE))
                    elif isinstance(content, SnakeBody):
                        pygame.draw.rect(screen, BLUE, pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE))

                x += BLOCK_SIZE
            x = 0
            y += BLOCK_SIZE
        pygame.display.update()


    running = True
    is_need_update_screen = True
    new_dir = None

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                is_need_update_screen = True

            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LEFT]:
                new_dir = "left"
            elif pressed[pygame.K_RIGHT]:
                new_dir = "right"
            elif pressed[pygame.K_UP]:
                new_dir = "up"
            elif pressed[pygame.K_DOWN]:
                new_dir = "down"
            elif pressed[pygame.K_q]:
                running = False

            if event.type == TIMEREVENT:
                moving_result = snake.move(new_dir)
                if moving_result is None:
                    running = False

                is_need_update_screen = True

        if is_need_update_screen:
            update_screen()
            is_need_update_screen = False

        clock.tick(FPS)
    pygame.quit()


def main():
    cmd = input("Select version please (1 - console, 2 - gui): ")
    # cmd = "2"
    if cmd == "1":
        start_console()
    elif cmd == "2":
        start_gui()
    else:
        print("Unknown command!")


if __name__ == "__main__":
    main()
