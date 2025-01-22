from map import Map
from snake import Snake
from eat import Eat
from stone import Stone


def main():
    map = Map()
    map.map[0][1].content = Eat()
    map.map[0][3].content = Eat()
    map.map[2][7].content = Eat()
    map.map[5][5].content = Eat()
    map.map[7][1].content = Eat()
    map.map[7][9].content = Eat()
    map.map[9][6].content = Eat()

    snake = Snake("Snake1")
    map.add_snake(snake)
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
        # map.show()
        # if result == False:
            # break


if __name__ == "__main__":
    main()
