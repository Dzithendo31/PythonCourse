from datetime import datetime


class Car:
    # add the values
    def __init__(self, name, engine, doors):
        self.name = name
        self.engine = engine
        self.doors = doors

    def horn(self):
        return "Helloe Babbi"


ferrari = Car("Benx", "V*", 23)

print(ferrari.horn())


##Bank Account
class bankAccount:
    intrestRate = 0.02
    Customer = 0

    def __init__(self, AccNo, AccHolder, balance):
        self.AccountNum = AccNo
        self.Name = AccHolder
        self.__balance = balance
        self.transID = 0
        self.trans = []
        bankAccount.Customer += 1

    @classmethod
    def updateInterest(cls, rate):
        bankAccount.intrestRate = rate

    @classmethod
    def getTotalAccounts(cls):
        return bankAccount.Customer

    @staticmethod
    # They don't take clas nor self
    # why use static methods:
    # methods that are bound to a class rather than an instance of the class.

    def displayBalance(self):
        return f"Your Balance is R{self.__balance}"

    def withdraw(self, amount):

        if amount > self.__balance:
            return f"Unsuccesful balance is {self.__balance}"
        else:
            # it there, the money is there..
            self.__balance = self.__balance - amount
            self.trans.append(self.saveTransaction("Withdraw", amount))
            return f"Successful, {self.displayBalance(self)}"

    def deposit(self, amount):
        self.__balance = self.__balance + amount
        self.trans.append(self.saveTransaction("Withdraw", amount))
        return f"Successful, {self.displayBalance(self)}"

    def getBankStatement(self):
        print(f"#  {'id':^6}{'Date':^10}{'Amount':^10}")
        for tran in self.trans:
            print(f"#  {tran['id']:^6}{tran['time']:^10}{tran['amount']:^10}")
        print(f"\n{'Balance:':#>16}{self.__balance:>10}")

    def saveTransaction(self, type, amount):
        # Get the time we got
        item = {}
        item["id"] = self.transID + 1
        item["time"] = f"{datetime.now():%d %b}"
        item["type"] = type
        item["amount"] = amount
        return item

    def applyIntrest(self):
        self.__balance = self.__balance + self.__balance * self.intrestRate


tina = bankAccount(125674234, "Thina", 153_000)
tinaX = bankAccount(12567422344, "Thna", 153_000)

# withdraw
tina.withdraw(3000)
tina.withdraw(3000)
tina.getBankStatement()
tina.applyIntrest()
tina.getBankStatement()
print(bankAccount.getTotalAccounts())


# Types of methods
# static, not gonna chnage anythiing, just a plain function.
# classMethod
#


class Circle:
    pi = 3.14159

    def __init__(self, r) -> None:
        self.r = r

    def area(self):
        return Circle.pi * self.r**2

    @staticmethod
    def parameter(radius):
        return 2 * Circle.pi * radius

    @classmethod
    def from_diameter(cls, d):
        return cls(d / 10)


# Tresting
cirle = Circle(2)
print(cirle.area())
cirlce2 = Circle.from_diameter(10)
print(cirlce2.area())
