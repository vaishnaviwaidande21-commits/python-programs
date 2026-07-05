x={}
print(x,type(x))

x["name"]="ram"
print(x)
print(x["name"])

x["name"]="sita"
print(x["name"])

x["age"]=17
print(x)

x.update({"name":"Purva"})
x.update({"age":18})

key=input(" enter key: ")
value=input(" enter value: ")
x[key]=value
print(x)
