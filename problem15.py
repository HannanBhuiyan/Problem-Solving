# problem: Calculate the sum of three given numbers, if the values are equal then return thrice of their sum

def sum_of_number(num1, num2, num3):

       if num1 == num2 == num3:
           result = (num1 + num2 + num3) * 3
       else:
          result = num1 + num2 + num3

       return result

print(sum_of_number(2, 2, 2))