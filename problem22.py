# problem: Check whether a specified value is contained in a group of values
def is_group_number(group_num, n):
    return n in group_num


print(is_group_number([1, 5, 8, 3], 3))
print(is_group_number([5, 8, 3], -1))
