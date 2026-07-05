n = int(input("Enter number of customers: "))

total = 0

for i in range(n):
    plan = int(input("Enter recharge plan (199/399/599): "))
    total += plan

print("Total Earnings =", total)
