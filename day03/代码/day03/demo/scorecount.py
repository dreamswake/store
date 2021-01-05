'''
    1.列表
    2.字典 + 方法
    3.中国工商银行账户管理系统：（开户，存钱，取钱，转账，查询，退出）
'''

scores = [90,85,75,72,63,10]
school = [
    [75,50,64,81,82,95],  # school[1][1]
    [10,20,36,85,75,12],
    [40,62,85,31,20],
    [90,10,120,36,102]
]
# 1. 求全校每个班级的总分
for i in range(0,len(school)):
    sum = 0
    for j in range(0,len(school[i])):
        sum = sum + school[i][j]
    print((i+1),"班的总分为：",sum)

# 1.对学校所有人求分数和
sum1 = 0
for i in range(0,len(school)):
    for j in range(0,len(school[i])):
        sum1 = sum1 + school[i][j]
print("全校分数综合为：",sum1)

# 1.对所有分数进行综合
sum = 0
for i in range(0,len(scores)):
    sum = sum +  scores[i]
print("总分为：",sum,"平均分为：",(sum // len(scores) ))



