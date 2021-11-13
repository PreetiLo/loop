# n=5
# for i in range(n,0,-1):
# 	for j in range(i):
# 	    print('* ', end="")
# 	print('')
# In this pattern for right angle   

# n=5
# for i in range(n):
# 	for j in range(i):
# 	    print ('* ', end="")
# 	print('')
# In this pattern for down angle    

# i=1
# while i<=10:
#     j=1
#     while j<=i:
#         print("j",end="i ")
#         j=j+1
#     print()
#     i=i+1  
# this pattern are right angle

# # diamond shapes for other shapes
# row=int(input("enter no of row"))
# col=int(input("enter no of col"))
# for a in range(row):
#     print(" "*(row-a)+"  *"*(a+1))
# for b in range(col-1):
#     print(" "*(b+1)+"  *"*(row-1-b))


# heart shep
for row in range (6):
    for col in range(7):
        if (row==0 and col%3!=0) or (row==1 and col%3==0) or (row-col==2) or  (row+col==8):
            print("*",end="")
        else:
            print(end=" ")
    print()
# diamond shapes
# for row in range(0,7):
#     for col in range(0,7):
#         if (row+col==3) or (row-col==3) or (row+col==9) or (row-col==9):
#             print("*",end=" ")
#             print("*",end=" ")
#         else:
#             print("",end=" ")    
#     print()        
