import math
from abc import (ABC, abstractmethod)

class SquareGenerator(ABC):
    @abstractmethod
    def e_squares(self, start, end):
        if start < end + 1:
            squares = [math.pow(x, 2) for x in range(start, end + 1)]
            return squares
        else:
            return "Start cannot be smaller than end"


class CubicGenerator(SquareGenerator):
    def e_cubes(self, start, end):
        if start < end + 1:
            squares = [math.pow(x, 3) for x in range(start, end + 1)]
            return squares
        else:
            return "Start cannot be smaller than end"

    def e_squares(self, start, end):
        if start < end + 1:
            squares = [math.pow(x, 2) for x in range(start, end + 1)]
            return squares
        else:
            return "Start cannot be smaller than end_v2"