uname = (input(" enter the username: "))

if(uname == "admin"):
    password = int(input(" enter the password: "))
    if(password==1234):
        print(" Login Successfull ")
    else:
        print(" You entered the wrong password ")
else:
    print(" Wrong Username ")
