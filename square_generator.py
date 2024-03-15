import math

class SquareGenerator:
    def e_squares(self, start, end):
        if start < end + 1:
            squares = [math.pow(x, 2) for x in range(start, end + 1)]
            return squares
        else:
            return "Start cannot be smaller than end"
