# problem : Sum of two given integers. However, if the sum is between 15 to 20 it will return 20
x = int(input("Enter First number :"))
y = int(input("Enter Second number :"))

# way one
def sum_of_two_numbers(num1, num2):
    result = num1 + num2
    if 15 <= result <= 20:
        return 20
    else:
        return result


#way two
def sum_of_two_numbers(num1, num2):
    result = num1 + num2
    if result in range(15, 20):
        return 20
    else:
        return result


print(sum_of_two_numbers(x, y))