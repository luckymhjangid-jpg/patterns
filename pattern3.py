n = 5
for i in range(n):
    for j in range(n-i):
          print("*",end=" ")
    print()

print("\n")
for i in range(0,5,1):
     for j in range(0,5-i):
          print("*",end=" ")
     print()
