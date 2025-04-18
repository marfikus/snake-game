from cell import Cell
# from snake_element import SnakeElement
from snake_head import SnakeHead
from snake_body import SnakeBody
from eat import Eat
from stone import Stone

import random


class Map:
    def __init__(self, w=10, h=10):
        self.width = w
        self.height = h
        self.map = [[Cell() for _ in range(self.width)] for _ in range(self.height)]
        self.snake = None


    def show(self):
        border = " " + "-=-" * len(self.map[0])
        print(border)
        for y in range(self.height):
            print("|", end="")
            num_line = " "
            for x in range(self.width):
                num_line += f" {x} "
                content = self.map[y][x].content
                if content is None:
                    print("   ", end="")
                elif isinstance(content, Stone):
                    print(" s ", end="")
                elif isinstance(content, Eat):
                    print(" e ", end="")
                elif isinstance(content, SnakeHead):
                    print(" h ", end="")
                elif isinstance(content, SnakeBody):
                    print(" b ", end="")
            print("|", y)
        print(border)
        print(num_line)


    def add_snake(self, s):
        if self.snake is not None:
            return
        
        self.snake = s
        for el in s.elements:
            # по идее надо проверять координаты на карте перед добавлением...
            self.map[el.y][el.x].content = el.type
            
        s.map_link = self
        
        
    def remove_snake(self, s):
        if s == self.snake:
            s.map_link = None
            self.snake = None
            for el in s.elements:
                self.map[el.y][el.x].content = None


    def add_new_eat(self):
        while True:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if self.map[y][x].content is None:
                self.map[y][x].content = Eat()
                break
                
                
    # def add_stone, eat... remove...