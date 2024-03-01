
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
        self.enemy_bots = []
        self.ijin_tackle = True #true itu boleh tackle
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
        dist_x = abs(a.x - b.x)
        dist_y = abs(a.y - b.y)
        dist = dist_x + dist_y
        return dist
    
    def closest_diamond(self, x: GameObject):
        dist_x = abs(self.current_position.x - x.position.x)
        dist_y = abs(self.current_position.y - x.position.y)

        dist = self.get_distance(self.current_position, x.position)

        if (x.properties.points == 2) : # WEIGH : membuat diamond merah berprioritas lebih tinggi
            dist /= 2
        elif (x.properties.points == 0.75) :
            dist /= 0.75
        return [x.id, x.position, x.properties.points, dist]

    def handle_diamonds(self, board_bot: GameObject, board: Board):
        # self.diamond_list = [[x.id, x.position, x.properties.points, 0] for x in board.diamonds]
        # self.diamond_list.append(self.reset_button[0].id, self.reset_button[0].position, 0.75, 0)
        self.reset_button[0].properties.points = 0.75

        self.diamond_list = list(map(self.closest_diamond, board.diamonds))
        self.diamond_list.append(self.closest_diamond(self.reset_button[0]))
        
        # sorting closest
        def func(e):
            return e[3]
        self.diamond_list.sort(key=func)
    
    def time_to_base(self, board_bot: GameObject):
        print(self.get_distance(self.current_position, self.base))
        print(board_bot.properties.milliseconds_left)
        if self.get_distance(self.current_position, self.base)+1 >= (board_bot.properties.milliseconds_left // 1000) // 1.1:
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
                self.teleporter.append([x.id, x.position, x.properties.pair_id, 0])
            elif x.type == "DiamondButtonGameObject":
                self.reset_button.append(x)

    def tackle(self, board_bot: GameObject, board: Board) -> Tuple [int, Position] : #0 itu aman, 1 itu passive tackle, 2 itu diam
        jarak = [0 for i in range(len(self.enemy_bots))]
        for i, x in enumerate (self.enemy_bots) :
            jarak[i] = self.get_distance(self.current_position, x[1])
            if (jarak[i] == 1) :
                return 1, x[1]
        for i in range(len(jarak)) :
            if (jarak[i] == 2) :
                return 2, self.current_position
        return 0, self.current_position
    
    def next_move(self, board_bot: GameObject, board: Board) -> Tuple[int, int]:
        start_time = time.time()
        # initialize var on run time
        if not self.init:
            self.base = board_bot.properties.base
            self.init = True

        # set enemies location
        self.set_enemy_info(board_bot, board)

        # get current location
        self.current_position = board_bot.position

        # set teleporter and reset location
        self.set_info(board_bot, board)

        # get diamonds location
        self.handle_diamonds(board_bot, board)
        
        tackle = self.tackle(board_bot, board)
        print("tackle =", tackle[0])
        if (tackle[0] == 1 and self.ijin_tackle) :
            print("TACKLE")
            self.ijin_tackle = False
            self.goal_position = get_direction(
                    self.current_position.x, 
                    self.current_position.y, 
                    tackle[1].x, 
                    tackle[1].y
                )
        elif (tackle[0] == 2 and self.ijin_tackle) :
            print("DIAM")
            self.goal_position = get_direction(
                    self.current_position.x, 
                    self.current_position.y, 
                    self.current_position.x, 
                    self.current_position.y
                )
        else :
            self.ijin_tackle = True
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
                print(self.diamond_target)

                self.tackle(board_bot, board)
                if (board_bot.properties.diamonds == 4 and self.diamond_list[0][2] == 2) : # minor fix supaya bot ga invalid maksa makan diamond merah
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

