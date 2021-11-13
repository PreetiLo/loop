# for row in range(7):
#     for col in range(7):
#         print("*",end="")
#     print()

        # if row==5 and col%3!=0 or row==3 and col%3==0 or row-col==2:
           
    #     else:
    #         print(end=" ")
    # print()            

# n=int(input("enter of number for pattern"))
# row=3
# col=0
# while row<n:
#     while col<n:
#         # if (row==3 and col%3!=0 )or (row==3 and col%3==0) or (row-col==2) or (row+col==1):
#         #     print("*",end="")
#         #     break
#         if (row+col==2) or (row==3 and col%3!=0) or (row-col==1) or (row==3 and col%3==0):
#             print("*",end="")
#         else:
#             print(end="")
#     print()            

# rows = 7
# for num in range(rows):
#     for i in range(num):
#         print(
#         num, end=" ")  
#     print(" ")
#     for i in range(num):
#         for num in range(rows):
#             print(i,end="")
#         print("")
#         break
   
# rows = 10
# i = 1
# while i <= rows:
#     j = 0
#     while j <=i:
#         print((i+2%1),end=" ")
#         # print((i * 2 - 1), end=" ")
#         j = j + 1
#     i = i + 1
#     print()   
# this pattern for number 1,22,33,44,555,66 etc.

# rows = int(input("Enter the number of rows: "))  
# i = 1  
# # outer file loop to print number of rows  
# while i <= rows:  
#     j = 1  
#     # Check the column after each iteration  
#     while j <= i:  
#         # print odd values  
#         print((i * 2 - 1), end=" ")  
#         j = j + 1  
#     i = i + 1  
#     print()  


















col=5
rows=4
i=1
while i<=col:
    j=1
    while j<=6-i:
        print(" ",end=" ")
        j+=1
    k=1
    while k<=1:
        print("*",end="")
        k+=1
    print()
    i+=1        
# # rows=6
a=1
while a<=rows:
    b=1
    while b<=6-a:
        print("",end="")
        b+=1
    c=1
    while c<=1:
        print("*",end="")
        c+=1
    print()
    a+=1            
        

# rows=7
# col=7
# a=1
# while (a<=rows,col):
#     b=1
#     while b<=7-a:
#         print(" ",end="")
#         b+=1
#     c=1
#     while c<=1:
#         print("* ",end="")
#         c+=1
#     print()
#     a+=1
            

# row=5
# i=1
# while i<=row:
#     j=1
#     while j<row-1:
#         print("*",end=" ")
#         j+=1
#     print()
#     i+=1        