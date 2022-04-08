# problem: Get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference

def number_difference(n):
    if n > 17:
        return abs((17 - n) * 2)
    else:
        return 17 - n


print(number_difference(24))
print(number_difference(15))
