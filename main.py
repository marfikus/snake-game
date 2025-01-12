from map import Map
from snake import Snake
from eat import Eat
from stone import Stone


map = Map()
map.map[0][1].content = Eat()
map.map[0][3].content = Eat()
map.map[5][5].content = Eat()
map.map[7][1].content = Eat()
map.map[7][9].content = Eat()

snake = Snake("Snake1")
map.add_snake(snake)
map.show()

snake.move("down")
snake.move("down")
snake.move("down")
snake.move("down")
snake.move("down")
snake.move("down")
snake.move("down")
snake.move("right")
snake.move("right")
snake.move("right")
snake.move("right")
snake.move("right")
snake.move("up")
snake.move("up")
snake.move("up")
snake.move("left")
snake.move("left")
snake.move("up")
snake.move("up")
snake.move("up")
snake.move("up")
snake.move("up")

