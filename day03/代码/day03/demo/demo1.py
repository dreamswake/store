a = [1,5,9,3,4,8]

# 1.求所有数的和a[]
sum = 0
for i in range(0,6):
    sum = sum + a[i]
print("总和为：",sum)

# 2.求偶数的和,奇数
sum1 = 0
for i in range(0,6):
    if a[i] % 2 == 0:    #  %2表示对2取余数
        sum1 = sum1 + a[i]
print("偶数的和为：",sum1)

# 3.求列表中的最大值
i = 0
for k in range(0,len(a)):
    if a[k] > i:
        i = a[k]
print("最大值为：",i)





