"""
Problem:
    Read 2 variables, named A and B and make the sum of these two variables, assigning its result to the variable X. Print X as shown below. Print endline after the result otherwise you will get “Presentation Error”.

Input
    The input file will contain 2 integer numbers.

Output
    Print the letter X (uppercase) with a blank space before and after the equal signal followed by the value of X.
"""

A = int(input())
B = int(input())
X = A + B
print(f"X = {X}")
