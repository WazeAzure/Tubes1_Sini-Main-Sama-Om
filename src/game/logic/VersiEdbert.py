
from typing import Optional, Tuple

from game.logic.base import BaseLogic
from game.models import GameObject, Board, Position
from ..util import get_direction

import time


class EdBot(BaseLogic):
    '''
        Types of Game Objects
        - TeleportGameObject
        - DiamondGameObject
        - BaseGameObject
        - DiamondButtonGameObject / RESET BUTTON
        - BotGameObject
        - 
    '''
    def __init__(self) -> None:
        self.goal_position: list[int, int] = None
        self.current_position: Optional[Position] = None
        self.current_direction = 0
        self.diamond_list = []
        self.base: Optional[Position] = None
        self.diamond_target: Optional[Position] = None
        self.init = False
        self.enemy_bots = []
        self.teleporter = []
        self.reset_button: list[GameObject] = []

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
        '''
        Get distance of 2 position
        '''
        dist_x = abs(a.x - b.x)
        dist_y = abs(a.y - b.y)
        dist = dist_x + dist_y
        return dist

    def get_distance_teleporter(self, a: Position, b: Position) -> int:
        '''
        Get distance relative to teleporter
        '''
        dist_x = abs(a.x - self.teleporter[0][1].x) + abs(self.teleporter[1][1].x - a.x)
        dist_y = abs(a.y - self.teleporter[0][1].y) + abs(self.teleporter[1][1].y - a.y)
        dist = dist_x + dist_y
        return dist

    def closest_diamond(self, x: GameObject):
        '''
        Count distance of closest diamonds
        '''
        dist = self.get_distance(self.current_position, x.position)
        dist2 = self.get_distance_teleporter(self.current_position, x.position)
        if(min(dist, dist2) == dist2):
            return [x.id, x.position, x.properties.points, dist, True]
        return [x.id, x.position, x.properties.points, dist, False]

    def handle_diamonds(self, board_bot: GameObject, board: Board):
        self.diamond_list = [[x.id, x.position, x.properties.points, 0, None] for x in board.diamonds]

        self.diamond_list = list(map(self.closest_diamond, board.diamonds))

        def func(e):
            return e[3]
        self.diamond_list.sort(key=func)
    
    def time_to_base(self, board_bot: GameObject):
        print(self.get_distance(self.current_position, self.base))
        print(board_bot.properties.milliseconds_left)
        if self.get_distance(self.current_position, self.base)+2.5 >= (board_bot.properties.milliseconds_left // 1000):
            return True
        return False
    
    def set_enemy_info(self, board_bot: GameObject, board: Board):
        self.enemy_bots = []
        for x in board.bots:
            if x.id != board_bot.id:
                self.enemy_bots.append([x.id, x.position, x.properties.diamonds])
    
    def set_info(self, board_bot: GameObject, board: Board) -> None:
        self.teleporter = []
        for x in board.game_objects:
            if x.type == "TeleportGameObject":
                dist = self.get_distance(self.current_position, x.position)
                self.teleporter.append([x.id, x.position, x.properties.pair_id, dist])
            elif x.type == "DiamondButtonGameObject":
                self.reset_button.append(x)
            
        # sort teleporter
        def func(e):
            return e[3]
        self.teleporter.sort(key=func)
    
    def next_move(self, board_bot: GameObject, board: Board) -> Tuple[int, int]:
        start_time = time.time()
        # initialize var on run time
        if not self.init:
            self.base = board_bot.properties.base
            self.init = True

        # get current location
        self.current_position = board_bot.position

        # set info teleporter and reset button
        self.set_info(board_bot, board)

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
            if(self.current_position.x + self.goal_position[0] == self.teleporter[0][1].x):
                self.goal_position[0] = 0
                self.goal_position[1] = 1
            elif(self.current_position.y + self.goal_position[1] == self.teleporter[0][1].y):
                self.goal_position[0] = 1
                self.goal_position[1] = 0


        # if inventory full return to base
        elif board_bot.properties.diamonds == 5:
            print("INVENTORY FULL")
            self.goal_position = get_direction(
                self.current_position.x, 
                self.current_position.y, 
                self.base.x, 
                self.base.y
            )

        # take diamonds
        else:
            print("TAKE DIAMOND")
            if (board_bot.properties.diamonds == 4 and self.diamond_list[0][2] == 2) : # minor fix supaya bot ga invalid maksa makan diamond merah
                self.diamond_target = self.diamond_list[1][1]
            else :
                if(self.diamond_list[0][4]):
                    self.diamond_target = self.teleporter[0][1]
                else:
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

