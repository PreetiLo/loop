# a="nav"
# a="gurukul"
# print(a,"_",a)

# x=10
# y=x
# y+=2
# print(x)
# print(y)

# iska dry run
# a=[5,6,3,4,5,6,7]
# i=1
# while i<len(a):
#     print(a[i]+2)
#     i+=1    

# asstem
# l=[[1,2,3],10,[2,4,3]]
# m=[]
# i=0
# while i<len(l):
#     if type(l[i])==list:
#         j=0
#         while j<len(l[i]):
#             m.append(l[i][j])
#             print(l[i][j])
#             j+=1      
#     i+=1 
# print(m)

# without len using
# a=[1,2,3,4,5,6]
# for i in a:
#     print(i)

# l=[[1,2,3],10,[2,4,3]]
# for i in range(len(l)):
#     if type(l[i]) is list:
#         for j in range(len(l[i])):
#             print(l[i][j])
#     else:
#         print(l[i])

# a=int(input("enter the number"))
# for i in range(1,a+1,1) :
#     for j in range(1,i+1):
#         print(j,end="")
#     print("")      


# i=1
# while i<51:
#     print(i**2)
#     i+=1

# j=1
# i=51
# while j<i:
#     print(j**2)
#     j+=1

# l=[2,9,8,7,6,5,4,14,7,3]
# b=[]
# c=[]
# sum=0
# sum1=0
# i=0
# while i<len(l):
#     if l[i]%2==0:
#         sum+=l[i]
#         b.append(l[i])
#     else:
#         sum1+=l[i]
#         c.append(l[i])
#     i+=1
# print(b,sum,"even")
# print(c,sum1,"odd")

l=[1,2,3,4,5,6,7,8,9,20]
b=[]
c=[]
sumofeven=0
sumofodd=0
perseofeven=0
perseofodd=0
count=0
i=0
while i<len(l):
    if l[i]%2==0:
        sumofeven=sumofeven+l[i]
        count+=1
        b.append(l[i])
    else:
        sumofodd=sumofodd+l[i]
        count+=1
        c.append(l[i])
    i+=1
# perseofeven = (count/sumofeven/len(l))*100
# perseofodd=(count/sumofodd/len(l))*100
# print(b,perseofeven,"% percentage of even",sumofeven%len(b))
# print(c,perseofodd,"% percentage of odd",sumofodd%len(c))
perseofeven=(count*100)/sumofeven
perseofodd=(count*100)/sumofodd
print(b,perseofeven)
print(c,perseofodd)
