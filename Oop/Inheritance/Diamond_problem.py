class A:
    def abc(self):
        print(" from abc A")

    def __init__(self,name):
        self.name=name
        print("name = ",self.name)
        print(" A constructor")

class B(A):
    def xyz(self):
        print(" from xyz B")
    
    def __init__(self,age):
        # A.__init__(self)
        self.age=age
        print(" age = ",self.age)
        print(" B constructor")
        super().__init__()


class C(A):
    def pqr(self):
        print(" from pqr C")

    def __init__(self,rollno):
        # A.__init__(self)
        self.rollno=rollno
        print(" roll no = ",self.rollno)
        print(" C constructor")
        super().__init__()

class D(B,C):
    def mno(self):
        print(" from mno D")

    def __init__(self,branch):
        #  B.__init__(self)
        #  C.__init__(self)
         self.branch=branch
         print(" branch = ",self.branch)
         print(" D constructor")
         super().__init__()


obj = D("Purva",17,219,"CO")
# obj.abc()
# obj.xyz()
# obj.pqr()
# obj.mno()
