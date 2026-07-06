amt = float(input("Enter bill amount: "))
vip = input("VIP customer (yes/no): ")

dis = 0

if amt > 5000:
    dis = amt * 20 / 100
elif amt > 2000:
    dis = amt * 10 / 100

if vip == "yes":
    dis = dis + amt * 5 / 100

amt = amt - dis
gst = amt * 18 / 100
total = amt + gst

print("Final Bill =", total)
