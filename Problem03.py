"""
Problem:
    Read 2 variables, named A and B and make the Swap of these two variables.
Input
    The input file will contain 2 integer numbers.
Output
    Print the the swap two variable.
"""
A = int(input())
B = int(input())
temp = 0
temp = A
A = B
B = temp
print(f"A = {A}")
print(f"B = {B}")

