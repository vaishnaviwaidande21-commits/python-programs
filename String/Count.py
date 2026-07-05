str="Maharashtra"

ec=0
oc=0

for ch in range(0,11):
    if ch % 2 ==0:
        ec+=1
    else:
        oc+=1

print(" even count = ",ec)
print(" odd count = ",oc)
