try:
    file=open("MyFile.txt","x")
    print(file)
except Exception as e:
    print(e)

with open("MyFile.txt","w") as f:
    f.write(" Hello ")
    print(" Data Added ")

with open("MyFile.txt","r") as f:
    data=f.read()
    print(data)

with open("MyFile.txt","a") as f:
    f.write(" World !! ")
