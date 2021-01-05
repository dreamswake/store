a=[15,20,12,63,3,8,94,61,27,5,10]


num=0
for i in range(0,len(a)):
    if a[i]%5==0:
        num=num+a[i]
print("其中是5的倍数的和为:",num)

