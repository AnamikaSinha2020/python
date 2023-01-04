class Customer:
    Name = " "
    SSN = " "

    def __init__(self, name, ssn):
        self.Name = name
        self.SSN = ssn

    def Cust_info(self):
        print("Customer Name: ", self.Name)
        print("Customer SSN: ", self.SSN)


class Bank(Customer):
    Card_no = " "
    

    def __init__(self, name, ssn, cardno):
        super().__init__(name, ssn)
        self.Card_no = cardno

    def info(self):
        print("Customer Name: ", self.Name)
        print("Customer SSN: ", self.SSN)
        print("Customer Card no", self.Card_no)


class ATM(Bank):
    balance = 0

    def account_detail(self):
        print(f" Name : {self.Name.upper()}")
        print(f"SSN: {self.SSN}")
        print(f"Balance : {self.balance}")

    def deposit(self, amount):
        self.amount = amount
        self.balance += self.amount
        print(f"current balance", self.balance)

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("insufficiant balance")
        else:
            self.balance -= self.amount
            print("Balance after withdrawal", self.balance)

    def check_balance(self):
        print("Availaval balance ", self.balance)

    def validate(self):
        print("Card validation in progress")
        cn = input("Enter card no")
        if self.Card_no == cn:
            print("Success")
        else:
            print("Invalid card")

    def transaction(self):
        print("""
        1.Account detal
        2. check balance
        3.Deposite
        4.Withdraw
        5.Exit
        """)
        while True:
            option = int(input("Enter your option: "))
            if option == 1:
                atm.account_detail()
            elif option == 2:
                atm.check_balance()
            elif option == 3:
                amount = int(input("Enter the amount"))
                atm.deposit(amount)
            elif option == 4:
                amount = int(input("Enter the withdrawal amount"))
                atm.withdraw(amount)
            elif option == 5:
                return False


name=input("Enter your name: ")
ssn=int(input("Enter ssn no: "))
card=input("enter card no")
atm=ATM(name,ssn,card)
atm.validate()
atm.transaction()