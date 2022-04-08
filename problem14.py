# problem: Test whether a number is within 100 of 1000 or 2000
def near_thousand(n):

     if (abs(1000 - n) <= 100) or (abs(2000 - n) <= 100):
         return True
     else:
        return False


print(near_thousand(5000))  # return False
print(near_thousand(1000))  # return True