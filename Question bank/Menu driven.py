for i in range(100):

    print("\n1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Exit")

    ch = int(input("Enter choice: "))

    if ch == 5:
        break

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    switch = {
        1: a + b,
        2: a - b,
        3: a * b,
        4: a / b
    }

    print("Result =", switch[ch])
