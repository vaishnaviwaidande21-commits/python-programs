class Bank:
    def __init__(self):
        self.Bname="HDFC Bank"
        self.Ifsc="HDFC001234"

    def display_bank(self):
            print(f"Bank name :- {self.Bname}")
            print(f"Ifsc no :- {self.Ifsc}")

class Account(Bank):
    def __init__(self):
        Bank.__init__(self)
        self.Acc_no="5928"
        self.Acc_Holder="Purva"

    def display_Account(self):
            print(f"Account_no :- {self.Acc_no}")
            print(f"Account_Holder :- {self.Acc_Holder}")

class Saving_Acc(Account):
    def __init__(self):
        Account.__init__(self)
        self.Balance=55000

    def display_Savings(self):
            print(f"Balance = {self.Balance} ")



    def Deposit(self):
            amt=int(input("\n enter deposit amount: "))
            self.Balance = self.Balance+amt
            print(" Amount deposited succesfully")
            print(" updated amount = ",self.Balance)



    def Withdraw(self):
            amt=int(input("\n enter withdraw amount: "))
            
            if (self.Balance)-(amt)>=2500:
                self.Balance=self.Balance-amt

                print(" amount withdrawn succesfully")
                print(" updated Balance = ",self.Balance)

            else:
                print(" Minimum balance must be maintained !!")



    def FD_Calculation(self):
            months = int(input("\n enter the number of months(3/6/9) : "))

            if months ==3:
                interest = (self.Balance*7*3) / (100*12)
            
            elif months ==6:
                interest = (self.Balance *7*6) / (100*12)

            elif months ==9:
                interest = (self.Balance*7*9) / (100*12)

            else:
                print(" Invalid choice ")
                return

            Final_amt=self.Balance + interest

            print(" Interest = ",interest)
            print(" Final Amount = ",Final_amt)




obj=Saving_Acc()


obj.display_bank()
obj.display_Account()
obj.display_Savings()

obj.Deposit()
obj.Withdraw()
obj.FD_Calculation()
