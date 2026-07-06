m1 = int(input(" enter the marks of subject 1: "))
m2 = int(input(" enter the marks of subject 2: "))
m3 = int(input(" enter the marks of subject 3: "))
m4 = int(input(" enter the marks of subject 4: "))
m5 = int(input(" enter the marks of subject 5: "))

percent = (m1+m2+m3+m4+m5)/500 *100
print(" percentage = ",percent)

if(percent>90):
    print(" Grade A -- Distinction ")
elif(percent>75 and percent<=90):
    print(" Grade B -- Pass ")
elif(percent>=50 and percent<=75):
    print(" Grade C -- Pass ")
elif(percent < 50):
    print(" Fail ")
