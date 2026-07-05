from payment import payment
from product import product

class order (product,payment):
    def bill(self):
        qty=int(input("enter the quantity: "))
        total = self.price*qty
        print(self.show_product())
        print("\n total price = ",total)
        
    # def show_message(self):
    #     return payment.pay(self)

obj = order("Car",75000)
obj.bill()
            
