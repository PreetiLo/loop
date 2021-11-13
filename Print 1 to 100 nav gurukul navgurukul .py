numb=1
while numb<=100:
    print(numb)
    numb=numb+1
    if numb%3==0:
        print("Nav")
    elif numb%7==0:
        print("Gurukul")
    elif numb%3==0 and numb%7==0:
        print("NavGurukul")
    else:
        print(numb)