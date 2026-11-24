for i in range(5):
    if(i == 0 or i == 4):
        for j in range(5):
            print("*",end=" ")
    else:
        for j in range(1):
            print("*",end=" ")
        for j in range(3):
            print(" ",end=" ")
        for k in range(1):
            print("*",end=" ")
    print()
    