
def create_map(strings, columns, cell_symbol):
    return [[cell_symbol for _ in range(columns)] for _ in range(strings)]


def print_map():
    border = "=" * len(map[0]) * 3
    print(border)
    for string in map:
        # print(string)
        for cell in string:
            if cell == 0:
                print(" ", end="")
            else:
                print(cell, end="")
        print()
    print(border)


def move(new_dir):    
    print(new_dir)
    prev_y = snake[0][0]
    prev_x = snake[0][1]
    new_y = prev_y + dirs[new_dir][0]
    # если дошли до границы карты, то выходим с другой стороны
    if new_y < 0:
        new_y = len(map) - 1
    elif new_y == len(map):
        new_y = 0
    new_x = prev_x + dirs[new_dir][1]
    if new_x < 0:
        new_x = len(map[0]) - 1
    elif new_x == len(map[0]):
        new_x = 0
        
    # проверка на столконовение с собой и противоход
    if [new_y, new_x] in snake:
        print("collapse!")
        print_map()
        return
    
    # наткнулись на еду)
    if map[new_y][new_x] == 1:
        snake.insert(0, [new_y, new_x])
        print("eat! new len:", len(snake))
        print_map()
        return
        
    snake[0][0] = new_y
    snake[0][1] = new_x
    map[prev_y][prev_x] = 0
    map[new_y][new_x] = 1
    
    for i in range(1, len(snake)):
        cur_y = snake[i][0]
        cur_x = snake[i][1]
        map[cur_y][cur_x] = 0
        snake[i][0] = prev_y
        snake[i][1] = prev_x
        map[prev_y][prev_x] = 1
        prev_y = cur_y
        prev_x = cur_x
    
    print_map()


# map = create_map(10, 8, 0)
map = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
]

dir = "right"
dirs = {
    "right": (0, 1),
    "down": (1, 0),
    "left": (0, -1),
    "up": (-1, 0),
}

# координаты змейки на карте, голова - нулевой элемент
snake = [
    [1, 2],
    [0, 2],
    [0, 1],
    [0, 0],
]
for cell in snake:
    map[cell[0]][cell[1]] = 1

print_map()
move("right")
move("right")
move("right")
move("right")
move("right")
move("right")
move("right")
move("right")
# move("left")
move("down")
move("down")
move("down")
move("down")
move("down")
move("down")
move("down")
# move("down")
# move("left")
# move("up")
move("right")
move("right")
# move("up")
# move("up")
# move("up")
# move("up")
# move("up")
# move("up")
# move("right")
# move("right")
# move("right")
# move("right")
# move("right")
# move("right")
move("down")
move("down")
move("down")
move("down")
move("down")
move("down")
move("down")
move("down")
move("down")
move("down")


        
