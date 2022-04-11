"""
problem: Write a Python program that will return true if the two given integer values are equal or their sum or
difference is 5
"""


def test_number(num1, num2):
    minusResult = num1 - num2
    addResult = num1 + num2

    if num1 == num2 or addResult == 5 or abs(minusResult) == 5:
        return True
    else:
        return False


print(test_number(7, 2))
print(test_number(3, 2))
print(test_number(53, 27))
