from game.logic.OptBot import OptBot

class DenBot(OptBot) :
    def __init__(self):
        super().__init__()

    def set_priority(self, obj) -> None:
        """
        set priorities for objectives.

        obj structure `[[Position(x, y), points, priority], ...]`
        """
        distance = min(
            self.get_distance(self.current_position, obj[0]),
            self.get_distance_teleporter(self.current_position, obj[0])
        )

        obj[2] = distance / obj[1]

        return obj