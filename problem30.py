# problem : Sum of three given integers. However, if two values are equal sum will be zero
def sum_of_three_numbers(num1, num2, num3):

    if num1 == num2 or num1 == num3 or num2 == num3:
        return 0
    else:
        return num1 + num2 + num3


print(sum_of_three_numbers(2, 5, 4))
print(sum_of_three_numbers(2, 5, 2))