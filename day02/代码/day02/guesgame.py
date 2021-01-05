# author:jason
'''
    1.猜数字游戏
        1.1 数字：由系统随机产生0~100
        1.2 一直猜，直到猜中为止。循环
        1.3 判断
    2.技术选型：
        2.1 如何随机
            2.1.1 导入随机数的包  import  random
            2.1.2 调用随机数的方法，得到一个随机数
        2.2 如何循环:while  + break
        2.3 if...elif...else
'''
import  random
# 让系统产生一个随机数
num = int(random.random() * 100)# 0~100
i = 0 # 游戏的计数器
while True: # 让用户无限次的猜
    a = int(input("请输入您猜的数：")) # 输入猜的数字
    i = i + 1 # 统计次数
    if a > num: # 判断猜的数字与随机数的大小关系
        print("大了！") # 温馨提示
    elif a < num:
        print("小了！")
    else: # 猜中的打印信息
        print("恭喜，猜中了，本次随机数为：",num,"您本次猜了",i,"次！")
        break # 猜中后就跳出循环

# 循环while
# i = 1
#
# while True:# True  False
#     if i > 5:
#         break # 中断
#     print("hello,world!",i)
#     i = i + 1




















