no = int(input(" enter a no: "))
temp = no

while(no!=1 and no!=4):
    sum = 0

    while(no>0):
        rem = no%10
        sum = sum+(rem*rem)
        no = no//10

    no = sum

if(no==1):
    print(f" {temp} is a happy no ")
else:
    print(f" {temp} is a sad no ")
