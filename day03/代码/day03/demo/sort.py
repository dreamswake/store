a = [3,5,4,7,2,1,9,10,8,6]

# 对该列表进行排序:选择排序
for i in range(0,len(a)):  # 控制大循环走向
    for j in range(i+1,len(a)):
        if a[j] < a[i]:
            c = a[j]
            a[j] = a[i]
            a[i] = c
print(a)





