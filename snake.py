from snake_element import SnakeElement
from snake_head import SnakeHead
from snake_body import SnakeBody
from eat import Eat
from stone import Stone


class Snake:
    def __init__(self, name):
        self.name = name
        self.map_link = None
        self.elements = []
        self.head = None
        self._add_element(x=0, y=0)

        
    def _add_element(self, y, x):
        new_el = SnakeElement(SnakeHead(), x=x, y=y)
        self.elements.insert(0, new_el)
        if self.map_link is not None:
            self.map_link.map[new_el.y][new_el.x].content = new_el.type
        if len(self.elements) > 1:
            self.elements[1].type = SnakeBody()
            self.map_link.map[self.elements[1].y][self.elements[1].x].content = self.elements[1].type
        self.head = self.elements[0]
        
        
    def move(self, new_dir):
        dirs = {
            "right": (0, 1),
            "down": (1, 0),
            "left": (0, -1),
            "up": (-1, 0),
        }
        
        print(new_dir)
        prev_y = self.head.y
        prev_x = self.head.x
        new_y = prev_y + dirs[new_dir][0]
        map = self.map_link.map
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
        for el in self.elements:
            if (new_y == el.y) and (new_x == el.x):
                print("collapse!")
                # self.map_link.show()
                return

        # наткнулись на еду)
        if isinstance(map[new_y][new_x].content, Eat):
            self._add_element(new_y, new_x)
            print("eat! new len:", len(self.elements))
            # self.map_link.show()
            return
        
        self.head.y = new_y
        self.head.x = new_x
        self.map_link.map[prev_y][prev_x].content = None
        self.map_link.map[new_y][new_x].content = self.head.type
        
        for i in range(1, len(self.elements)):
            cur_y = self.elements[i].y
            cur_x = self.elements[i].x
            self.map_link.map[cur_y][cur_x].content = None
            self.elements[i].y = prev_y
            self.elements[i].x = prev_x
            self.map_link.map[prev_y][prev_x].content = self.elements[i].type
            prev_y = cur_y
            prev_x = cur_x

        # self.map_link.show()

