age = int(input(" enter your age: "))
citizenship = input(" enter your citizenship: ")
crecord = input(" yes or no : ")

if(age>=18):
    if(citizenship == "Indian"):
        if(crecord == "no"):
            print( " you are eligible to vote")
        else:
            print( " you have criminal record, you cannot vote!!")
    else:
        print( " citizenship is not indian , you cannot vote!!")
else:
    print( " age is less than 18 , you cannot vote!!  ")
