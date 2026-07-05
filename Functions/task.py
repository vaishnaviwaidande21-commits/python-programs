def add(no1,no2):

    try:
        addition = no1+no2
        print("addition = ",addition)
\
    except ValueError as v:

        print(v)

    except Exception as e:
        print(" some unknown error occured ",e)

    finally :
        print(" program ended ")


no1=int(input(" enter no1: "))
no2=int(input(" enter no2: "))
add(no1,no2)
