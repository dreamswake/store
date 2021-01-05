'''
    1.给购物车添加购物积分功能。
        0~5000： 200
        5000~10000 : 400
    2.方法
        def ["方法名"] (参数列表):
            方法体
            return  将数据返回
'''
# 写一个方法，方法对传入的数据进行求和
# def sum(x,y):
#     s = x + y
#     return s

# 定义一个方法，求和结果，无需返回，直接打印即可。
# def sum(x,y):
#     s = x + y
#     print("求和结果为：",s)
#
# sum(7,8)
# 定义方法，传入一个n，打印NxN的乘法表。具有功能单一性。不要讲一个方法即可一个功能又做其他功能。
def table(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,"x",i,"=",(i*j),"\t",end="")
        print()


# n = input("请输入乘法表的层数：")
# n = int(n)
# table(n)

def sum(x,y):
    return x + y

# a = 9  b = 3  c = 7
a = 9
b = 3
c = 7

s1 = sum(sum(a,b),c)
print(s1)






















