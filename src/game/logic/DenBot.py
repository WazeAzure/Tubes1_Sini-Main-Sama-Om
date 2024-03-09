from game.logic.OptBot import OptBot
from typing import Optional, Tuple

from game.logic.base import BaseLogic
from game.models import GameObject, Board, Position
from ..util import get_direction

import time

class DenBot(OptBot) :
    def __init__(self):
        super().__init__()

    def set_priority(self, obj) -> None:
        """
        set priorities for objectives.

        obj structure `[Position(x, y), points, priority]`
        """
        distance = min(
            self.get_distance(self.current_position, obj[0]),
            self.get_distance_teleporter(self.current_position, obj[0])
        )

        obj[2] = distance / obj[1]

        return obj
    
    def get_distance_teleporter(self, a: Position, b: Position) -> int:
        """
        get distance between 2 position account teleporter to SELF
        """
        return min(
            self.get_distance(a, self.teleporter[0][0]) + self.get_distance(self.teleporter[1][0], b), 
            self.get_distance(a,self.teleporter[1][0]) + self.get_distance(self.teleporter[0][0],b)
            )
    
    def set_priority_relativeBase(self, obj) -> None:
        """
        set priorities for objectives.

        obj structure `[Position(x, y), points, priority]`
        """
        distance = min(
            self.get_distance(self.current_position, obj[0]) + self.get_distance_teleporter(obj[0], self.base_position),
            self.get_distance(self.current_position, obj[0]) + self.get_distance(obj[0], self.base_position),
            self.get_distance_teleporter(self.current_position, obj[0]) + self.get_distance(obj[0], self.base_position),
            self.get_distance_teleporter(self.current_position, obj[0]) + self.get_distance_teleporter(obj[0], self.base_position)      
        )

        obj[2] = distance / obj[1]

        return obj