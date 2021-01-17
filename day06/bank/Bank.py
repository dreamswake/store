from bank.DBUtils import DBUtils
from bank.View import user_info
class Bank:
    __db = DBUtils(database="lida")
    __bankName = "中国工商银行北京市沙河支行"

    def getBankName(self):
        return self.__bankName


    def bankAddUser(self,user):
        sql1 = "select count(1) from t_user"  # 查询是否已满的数据库
        sql = "select * from t_user where username = %s" # 检查是否存在该用户
        sql2 = "insert into t_user(" \
               "account,username,password,country," \
               "province,street,door,money,reg_date,bankname)" \
               " values(%s,%s,%s,%s,%s,%s,%s,%s,now(),%s)"
        param = [user.getUsername()]
        if self.__db.select(sql1,None)[0][0] >= 100:
            return 3
        elif len(self.__db.select(sql,param)) != 0:
            return 2
        else:
            param1 = [
                user.getAccount(),
                user.getUsername(),
                user.getPassword(),
                user.getAddress().getCountry(),
                user.getAddress().getProvince(),
                user.getAddress().getStreet(),
                user.getAddress().getDoor(),
                user.getMoney(),
                user.getBankName()
            ]
            self.__db.update(sql2,param1)

            print(user_info.format(account=user.getAccount(),
                          username=user.getUsername(),
                          password=user.getPassword(),
                          country=user.getAddress().getCountry(),
                          province=user.getAddress().getProvince(),
                          street=user.getAddress().getStreet(),
                          door=user.getAddress().getDoor(),
                          money=user.getMoney(),
                          time=user.getRegisterDate(),
                          bank_name=user.getBankName()))
            self.__db.releaseConnection()
            return 1

    def selectUser(self,account,password):
        sql = "select * from t_user where account = %s  and password = %s"
        param = [account,password]
        result = self.__db.select(sql,param,mode="one")
        return result

    def select(self,account,password):
        bank = Bank()
        sql = "select * from t_user where account = %s "
        sql1 = "select * from t_user where account = %s and password = %s"
        param = [account]
        param1 = [account, password]
        if len(self.__db.select(sql, param)) == 0:
            print("账号不存在！")
        elif len(self.__db.select(sql1, param1)) == 0:
            print("密码错误！")
        else:
            database = bank.selectUser(account, password)
            print(user_info.format(account=database[1],
                                   username=database[2],
                                   password=database[3],
                                   country=database[4],
                                   province=database[5],
                                   street=database[6],
                                   door=database[7],
                                   money=database[8],
                                   time=database[9],
                                   bank_name=database[10]))

    def saveMoney(self,account,money):
        sql = "select * from t_user where account = %s"
        sql1 = "update t_user set money = %s where account =%s"
        param = [account]
        if len(self.__db.select(sql,param)) == 0:
            print("存款账号不存在！")
            return False
        else:
            a=self.__db.select(sql,param,mode="one")
            money = a[8] + money
            param1 = [money,account]
            self.__db.update(sql1,param1)
            print("存款成功！")
            return True

    def getMoney(self,account,password,money):
        sql = "select * from t_user where account = %s"
        sql1 = "select * from t_user where account = %s and password = %s"
        sql2 = "update t_user set money = %s where account =%s"
        param = [account]
        param1 = [account,password]
        if len(self.__db.select(sql,param)) == 0:
            # print("取款账号不存在！")
            return 1
        elif len(self.__db.select(sql1, param1)) == 0:
            # print("密码错误！")
            return 2
        else:
            a=self.__db.select(sql,param,mode="one")
            if a[8]<money:
                return 3
            else:
                money = a[8] - money
                param2 = [money,account]
                self.__db.update(sql2,param2)
                print("取款成功!")

    def moveMoney(self,account,account1,password,money):
        sql = "select * from t_user where account = %s"
        sql1 = "select * from t_user where account = %s and password = %s"
        sql2 = "update t_user set money = %s where account =%s"
        param = [account]
        param1 = [account1]
        param2 = [account,password]
        if len(self.__db.select(sql,param)) == 0:
            return 1     #转出账号不存在！
        elif  len(self.__db.select(sql,param1)) == 0:
            return 2     #转入账号不存在！
        elif len(self.__db.select(sql1, param2)) == 0:
            return 3     #密码不正确！
        else:
            a=self.__db.select(sql,param,mode="one")
            b=self.__db.select(sql,param1,mode="one")
            if a[8]<money:
                return 4    #转出账号余额不足！
            else:
                money1 = a[8] - money
                money2 = b[8] + money
                param3 = [money1,account]
                param4 = [money2,account1]
                self.__db.update(sql2,param3)
                self.__db.update(sql2,param4)
                print("转账成功！")




