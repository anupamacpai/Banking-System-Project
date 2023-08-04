class BankAccount:
    def login(self):
        users={'anupamac95':'Anupama*1995',
               'madhav2020':'Madhavrpai2001',
               'sinur2001':'Sinur#2001',
               'Meerad02':'Meerad@20',
               'Vinus0321':'Vinusnair*21'}
        username=input("Enter username:")
        password=input("Enter password:")
        if username in users and users[username]==password:
            print("Login successful")
        else:
            print("Invalid credentials!Please try again")
            exit()
    def __init__(self):
        self.balance=0
    def deposit(self):
        amount=float(input("Enter the amount to be deposited:"))
        self.balance+=amount
        print("Amount deposited is:",amount)
    def withdraw(self):
        amount=float(input("Enter the amount to be withdrawn:"))
        if self.balance>=amount:
            self.balance-=amount
            print("You withdraw:",amount)
        else:
            print("Insufficient balance")
    def display(self):
        print("Available balance is:",self.balance)
b1=BankAccount()
print("Welcome to Banking services")
b1.login()
b1.deposit()
b1.withdraw()
b1.display()