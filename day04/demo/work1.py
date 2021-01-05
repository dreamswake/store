shop=[
    ["iphone 8p",1000],
    ["mac loptop",12000],
    ["iwatch",500],
    ["lenovo PC",4000],
    ["辣条",10],
    ["洗衣粉",23.5]
]
while True:
    salary = input("请初始化您的薪资:")
    if salary.isdigit():
        salary = int(salary)
        break
    else:
        print("请输入合适的薪资:")

def showshop():
    for item,value in enumerate(shop):
        print(item,value)

import random
a=float(random.uniform(8,10)/10)
b=round(a,1)
print(b)



mycart=[]
n=0
while True:
    print("-----------欢迎来到XXX商城---------------","您的本次随机优惠为:",b,"--------------------")
    showshop()
    chose = input("请输入您要购买的商品编号:")
    if chose.isdigit():
        chose = int(chose)
        if chose > len(shop):
            print("您输入的商品不存在:")
        else:
            if salary < shop[chose][1]:
                print("\033[41;20;1m穷鬼，您的金钱余额不足，下个月再来吧！\033[0m")
            else:
                mycart.append(shop[chose])
                # shop[chose][1] = shop[chose][1]*b
                salary = salary - shop[chose][1]*b
                if shop[chose][1] >= 4000 and shop[chose][1] < 10000:
                    n=n+200
                elif shop[chose][1] >= 10000 and shop[chose][1] < 50000:
                    n=n+400
                elif shop[chose][1] < 4000:
                    n=n+0
                print("\033[32;20;1m购买成功！您的余额为:",salary,"您的积分为:",n,"\033[0m")
                # if shop[chose][1] >= 4000 and shop[chose][1] < 10000:
                #     n=n+200
                #     print("\033[32;20;1m您的积分为:",n,"\033[0m")
                # elif shop[chose][1] >=10000 and shop[chose][1] < 50000:
                #     n=n+400
                #     print("\033[32;20;1m您的积分为:",n,"\033[0m")
                # elif shop[chose][1] < 4000:
                #     n=n+0
                #     print("\033[32;20;1m您的积分为:",n,"\033[0m")


    elif chose=="Q" or chose=="q":
        break
    else:
        print("您的输入不合法！请重新输入！")
print("-------------------欢迎下次光临-----------------")
print("以下是您购物车的信息:")
for item in mycart:
    print(item)
print("您的余额为:",salary)
print("您的总积分为:",n)






