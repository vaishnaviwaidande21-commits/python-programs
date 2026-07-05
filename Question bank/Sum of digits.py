no = int(input(" enter a no: "))
sum =0

while(no>0):
    d = no%10
    sum = sum+d
    no = no//10

print(" sum of digits =  ",sum)
