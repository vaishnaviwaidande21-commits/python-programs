no1 = int(input(" enter no1: "))
no2 = int(input(" enter no2: "))
no3 = int(input(" enter no3: "))

if(no1>no2 and no1>no3):
    print(f"{no1} is greater ")
elif(no2>no1 and no2>no3):
    print(f"{no2} is greater ")
else:
    print(f"{no3} is greater ")
