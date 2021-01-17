class Cook:
    __name = None
    __age = None

    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def setName(self,name):
        self.__name = name
    def getName(self):
        return self.__name

    def setAge(self,age):
        self.__age = age
    def getAge(self):
        return self.__age

class Cook1(Cook):
    def cook(self):
        print(super().getName(),"在炒菜！")

class Cook2(Cook1):
    def cook(self):
        print(super().getAge(),"岁的",super().getName(),"在炒菜！")

# a=Cook2("张三",18)
# print(Cook2.getName(a))
# print(Cook2.getAge(a))
# a.cook()













