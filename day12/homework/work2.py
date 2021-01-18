class getMoney:
    __money = None

    def __init__(self,money):
        self.__money =  money

    def setMoney(self,money):
        self.__money = money

    def getMoney(self):
        return self.__money

    def GetMoney(self,money):
        if money > self.__money:
            raise ArithmeticError("余额不足！")
        else:
            self.__money = self.__money - money
            print("您的余额为：",self.getMoney())
try:
    num = getMoney(3000)
    num.GetMoney(2000)
except ArithmeticError as ER:
    print(ER)






















