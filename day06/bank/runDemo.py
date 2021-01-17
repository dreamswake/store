from bank.Bank import Bank
from bank.View import view
from bank.View import user_info
from bank.User import User
from bank.Bank import Bank
from bank.Address import Address
from bank.DBUtils import DBUtils

def addUser():
    bank = Bank()
    # 开户逻辑
    username = input("请输入您的姓名：")
    password = input("请输入您的密码：")
    print("接下来要输入您的地址信息：")
    country = input("国家：")
    province = input("省份：")
    street = input("街道：")
    door = input("门牌号：")
    money = int(input("请输入您的余额："))

    address = Address(country,province,street,door)

    user = User(username=username,password=password,address=address,money=money)
    # user.setAddress(address)
    # user.setUsername(username)
    # user.setMoney(money)
    # user.setPassword(password)

    # 将上述数据传输给银行开户逻辑
    status = bank.bankAddUser(user)

    if status == 3:
        print("对不起，本银行用户库已满，请携带证件到其他银行办理！")
    elif status == 2:
        print("对不起，您的个人信息已存在！请稍后再试！")
    elif status == 1:
        print("恭喜！开户成功！以上就是您的开户信息！")

def select1():
    bank =Bank()
    account = input("请输入账号：")
    password = input("请输入密码：")
    bank.select(account,password)

def savemoney():
    bank = Bank()
    account = input("请输入账号：")
    money = int(input("请输入存款金额："))
    bank.saveMoney(account,money)

def getmoney():
    bank = Bank()
    account = input("请输入账号：")
    password = input("请输入密码：")
    money = int(input("请输入取款金额："))
    status = bank.getMoney(account,password,money)
    if status == 1:
        print("取款账号不存在！")
    elif status == 2:
        print("密码错误！")
    elif status == 3:
        print("余额不足！")

def movemoney():
    bank = Bank()
    account = input("请输入转出账号：")
    account1 = input("请输入转入账号：")
    password = input("请输入转出密码：")
    money = int(input("请输入金额："))
    status = bank.moveMoney(account,account1,password,money)
    if status == 1:
        print("转出账号不存在！")
    elif status == 2:
        print("转入账号不存在！")
    elif status == 3:
        print("密码不正确！")
    elif status == 4:
        print("转出账号余额不足！")





while True:
    # 1.打印视图
    print(view)

    # 2.让用户输入 ,并判断输入是否合法
    choose=input("请输入您的业务编号:")# 输入
    if choose.isdigit():# 判断输入是否是数字
        if not int(choose) in range(1,7):# 业务编号是否在可控范围
            print("您的输入非法！请重新输入！")
            continue
        else:
            choose=int(choose)
    if choose == 1:
        addUser()
    elif choose ==2:
        savemoney()
        # print("存钱业务！")
    elif choose == 3:
        getmoney()
        # print("取钱业务！")
    elif choose == 4:
      movemoney()
        # print("转账业务！")
    elif choose == 5:
        select1()
        # print("查询用户！")
    elif choose == 6:
        print("-------------------这位爷！欢迎下次光临!-------------------")
        exit(0) # 退出
























