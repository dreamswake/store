a=[9,8,3,2,6,5,7,4,1,10]
# 对该列表进行排序:选择排序
# for i in range(0,len(a)): # 控制大循环走向
#     for j in range(i+1,len(a)):
#         if a[j]>a[i]:
#             c=a[j]
#             a[j]=a[i]
#             a[i]=c
# print(a)
# for i in range(0,len(a)): # 控制大循环走向
#     for j in range(i+1,len(a)):
#         if a[j]>a[i]:
#             c=a[j]
#             a[j]=a[i]
#             a[i]=c
# print(a)
# for i in range(0,len(a)):
#     if a[i]%2==0:
#         print(a[i])


# scores=[40,50,60,80,95]
school=[
    [40,50,60,70,80],
    [45,55,65,75,85],
    [10,50,60,40,80],
    [60,70,80,90,100]
]
#求全校每个班级的总分
# for i in range(0,len(school)):
#     sum2=0
#     for j in range(0,len(school[i])):
#         sum2=sum2 + school[i][j]
#     print((i+1),"班的总分为:",sum2)






#求学校所有人求分数和
# sum1=0
# for i in range(0,len(school)):
#     for j in range(0,len(school[i])):
#         sum1=sum1+school[i][j]
# print("学校所有人总分为:",sum1)



'''
#对所有分数进行总和
sum=0
for i in range(0,len(scores)):
    sum=sum + scores[i]
print("分数总和为:",sum,"平均分为:",(sum//len(scores))) # /表示取商，//表示取商的整数位
'''

