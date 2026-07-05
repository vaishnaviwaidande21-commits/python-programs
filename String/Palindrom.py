str="Maharashtra"
rev=""
length = len(str)

for ch in str:
    rev = ch + rev

if(str==rev):
    print("Palindrome")
else:
    print(" not palindrome")
