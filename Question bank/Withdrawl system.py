bal = int(input(" enter the account balance: "))
amt = int(input(" enter the withdrawl amount: "))

if(amt%100==0):
    if(bal-amt>=1000):
        print(" withdrawl succesfull ")
        print(" remaining balance = ",bal-amt)
    else:
        print(" Failure: minimum balance should remain 1000 ")
else:
    print(" Failure: Amount should be multiple of 100")
