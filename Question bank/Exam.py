n = int(input("Enter number of students: "))

for i in range(n):
    print("\nStudent", i + 1)

    total = 0

    for j in range(5):
        m = int(input("Enter marks: "))
        total += m

    per = total / 5

    if per >= 75:
        grade = "A"
    elif per >= 60:
        grade = "B"
    elif per >= 40:
        grade = "C"
    else:
        grade = "F"

    print("Total =", total)
    print("Percentage =", per)
    print("Grade =", grade)

    if per >= 40:
        print("Pass")
    else:
        print("Fail")
