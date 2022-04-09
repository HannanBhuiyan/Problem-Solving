# problem : n (non-negative integer) copies of the first 2 characters of a given string

def sub_string_copy(str, n):
    sub_str = ""

    if len(str) < 2:
        for i in range(n):
            sub_str = sub_str + str

    else:
        for i in range(n):
            sub_str = sub_str + str[:2]

    return sub_str


print(sub_string_copy("abcdef", 2))
print(sub_string_copy("a", 3))