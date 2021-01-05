# author:jason

# 个人信息模板
username = "张三"
age = 36
high = 1.56
weight = 145
# 李四的个人信息
u1 = "李四"
age1 = 56
high1 = 1.89
weight1 = 200
# 个人信息的打印模板
info = '''
-----------个人展示-----------
姓名：{username},
年龄：{age}岁,
身高：{high}m,
体重：{weight}kg,
----------------------------
'''
# 数据填充，数据的格式化
print(info.format(username=username,age=age,high=high,weight=weight))
print(info.format(username=u1,age=age1,high=high1,weight=weight1))







