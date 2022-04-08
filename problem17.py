# problem : Get a string which is n (non-negative integer) copies of a given string
def larger_string(str, n):
    result = ""
    for n in range(n):
        result += str
    return result


print(larger_string(".op", 5))
print(larger_string(".py", 5))