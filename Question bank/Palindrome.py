no = int(input(" enter a no: "))
temp =no
rev = 0

while(no>0):
    d=no%10
    rev = rev*10 +d
    no = no//10

if(temp == rev):
    print(" Palindrome ")
else:
    print(" not a Palindrome ")
