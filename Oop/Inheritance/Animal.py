class Animal:
    type="animal type"

    def __init__(self):
        print(" default constructor called ")

    def __init__(self,name,weight):
        self.name=name
        self.weight=weight

    def xyz(self):
        print(" hello from parent class")

    def greet(self):
        print(" hello I am Animal")


class Dog(Animal):

    def __init__(self):
        print(" child constructor")

    def __init__(self,name,weight,colour):
        self.colour=colour
        super().__init__(name,weight)

    def abc(self):
        print(" I am from child class")

    def dog_details(self):
        super().greet()
        print(f" name = {self.name}   colour = {self.colour}")

d=Dog("lab","7kg","Black")
d.xyz()
d.abc()
d.dog_details()
