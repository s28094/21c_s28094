import math
import square_generator
"""
# Task 1

squares = [x ** 2 for x in range(1, 11)]
print(squares)
"""
# Task 2
"""
def e_squares(start, end):
    squares = [x**2 for x in range(start, end + 1)]
    return squares

start = 1
end = 10
result = e_squares(start, end)
print(result)
"""
# Task 3
"""
class SquareGenerator:
    def e_squares(self, start, end):
        squares = [x ** 2 for x in range(start, end + 1)]
        return squares


start_num = 1
end_num = 10
squares_list = SquareGenerator().e_squares(start_num, end_num)
print(squares_list)
"""
# Task 4
"""

class SquareGenerator:
    def e_squares(self, start, end):
        squares = [math.pow(x, 2) for x in range(start, end + 1)]
        return squares


start_num = 1
end_num = 10
squares_list = SquareGenerator().e_squares(start_num, end_num)
print(squares_list)
"""

# Task 5
"""

class SquareGenerator:
    def e_squares(self, start, end):
        if start < end + 1:
            squares = [math.pow(x, 2) for x in range(start, end + 1)]
            return squares
        else:
            return "Start cannot be smaller than end"


start_num = 10
end_num = 10
squares_list = SquareGenerator().e_squares(start_num, end_num)
print(squares_list)
"""

# Task 6
"""
start_num = 10
end_num = 10
squares_list = square_generator.SquareGenerator().e_squares(start_num, end_num)
print(squares_list)
"""
# Task 7
"""
start_num = 10
end_num = 10
squares_list = square_generator.SquareGenerator().e_squares(start_num, end_num)
print(squares_list)
"""
# Task 8
"""
start_num = 10
end_num = 10
squares_list = square_generator.SquareGenerator().e_squares(start_num, end_num)
print(squares_list)

start_num = 10
end_num = 10
cubic_list = square_generator.CubicGenerator().e_cubes(start_num, end_num)
print(cubic_list)
"""
# Task 9
"""
start_num = 10
end_num = 10
squares_list = square_generator.SquareGenerator().e_squares(start_num, end_num)
print(squares_list)

start_num = 10
end_num = 10
cubic_list = square_generator.CubicGenerator().e_cubes(start_num, end_num)
print(cubic_list)

start_num = 10
end_num = 8
cubic_list = square_generator.CubicGenerator().e_squares(start_num, end_num)
print(cubic_list)
"""
# Task 10

# commented because e_squares is an abstract method

# start_num = 10
# end_num = 10
# squares_list = square_generator.SquareGenerator().e_squares(start_num, end_num)
# print(squares_list)

start_num = 9
end_num = 10
cubic_list = square_generator.CubicGenerator().e_cubes(start_num, end_num)
print(cubic_list)

start_num = 9
end_num = 10
cubic_list = square_generator.CubicGenerator().e_squares(start_num, end_num)
print(cubic_list)