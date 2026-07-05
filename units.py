unit = int(input(" enter the units:  "))

if(unit<=100):
    unit = unit*2
    print(" units = ",unit)

elif(unit>100 and unit<=200):
    unit = (unit*3)+200
    print(" units = ",unit)
    
elif(unit>200):
    unit = (unit*5)+500
    print(" units = ",unit)
