class Dmart:
    storename="dmart"

    def __init__(self,category,p_name,qty,price):
        self.category=category
        self.p_name=p_name
        self.qty=qty
        self.price=price

    @classmethod
    def display_store(cls):
        return f" store name = {cls.storename}"
    
    def common_features(self):
        return f" category = {self.category} \n product name = {self.p_name}\n quantity = {self.qty}\n price = {self.price}"
    

class clothes (Dmart):
    def __init__(self,category,p_name,qty,price,colour,size):
        super().__init__(category,p_name,qty,price)
        self.colour=colour
        self.size=size

    def display_clothes(self):
        print(super().display_store())
        print(super().common_features())

        return f" colour = {self.colour}\n size = {self.size}\n"


class grocery (Dmart):
    def __init__(self,category,p_name,qty,price,brand,MFG,EXP):
        super().__init__(category,p_name,qty,price)
        self.brand=brand
        self.MFG=MFG
        self.EXP=EXP

    def display_grocery(self):
        print(super().display_store())
        print(super().common_features())

        return  f" Brand name = {self.brand}\n MFG = {self.MFG}\n EXP = {self.EXP}\n"



obj=clothes("clothes","Jeans",100,799,"blue",'M')

obj1 = grocery("grocery_section","sugar",60,100,"sugarlite","2026-06-01","2027-06-01")


while True:
    print("\n Welcome To Dmart \n 1. Grocery_section \n 2. Clothing_section \n 3. Purchase\n 4. exit\n")
    choice=int(input("enter your choice : "))
    print("\n")

    match choice:

        case 1:
            print(obj1.display_grocery())

        case 2:
            print(obj.display_clothes())

        case 3:
            orders=[]

            while True:
                print("\nEnter 1. for grocery shopping \n enter 2. for clothes shopping ")
                choice = int(input(" enter your choice : "))

                if choice ==1:
                    c=input("\nenter yes if you want to purchase the item:  ")

                    if c=='yes':

                        qty=int(input("\n enter the quantity: "))
                        total=obj1.price*qty
                        orders.append([obj1.p_name,qty,obj1.price,total])

                        ch=int(input("\n enter 1. to generate bill\n enter 2. for  continue shopping : "))

                        if ch==1:

                            print("\n--------------BILL-----------------")
                            print("productname \t quantity \t price \t total")

                            gtotal=0
                            for i in orders:
                                print(f"{i[0]} \t\t {i[1]} \t\t {i[2]} \t\t {i[3]}")
                                gtotal=gtotal+i[3]


                        else:
                            continue

                    else:
                        break

                elif choice==2:
                    cl=input("\n enter yes if you want to purchase the items : ")

                    if cl=='yes':

                        qty=int(input("\n enter the quantity: "))
                        total=obj.price*qty
                        orders.append([obj.p_name,qty,obj.price,total])

                        ch=int(input("\n enter 1. to generate bill\n enter 2. for  continue shopping : "))

                        if ch==1:

                            print("\n--------------BILL-----------------")
                            print("productname \t quantity \t price \t total")

                            gtotal=0
                            for i in orders:
                                print(f"{i[0]} \t\t {i[1]} \t\t {i[2]} \t\t {i[3]}")
                                gtotal=gtotal+i[3]

                            print("---------------------------------------")
                            print("Grand Total = ",gtotal)

                            break

                        else:
                            continue

                    else:
                        break

        case 4:
            print(" Thank You!!! \n")

        case _:
            print(" Invalid choice! \n")
