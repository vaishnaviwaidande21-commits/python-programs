sal = float(input("Enter salary: "))
exp = int(input("Enter years of experience: "))
rate = input("Enter rating (A/B/C): ")

bonus = 0

if exp > 5:
    bonus = bonus + sal * 20 / 100

if rate == "A":
    bonus = bonus + sal * 10 / 100
elif rate == "B":
    bonus = bonus + sal * 5 / 100

final_sal = sal + bonus

print("Final Salary =", final_sal)
