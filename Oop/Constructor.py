# class student:
#     def  stud(self,name,rollno):
#         self.name=name
#         self.rollno=rollno

# s=student()
# s.stud
global_var=20
class Demo:
    pass


    def __init__(self):
        print("obj created")

    def __init__(self,age):
        self.name="Purva"
        self.age=age

    def __del__(self):
        print(" obj deleted")

    def access(self):
        print(global_var)
        local_var=17
        print(local_var)


obj=Demo(17)
print("name = ",obj.name)
print("age = ",obj.age)
obj.access()
print("global variable= ",global_var
