# problem : Write a Python program to add two objects if both objects are an integer type

def add_numbers(a, b):
    if not isinstance(a, int) and isinstance(b, int):
        return "Input must be integer number"
    else:
        return a + b

print(add_numbers(20, "sdf")) # Error
print(add_numbers(20, 4)) # success