# problem: Concatenate all elements in a list into a string and return it
def concatenate_list_data(items):
    data = ""
    for i in items:
        data += str(i)
    return data


print(concatenate_list_data([1, 2, 3, 4, 5]))

print(concatenate_list_data(['jhon', 'smit', 'marry']))