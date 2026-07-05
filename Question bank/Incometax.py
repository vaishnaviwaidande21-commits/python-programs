inc = float(input("Enter income: "))

if inc <= 250000:
    tax = 0
elif inc <= 500000:
    tax = inc * 5 / 100
elif inc <= 1000000:
    tax = inc * 20 / 100
else:
    tax = inc * 30 / 100

cess = tax * 4 / 100
total_tax = tax + cess

print("Tax =", tax)
print("Cess =", cess)
print("Total Tax =", total_tax)
