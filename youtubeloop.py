# for row in range(0,7):
#     for col in range(0,7):

#         if (row+col==3)or(row-col==3)or(row+col==9)or(row-col==3):
#             print("*+-/",end=" ")
#         else:
#             print(" ",end=" ")
#     print()  
# print()          


              
     
         
# diamond shapes
# row=int(input("enter no of row"))
# for a in range(row):
#     print(" "*(row-a)+"  *"*(a+1))
# for b in range(row-1):
#     print(" "*(b+1)+"  *"*(row-1-b))

# for row in range(0,8):
#     for col in range(0,8):
#         if (row+col==3) or (row-col==3) or (row+col==9) or (row-col==3):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")    
#     print()  

# for i in range(1,21):
#     for row in range(2,21):
#         print(i)
# this is print number 111,22,33,44,55,66,77,88,999,10101010,111111,1212121212,13131313,141414,15151515,16161616,1717171717,1818188,191919,202020200


# r1 = int(input("Enter the starting range value?"))
# r2 = int(input("Enter the ending range value?"))
         
# print("Range: %d - %d" % (r1, r2))

# num = r1 + 1
# count = 0

# while num < r2:
#     print("num: %d" % (num))
#     res = num % 2
#     print("res: %d" % (res))
#     if (num % 2) > 0:
#         count += 1
#     num += 1

# print("Odd count: %d" % (count))

# count = 0
# while count < 5 :
#     num = int(input("Enter number between 0-100?"))
#     if (num < 0) or (num > 100):
#         print("Aborted while: You've entered an invalid number.")
#         break
#         count += 1
#     else:
#         print("While loop ended gracefully.")

# while_else_demo()
# pattern
# def pattern(n):
#     k = 2 * n - 2
#     for i in range(0,n):
#         for j in range(0,k):
#             print(end=" ")
#             k = k - 1
#             for j in range(0, i+1):
#                 print("  *", end=" ")
#         print("")
# pattern(15)