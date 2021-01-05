shop=[
    ["iphone 8p",1000],
    ["mac loptop",12000],
    ["iwatch",500],
    ["lenovo PC",4000],
    ["辣条",10],
    ["洗衣粉",23.5]
]
#1.展示商品
# for item,value in enumerate(shop):
#     print(item,value)
# for item in shop:
#     print(item)
def showshop():
    for item,value in enumerate(shop):
        print(item,value)

#2.让用户输入自己的薪资
while True:
    salary = input("请初始化您的薪资:")
    if salary.isdigit():     # isdigit() 判断某个字符串是否是由数字组成"12345"
        salary=int(salary)
        break
    else:
        print("请输入合适的薪资")

mycart=[]
#3.开始购物
while True:
    # 3.1先展示商品
    print("-----------欢迎来到XXX商城---------------")
    showshop()

    #3.2 请输入要买的商品编号
    chose=input("请输入您要买的商品编号:")
    if chose.isdigit():  #判断输入是否是数字
        chose=int(chose)
        if chose > len(shop):
            print("您输入的商品不存在！")
        else:
            if salary < shop[chose][1]:#如果钱不够，
                print("\033[41;20;1m穷鬼，您的金钱余额不足，下个月再来吧！\033[0m")
            else: #正常买东西，添加到我的购物车，薪资减去相应的商品金钱
                mycart.append(shop[chose])
                salary = salary - shop[chose][1]
                print("\033[32;20;1m购买成功！您的余额为:",salary,"\033[0m")

    elif chose=="Q" or chose =="q":
        break
    else:
        print("您的输入不合法!请重新输入！")
print("-------------------欢迎下次光临-----------------")
print("以下是您购物车的信息:")
for item in mycart:
    print(item)
print("您的余额为:",salary)










