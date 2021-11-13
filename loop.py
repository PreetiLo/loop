# i=0
# while i<=10:
#     print(i)
#     i+=1
# print("whole number")  
# 
# n=int(input("enter the number"))
# if n>1:
#     if n%2==0:
#         print(n,"not a prime number")
#     else:
#         print(n,"its prime number")  
# else:
#     print("not prime number")            
# s=0
# i=n
# while i>0:
#     f=1
#     r=i%10
#     for i in range(1,r+1):
#         f*=i
#         print("this number %d=%d"%(r,f))
#         s+=f
#     i//=10
# print("\n given the number %d=%d"%(n,s))    
# if n==s:
#     print("its strong number") 
# else:
#     print("its not strong number")          

# s=0
# i=n
# while i>0:
#     j=1
#     f=1
#     r=i%10
#     while j<=r:
#         f*=j
#         j+=1
#     s+=f
#     i//=10
# if s==n:  
#     print(n,"is a storng number")
# else:
#     print(n,"is not storng number")          
# a=[1,2,[3,4,5],[6,7,8],9,[10,11,12]]
# sum=0
# i=0
# while i<len(a):
#     j=0
#     b=a[i]
#     if type(b)is a:
#         for j in range(len(b)):
#             sum+=1
#             j+=1
#     else:
#         sum=sum+a[i]
#     i+=1
# print(sum)    

# reversed in smple loop   
# i=10
# while i>=0:
#     print(i)
#     i-=1
# print("reversed")        

# user input that reversed number
# a=int(input("enter the number"))
# i=a
# while i>0:
#     print(i)
#     i-=1
# print(i,"reversed number")    

# a=[100,20,40,50,60,10,30]
# a=[10,30,40,60,50,20,100]
# a.sort(reverse=True)
# print(a)
# b=[]    
# i=0
# while i<len(a):
#     print(a[i])
#     if len(a[i])%2==0:
#         print(i,"even")
        
#     else:
#         if a[i] not in b:
#             b.append(b)  
#     i+=1
# print()   

# binary_number = [1, 0, 0, 1, 1, 0, 1, 1]
# i = 0
# while i<len(binary_number):
# # for ele in binary_number:
# 	i= (i << 1)
# print ("The converted integer value is : " + str(i))
# 

# question 1
# names_list = ["rahul", "shivam", "kavay", "ashish", "rohit"]
# print(names_list) 
# print (type(names_list))

# mixed = ["rahul", 12, 9.0, "kaavay", "shivam", 1]
# mixed1=[]
# i=0
# while i<=len(mixed):
#     mixed1.append(mixed)
#     j=i
#     while j<len(mixed1[i]):
#         print(mixed1[j])
#         j+=1
#     i+=1
# print(mixed1)    

# without len funcation using 
# num=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# for i in range(0,num):
#     print(i)


# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# i=0
# while i<len(numbers):
#     j=second(numbers[i])
#     while (j<second-max(numbers[i])):
#         j+=1
#     i+=1
# print("\n second-max ",max(numbers))    

'''
1
14
149
14916
1491625
'''

# a=int(input("enter any number"))
# i=1
# while i<=a:
#     j=i*1
#     while j<=i:
#         print(j+i,end="")
#         j+=1
#     print()
#     i+=1








