# a=[5,6,7,[5,7,8]]
# b=[]
# i=0
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         while j<len(a[i]):
#             b.append(a[i][j])
#             j+=1
#     else:
#         b.append(a[i])
#     i+=1
# print(b)    


# a=[[2,3,8],[3,2,1],[5,6,1]]
# sum=0
# sum1=0
# sum2=0
# i=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         sum+=a[i][j]
#         j+=3
#     i+=1
# print(sum)        
# i=0
# while i<len(a):
#     j=1
#     while j<len(a[i]):
#         sum1+=a[i][j]
#         j+=2
#     i+=1
# print(sum1)
# i=0
# while i<len(a):
#     j=2
#     while j<len(a[i]):
#         sum2+=a[i][j]
#         j+=4
#     i+=1
# print(sum2)



         
# n1=int(input("enter the number"))
# l1=[]
# n=0
# while n <n1:
#     if n%2==0:
#         l1.append(n**2)
#     n+=1
# print(l1)    

#list_mp=[[23,40,60],[40,90,80],[60,70,30]]
# i=0
# sum=0
# averge=0
# count=0
# while i<len(list_mp):
#     j=0
#     while j<len(list_mp[i]):
#         sum=sum+list_mp[i][j]
#         averge=averge//list_mp[i][j]
#         count=count+1
#         j=j+1
#     i=i+1
# print(sum,averge,count)   

# a= [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]     
# i=0
# lis=[]
# while i<len(a):
#     if a[i] not in lis:
#         lis.append(a[i])
#     i+=1
# print(lis)


# n= [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11] 
# i=0
# repeated = []
# while i<len(n):
#     m=n[i]
#     if m not in repeated:
#         repeated.append(m)
#     i+=1     
# print(repeated)  


# student_marks = [23, 45, 89, 90, 56, 80] 
# # length = len(student_marks)
# index = 0
# total_marks = 0
# while index < len(student_marks):
#     total_marks = student_marks[index] + total_marks
#     index = index + 1
# print ("Total Marks: ",+(total_marks))


# a=["madan"]
# i=0
# while i<len(a):
#     print(len(a[::]))
#     i+=1

# a=[[2,6,8],[2,9,5]]
# b=[]
# i=0
# while i<len(a):
#     if b not in a:
#         for j in range(0,len(b)):
#             # if b[i]%2==0:
#                 # print("even")
#                 b.append(a[i][j])
#     # else:
#                 # print("odd")
#                 # b.append(a[i]) 
#     i+=1
# print(b) 



# a=[[1,2,3,45,6,78],[1,5,3,4,6]]
# i=0
# while i<len(a):
#     j=0
#     while j<len(a):
#         if a[i]%2==0:
#             if a[j]%2==0:
#                 print(a[i],"even")
#         else:
#             print(a[j],"odd")
#         j=j+1
#     i=i+1
         




# student_marks = [23, 45, 67, 89, 90, 54, 34, 21, 34, 23, 19, 28, 10, 45, 86, 87, 9]
# list_length = len(student_marks)
# index = 0
# less_than50 = 0
# more_than50 = 0
# while index < list_length:
#     marks = student_marks[index]
#     if marks < 50:
#         less_than50 = less_than50 + 1
#     else:
#         more_than50 = more_than50 + 1
#     index = index + 1
# print ("Marks more than 50: " + str(more_than50))
# print ("Marks less than 50: " + str(less_than50))


# print("Enter quant")
# quantity = input()
# if quantity*100 >1000:
#     print ("Cost is"((quantity*100)-(1*quantity*100)))
# else:
#     print ("Cost is",quantity*100)


    
# i=10
# while i>0:
#     print(i)
#     i-=1