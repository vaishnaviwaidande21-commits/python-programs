class p1:
    def xyz(self):
        print(" From p1 ---- XYZ")

    def show(self):
        print(" I am from p1")

    def __init__(self,name):
        self.name=name
        print(" name = ",self.name)
        print(" p1 constructor")

class p2:
    def abc(self):
        print(" From p2 ----- ABC")

    def show(self):
        print(" I am from p2")

    def __init__(self,age):
        self.age=age
        print(" age = ",self.age)
        print(" p2 constructor")

class c(p1,p2):
    def pqr(self):
        print(" From child -----PQR")

    def show(self):
        print(" I am from child")

    def show_p2(self):
        return p2.show(self)
    
    def __init__(self,name,age):
        print(" consturctor :-")

        p1.__init__(self,name)
        p2.__init__(self,age)



obj=c("Purva",17)
# obj.xyz()
# obj.show()
# obj.abc()
# obj.pqr()
# obj.show_p2()
