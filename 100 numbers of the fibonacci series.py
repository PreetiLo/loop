# Make an algorithm that prints the first 100 numbers of the fibonacci series.
# Fibonacci series is shown here, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
# In this series first_number is 0 andsecond_number is 1. After this, 
# the next number will be the sum of the last two numbers.

f=0
s=1
c=0
while c<=60:
    print(f)
    c=f+s
    f=s
    s=c