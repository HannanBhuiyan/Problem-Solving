"""
problem: Print all even numbers from a given numbers list in the same order and stop the printing if any numbers
that come after 237 in the sequence
"""


def even_number_list(numbers):
    for i in numbers:
       if i == 237:
           print(i)
           break
       elif i % 2 == 0:
            print(i)


even_number_list([
    386, 462, 237, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958,743, 527
    ])
