# problem : Compute the greatest common divisor (GCD) of two positive integers
from functools import reduce
from math import gcd as _gcd
import math

# way one
num1 = 60
num2 = 24

n = num1
n2 = num2

while n2 != 0:
    temp = n % n2
    n1 = n2
    n2 = temp

print("GCD = ", n1)


# way two
print(math.gcd(num1, num2))


# way three
def GCD_NUM(n1, n2):
    while n2:
        temp = n1 % n2
        n1, n2 = n2, temp

    return n1


print(GCD_NUM(60, 48))


# Way Four
def gcd(numbers):
    return reduce(_gcd, numbers)


nums = [24, 30, 36]
print(gcd(nums))
