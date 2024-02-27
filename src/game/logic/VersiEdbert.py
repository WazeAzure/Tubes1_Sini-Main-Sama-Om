
from typing import Optional, Tuple

from game.logic.base import BaseLogic
from game.models import GameObject, Board, Position
from ..util import get_direction



class EdBot(BaseLogic):
    def __init__(self) -> None:
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.my_attribute = 0
        self.goal_position: Optional[Position] = None
        self.current_direction = 0
    
    def next_move(self, board_bot: GameObject, board: Board) -> Tuple[int, int]:
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
        return 1, 0
    
    def getAllBots(self):
        print(dir(Board))
    

    
