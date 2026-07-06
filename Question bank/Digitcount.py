no = int(input(" enter a no: "))
count = 0

while(no>0):
    d= no%10
    count+=1
    no = no//10

print(" total digits = ",count)
