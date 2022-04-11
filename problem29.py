# problem: Least common multiple (LCM) of two positive integers


# way one
num1 = 15
num2 = 17

n1 = num1
n2 = num2

while n2 != 0:
    temp = n1 % n2
    n1 = n2
    n2 = temp

lcm = num1 * num2 // n1
print(lcm)


# way two
def lcm(x, y):
    if x > y:
        z = x
    else:
        z = y
    while True:
        if (z % x == 0) and (z % y == 0):
            lcm = z
            break

        z += 1
    return lcm


print(lcm(4, 6))
