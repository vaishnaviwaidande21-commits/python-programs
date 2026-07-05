fare = float(input("Enter base fare: "))
age = int(input("Enter age: "))
gender = input("Enter gender (M/F): ")
cls = input("Enter class (AC/NonAC): ")

if age >= 60:
    fare = fare - fare * 20 / 100

if gender == "F":
    fare = fare - fare * 10 / 100

if cls == "AC":
    fare = fare + fare * 25 / 100

print("Final Fare =", fare)
