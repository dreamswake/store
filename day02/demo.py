username="黎达"
age="18"
sex="男"
high="168"
weight="50"
print("我叫:",username,"，今年",age,"岁!性别",sex,",身高",high,",体重",weight,)

user="张三"
age1=40
high1=170
weight1=60

user2="李四"
age2=50
high2=170
weight2=70

info='''
----------------个人信息----------------
姓名:{username}
年龄:{age}岁
身高:{high}cm
体重:{weight}kg
---------------------------------------
'''
print(info.format(username=user,age=age1,high=high1,weight=weight1))
print(info.format(username=user2,age=age2,high=high2,weight=weight2))











