class BankAccount:
 def __init__(self, account_number, account_holder_name, initial_balance=0.0):
   self.__account_number = account_number
   self.__account_holder_name = account_holder_name
   self.__account_balance = initial_balance

 def deposit(self, amount):
  if amount > 0:
   self.__account_balance += amount
   print(f"\nDeposited ₹{amount:.2f} successfully.")
  else:
   print("\nInvalid deposit amount. Please enter a positive amount.")

 def withdraw(self, amount):
  if amount > 0:
   if amount <= self.__account_balance:
    self.__account_balance -= amount
    print(f" \nWithdrew ₹{amount:.2f} successfully.")
   else:
    print("\nInsufficient balance for withdrawal.")
  else:
    print("\nInvalid withdrawal amount. Please enter a positive amount.")

 def display_balance(self):
   print(f" \nAccount Number        : {self.__account_number}")
   print(f" \nAccount Holder Name   : {self.__account_holder_name}")
   print(f" \nAccount Balance       : ₹{self.__account_balance:.2f}")


# Create an instance of the BankAccount class
account = BankAccount("IBC522098", "Deepika", 100.0)

# Test deposit and withdrawal functionality
account.display_balance()
account.deposit(500.0)
account.withdraw(20.0)
account.display_balance()