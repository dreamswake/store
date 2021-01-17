import time

class oldPhone:
    __a = None

    def __init__(self,a):
        self.__a = a

    def setA(self,a):
        self.__a = a

    def getA(self):
        return self.__a

    def call(self,num1):
        print("正在给",num1,"打电话")
        # for i in range(6):
        #     print(".",end="")
        #     time.sleep(1)

class newPhone(oldPhone):
    def call(self,num1):
        print("语音拨号中...")
        super().call(num1)
        print("品牌为：",super().getA(), "的手机很好用！")


# phone = newPhone("诺基亚")
# phone.call(110)



# phone = oldPhone("诺基亚")
# phone.call("110")








