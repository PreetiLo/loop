# n=int(input("enter the number"))
i = 1
while (i<100):
    if (i%2 == 0):
        print(i, 'is not a prime number')
        break
    else:
        print(i, 'is a prime number')
    i = i + 1