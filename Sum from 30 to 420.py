# Write a code that calculates the sum of those 
# numbers from 30 to 420 which are multiples of 8 
# that means those numbers come in the table of 8.

i=30
total=0
while i<=420:
    i+=1
    if i%8==0:
        total+=i
print(total)