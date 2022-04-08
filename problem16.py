"""
    problem: Get a new string from a given string where 'Is' has been added to the front.
    If the given string already begins with 'Is' then return the string unchanged
"""
name = input("Enter name ")
if len(name) > 2 and name[:2] == "is":
    print(name)
else:
    print("is"+name)



