class People:
    __age = None
    __sex = None
    __name = None


    def __init__(self,age,sex,name):
        self.__age = age
        self.__sex = sex
        self.__name = name

    def setAge(self, age):
        self.__age = age

    def getAge(self):
        return self.__age

    def setSex(self,sex):
        self.__sex = sex

    def getSex(self):
        return self.__sex

    def setName(self,name):
        self.__name = name

    def getName(self):
        return self.__name





class workPeople(People):
    def work(self):
        print(super().getAge(),"岁的",super().getSex(),super().getName(),"在干活！")

class Student(People):
    __num = None

    def setNum(self,num):
        self.__num= num
    def getNum(self):
        return self.__num

    def study(self):
        print(self.getNum(),super().getAge(), "岁的",super().getSex(),"学生", super().getName(), "在学习。")

    def sing(self):
        print(self.getNum(),super().getAge(), "岁的", super().getSex(), "学生", super().getName(), "在唱歌。")

a = workPeople(18,"男","张三")
a.work()
b = Student(15,"男","李四")
b.setNum("01")
b.study()
b.sing()







