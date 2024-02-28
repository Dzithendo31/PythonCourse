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

    def __init__(self, AccNo, AccHolder, balance):
        self.AccountNum = AccNo
        self.Name = AccHolder
        self.__balance = balance
        self.transID = 0
        self.trans = []

    def displayBalance(self):
        return f"Your Balance is R{self.__balance}"

    def withdraw(self, amount):

        if amount > self.__balance:
            return f"Unsuccesful balance is {self.__balance}"
        else:
            # it there, the money is there..
            self.__balance = self.__balance - amount
            self.trans.append(self.saveTransaction("Withdraw", amount))
            return f"Successful, {self.displayBalance()}"

    def deposit(self, amount):
        self.__balance = self.__balance + amount
        self.trans.append(self.saveTransaction("Withdraw", amount))
        return f"Successful, {self.displayBalance()}"

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

# withdraw
tina.withdraw(3000)
tina.withdraw(3000)
tina.getBankStatement()
tina.applyIntrest()
tina.getBankStatement()
