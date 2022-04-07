n = int(input())
isPrime = False
if n > 1:
    for i in range(2, n):
        print(i)
        if n % i == 0:
            isPrime = True
            break

else:
    print("Enter the number greater than 1")
    exit()

if isPrime:
    print(n, "is not a Prime number")
else:
    print(n, "is a prime number ")