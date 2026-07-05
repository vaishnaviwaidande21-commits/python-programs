for i in range(3):
    print(" " * (4 - 2*i), end="")
    for j in range(2*i + 1):
        print(2*i + 1, end=" ")
    print()

for i in range(1, -1, -1):
    print(" " * (4 - 2*i), end="")
    for j in range(2*i + 1):
        print(2*i + 1, end=" ")
    print()
    
