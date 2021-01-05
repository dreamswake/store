# for i in range(0,11):
#     print(i)


# for i in range(0,5):
#     for j in range(0,i+1):
#         print("*",end="")    # end==""表示不换行
#     print()

# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,"*",i,"=",(j*i),"\t",end="")
#     print()
# n=input("请输入乘法表的层数:")
# n=int(n)
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,"*",i,"=",(j*i),"\t",end="")
#     print()

a=[1,2,5,9,8,6]

# 1.求所有数的和

# sum=0
# for i in range(0,6):
#     sum=sum + a[i]
# print("所有数的和为:",sum)

#2.求偶数的和
# sum1=0
# for i in range(0,len(a)):
#     if a[i] %2 == 0:                        # %2表示对2取余数
#         sum1=sum1+a[i]
# print("偶数的和为:",sum1)

#3.求列表中的最大值
# i=0
# for k in range(0,len(a)):
#     if a[k]>i:
#         i=a[k]
# print("最大数为:",i)

# print("最大数为:",max(a))

# for i in range(0,len(a)):
#     if a[i]%2==0:
#         print(a[i])


for i in range(0,len(a)):
    if a[i]%2==0:
        print(a[i])









