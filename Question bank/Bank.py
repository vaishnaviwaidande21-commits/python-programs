sal = int(input("Enter salary: "))
cibil = int(input("Enter CIBIL score: "))
loan = int(input("Enter existing loan amount: "))
age = int(input("Enter age: "))

if sal > 25000 and cibil > 750 and loan < 500000 and age >= 21 and age <= 60:
    print("Eligible")

    if sal > 50000 and cibil > 800:
        print("Premium Customer Loan Offer")
else:
    print("Not Eligible")
