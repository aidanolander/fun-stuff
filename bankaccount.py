class BankAccount(object): 
  balance = 0
  def __init__(self, name):
    self.name = name
  def __repr__(self):
    return "This account belongs to %s. Balance: $%.2f" % (self.name, self.balance)
  def show_balance(self):
    print "Balance: $%.2f" % (self.balance)
  def deposit(self, amount):
    self.amount = amount
    if amount <= 0:
      print "Cannot add zero or less to account."
      return
    else:
      print "Depositing $%.2f into account." % (self.amount)
      self.balance += amount
      self.show_balance()
  def withdraw(self, amount):
    self.amount = amount
    if amount > self.balance:
      print "Missing required funds."
      return
    else:
      print "Withdrawing $%.2f from account." % (self.amount)
      self.balance -= amount
      self.show_balance()

my_account = BankAccount("AidanAccount")
print my_account
my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(1000)

print my_account

