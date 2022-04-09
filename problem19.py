# problem: Count the number 4 in a given list

def count_four(numbers):
    count = 0
    for i in numbers:
        if i == 4:
            count = count + 1

    return count


print(count_four([1, 2, 3, 4, 5, 4, 7, 4, 4, 4]))
