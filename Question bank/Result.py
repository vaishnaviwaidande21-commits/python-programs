for i in range(5):
    m = int(input("Enter marks: "))

    per = m

    if per >= 75:
        grade = "A"
    elif per >= 60:
        grade = "B"
    elif per >= 40:
        grade = "C"
    else:
        grade = "Fail"

    print("Total =", m)
    print("Percentage =", per)
    print("Grade =", grade)
