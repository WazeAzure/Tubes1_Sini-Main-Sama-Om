
from typing import Optional, Tuple

from game.logic.base import BaseLogic
from game.models import GameObject, Board, Position
from ..util import get_direction

import time


class VanBot(BaseLogic):
    '''
        Types of Game Objects
        - TeleportGameObject
        - DiamondGameObject
        - BaseGameObject
        - DiamondButtonGameObject
        - BotGameObject
    '''
    def __init__(self) -> None:
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.my_attribute = 0
        self.goal_position = None
        self.current_position: Optional[Position] = None
        self.current_direction = 0
        self.diamond_list = []
        self.base: Optional[Position] = None
        self.diamond_target: Optional[Position] = None
        self.init = False

    def details(self, board_bot: GameObject, board: Board):
        properties = board_bot.properties
        print(properties.score)
        print(board_bot.properties)
        print(board_bot.position)
        for x in board.diamonds:
            print(x)
        
        print()
        for x in board.bots:
            print(x)
        # print(GameObject.properties.base)
    
    def get_distance(self, a: Position, b: Position):
        dist_x = abs(a.x - b.x)
        dist_y = abs(a.y - b.y)
        dist = dist_x + dist_y
        return dist
    
    def closest_diamond(self, x: GameObject):
        dist_x = abs(self.current_position.x - x.position.x)
        dist_y = abs(self.current_position.y - x.position.y)

        dist = self.get_distance(self.current_position, x.position)
        return [x.id, x.position, x.properties.points, dist]

    def handle_diamonds(self, board_bot: GameObject, board: Board):
        self.diamond_list = [[x.id, x.position, x.properties.points, 0] for x in board.diamonds]

        self.diamond_list = list(map(self.closest_diamond, board.diamonds))

        def func(e):
            return e[3]
        self.diamond_list.sort(key=func)
    
    def time_to_base(self, board_bot: GameObject):
        print(self.get_distance(self.current_position, self.base))
        print(board_bot.properties.milliseconds_left)
        if self.get_distance(self.current_position, self.base) >= (board_bot.properties.milliseconds_left // 1000):
            return True
        return False

    def next_move(self, board_bot: GameObject, board: Board) -> Tuple[int, int]:
        
        print(board.game_objects)
        start_time = time.time()
        # initialize var on run time
        if not self.init:
            self.base = board_bot.properties.base
            self.init = True

        # get current location
        self.current_position = board_bot.position

        # get diamonds location
        self.handle_diamonds(board_bot, board)

        if self.time_to_base(board_bot):
            print("TIME TO GO HOME")
            self.goal_position = get_direction(
                self.current_position.x, 
                self.current_position.y, 
                self.base.x, 
                self.base.y
            )

        # if inventory full return to base
        elif board_bot.properties.diamonds == 5:
            print("INVENTORY FULL")
            self.goal_position = get_direction(
                self.current_position.x, 
                self.current_position.y, 
                self.base.x, 
                self.base.y
            )
        else:
            print("TAKE DIAMOND")
            if (board_bot.properties.diamonds == 4) : # minor fix supaya bot ga invalid maksa makan diamond merah
                self.diamond_target = self.diamond_list[1][1]
            else :
                self.diamond_target = self.diamond_list[0][1]
            self.goal_position = get_direction(
                self.current_position.x,
                self.current_position.y,
                self.diamond_target.x,
                self.diamond_target.y
            )
        end_time = time.time()
        print("elapsed: ", end_time-start_time)
        return self.goal_position[0], self.goal_position[1]
    
    def getAllBots(self):
        print(dir(Board))

