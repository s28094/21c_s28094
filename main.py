# Task 1

squares = [x ** 2 for x in range(1, 11)]
print(squares)

# Task 2

def e_squares(start, end):
    squares = [x**2 for x in range(start, end + 1)]
    return squares

start = 1
end = 10
result = e_squares(start, end)
print(result)
