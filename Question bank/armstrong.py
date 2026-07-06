no = int(input("Enter a number: "))

temp = no
s = 0

while no > 0:
    d = no % 10
    s = s + (d * d * d)
    no = no // 10

if s == temp:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
