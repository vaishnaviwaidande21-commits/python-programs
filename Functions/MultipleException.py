try:
    a=int(input(" enter 1st no: "))
    b= int(input(" enter 2nd no: "))

    print(a/b)
except ZeroDivisionError as z:
    print(z)
except ValueError as v:
    print(v)
