# n = int(input('Enter number of rows : '))
 
# i = 1
# while i <= n :
#     j = 1
#     while j <= i:
#         print("*", end = " ")
#         j += 1
#     print()
#     i += 1
# n = int(input('Enter number of rows : '))
# i = 1
# while i <= n :
#     j = n
#     while j >= i:
#         print("*", end = " ")
#         j -= 1
#     print()
#     i += 1

# import copy
# import random


# def main():
#     my_list = list(range(10))
#     print(my_list)
#     print(shuffle(my_list))
#     print(my_list)
#     shuffle_in_place(my_list)
#     print(my_list)


# def shuffle(container):
#     new_container = copy.copy(container)
#     shuffle_in_place(new_container)
#     return new_container


# def jay(name,number):
#     pass
# def main():
#     students=['anjali','suchitra','divyani','preeti','amisha']
#     print(jay(students,3)
# # if _name_ =='_main_':
# #     main()    

# import random
# def shuffle(x):
#     for i in range(len(x),1,-1):
#         r=random.randint(0,i-1)
#         temp=x[i-1]
#         x[i-1]=x[r]
#         x[r]=temp
#     return x
# def main():
#     p=[2,10,3,4,5,6,7,8,9,1,0]
#     print(p)
#     print(shuffle(p))



# def shuffle_in_place(container):
#     for index in range(len(container) - 1, 0, -1):
#         other = random.randint(0, index)
#         if other == index:
#             continue
#         container[index], container[other] = container[other], container[index]


# if __name__ == '__main__':
#     main()