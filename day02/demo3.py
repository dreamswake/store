username1=input("请输入姓名:")
sex1=input("请输入性别:")
age1=input("请输入年龄:")
high1=input("请输入身高:")
weight1=input("请输入体重:")
num1=input("请输入身份证号:")


info='''
----------------个人信息----------------
姓名:{username}
性别：{sex}
年龄:{age}岁
身高:{high}cm
体重:{weight}kg
身份证号:{num}
---------------------------------------
'''
print(info.format(username=username1,sex=sex1,age=age1,high=high1,weight=weight1,num=num1))