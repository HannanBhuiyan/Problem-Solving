# problem : Create a histogram from a given list of integers
def histogram(items):
    for i in items:
        output = ""
        times = i
        while(times > 0):
            output += "*"
            times -= 1
        print(output)


histogram([2, 4])



