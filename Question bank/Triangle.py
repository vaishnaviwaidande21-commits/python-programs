a1=int(input(" enter the value of angle 1: "))
a2=int(input(" enter the value of angle 2: "))
a3=int(input(" enter the value of angle 3: "))

if(a1+a2+a3 == 180):
    if(a1==a2==a3):
        print(" Triangle is an equilateral triangle ")
    elif(a1==a2 or a2==a3 or a3==a1):
        print(" Triangle is an Isoceles triangle ")
    else:
        print(" Triangle is an Scalene triangle ")
else:
    print(" Invalid Triangle!!")
