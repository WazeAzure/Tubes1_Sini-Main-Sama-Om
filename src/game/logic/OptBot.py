from typing import Optional, Tuple

from game.logic.base import BaseLogic
from game.models import GameObject, Board, Position
from ..util import get_direction

import time

class OptBot:
    def __init__(self):
        self.init = False
        '''
        variable just to run once in game loop.
        '''
        self.current_position: Optional[Position] = None
        '''
        our bot current position `Position(x, y) - object`
        '''
        self.base_position: Optional[Position] = None
        '''
        our bot base position `Position(x, y) - object`
        '''
        self.enemy_bots: Tuple[list[GameObject], int] = []
        '''
        list of enemy bots metadata
        '''
        self.teleporter: list[Position] = []
        '''
        list of teleporter position `[Position(x, y), ...] - object`
        '''
        self.list_objective = []
        '''
        list of diamonds and reset buttons.
        
        structure `[[Position(x, y), points, priority], ...]`
        '''
        self.target_position: Optional[Position] = None
        '''
        target position. object `Position(x, y)`
        '''

    def set_current_position(self, board_bot: GameObject) -> None:
        """
        set current position every iteration.
        """
        self.current_position = board_bot.position
    
    def set_info_once(self, board_bot: GameObject) -> None:
        """
        set information only once such as:
        - base position
        """
        if not self.init:
            self.base_position = board_bot.properties.base
            self.init = True

    def set_teleporter(self, board: Board) -> None:
        """
        set teleporter locations
        """
        self.teleporter = [x.position for x in board.game_objects if x.type == "TeleportGameObject"]

        def func(x):
            """sort teleporter by closest distance to current_position"""
            return self.get_distance(self.current_position, x)
        self.teleporter.sort(key=func)
    
    def get_distance(self, a: Position, b: Position) -> int:
        """
        get distance between 2 position

        return:
        - distance: `int`
        """
        dist_x = abs(a.x - b.x)
        dist_y = abs(a.y - b.y)
        dist = dist_x + dist_y
        return dist
    
    def get_distance_teleporter(self, a: Position, b: Position) -> int:
        """
        get distance between 2 position account teleporter to SELF
        """
        return self.get_distance(a, self.teleporter[0]) + self.get_distance(self.teleporter[1], b)

    def set_priority(self, obj) -> None:
        """
        set priorities for objectives.

        obj structure `[[Position(x, y), points, priority], ...]`
        """
        obj[2] = min(
            self.get_distance(self.current_position, obj[0]),
            self.get_distance_teleporter(self.current_position, obj[0])
        )

        return obj

    def set_list_objective(self, board: Board) -> None:
        """
        set list objectives location and points. such as:
        - diamonds
        - reset button
        """
        # add all diamonds
        temp_objective = [[x.position, x.properties.points, 0]for x in board.diamonds]
        # add all reset buttons
        reset_button = [[x.position, 0.75, 0] for x in board.game_objects if x.type == "DiamondButtonGameObject"]
        temp_objective.append(reset_button[0])

        self.list_objective = list(map(self.set_priority, temp_objective))

        # sort by priority
        def func(e):
            """sort list_objective by 2nd key - priority"""
            return e[2]
        self.list_objective.sort(key=func)

    def go_to_destination(self) -> None:
        """"
        go to destination
        """
        dist_normal = self.get_distance(self.current_position, self.target_position)
        dist_teleporter = self.get_distance_teleporter(self.current_position, self.target_position)

        if(dist_teleporter < dist_normal):
            # get closest teleporter
            self.target_position = self.teleporter[0]
        

    def next_move(self, board_bot: GameObject, board: Board) -> Tuple[int, int]:
        '''
        default function *main game loop*!
        '''
        time_start = time.time()

        # init once
        self.set_info_once(board_bot)

        # info setup
        self.set_current_position(board_bot)
        self.set_teleporter(board)
        self.set_list_objective(board)

        # set destination
        if (board_bot.properties.diamonds == 5):
            self.target_position = self.base_position
        else:
            if(board_bot.properties.diamonds + self.list_objective[0][1] > board_bot.properties.inventory_size):
                self.list_objective.pop(0)
            self.target_position = self.list_objective[0][0]

        # get position
        self.go_to_destination()

        # get direction
        direction = get_direction(
            self.current_position.x,
            self.current_position.y,
            self.target_position.x,
            self.target_position.y
        )

        time_end = time.time()
        print("Elapsed Time:", time_end - time_start)

        return direction[0], direction[1]
