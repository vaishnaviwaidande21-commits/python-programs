normal = 0
fever = 0

for i in range(20):
    t = float(input("Enter temperature: "))

    if t > 100:
        fever += 1
    else:
        normal += 1

print("Normal Patients =", normal)
print("Fever Patients =", fever)
