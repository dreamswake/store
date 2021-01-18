from homework.AgeException import AgeException



class Person:
    # __age = None
    #
    # def __init__(self,age):
    #     self.__age = age

    def setAge(self,age):
        if age <= 0:
            raise AgeException ("非法数据！")
        else:
            self.__age = age
            print("数据合法！")

    def getAge(self):
        return self.__age

try:
    person = Person()
    person.setAge(-1)
except AgeException as Err:
    print(Err)





















