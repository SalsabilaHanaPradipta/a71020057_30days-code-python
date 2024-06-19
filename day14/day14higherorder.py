def apply_function(func, value):
    return func(value)

def square(x):
    return x * x

def cube(x):
    return x * x * x

print(apply_function(square, 5))  
print(apply_function(cube, 3))    

numbers = [1, 2, 3, 4]
squared_numbers = map(square, numbers)
print(list(squared_numbers))  