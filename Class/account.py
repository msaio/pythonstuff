class counter(object):
    number = 0
    def __init__(self):
        type(self).number += 1
        print("Number: "+str(self.number))
    
    def __del__(self):
        type(self).number -= 1
        print("This is from counter")
        print(type(self).number)
        
class account(counter):
    # Constructor: This is not a real contructor, just is something similar.
    # __init__ is called when making an instance
    def __init__(self, holder, number, balance, credit_line = 1500):
        counter.__init__(self)
        self.__holder = holder
        self.__number = number
        self.__balance = balance
        self.__credit_line = credit_line
    # Destructor: There is no real destructor in python just __del__ which works similarly
    # __del__ is call when an instance is about to be destroyed by default (When exit the program).
    # account inherited from counter so method __del__ of counter was called first
    # then __del__ of account was called.
    # No need to overwrite __del__.
    # def __del__(self):
    #     counter.__del__(self)
    #     print("This is from account")
    #     print(self.number)
        ## it would be fine with only these line
        # self.number -= 1
        

    def say_hello(self):
        print("Hello World")

    def deposit(self, amount):
        if amount <=0:
            print("deposit must be more than 0")
            return False
        else:
            print("depositing...")
            self.balance = self.balance + amount
            return True

    def withdraw(self, amount):
        if self.balance - amount < - self.credit_line:
            print("over credit line. U can get more money than", str(self.balance + self.credit_line))
            return False
        else:
            print("withdrawing...")
            self.balance = self.balance - amount
            return True

    def get_balance(self):
        return self.balance
    
    def transfer(self, target, amount):
        if self.balance - amount < - self.credit_line:
            print("over credit line. U only can send more money than " + str(self.balance + self.credit_line))
            return False
        else:
            print("transfering...")
            self.balance = self.balance - amount
            target.balance = target.balance + amount
            return True

try:
    k = account("Guido",345267,10009.78)
except AttributeError:
    pass

try:
    l = account("Sven",345289,3800.0)
except AttributeError:
    pass

try:
    c = account("Mary", 3123331, 300.23)
except AttributeError:
    pass
