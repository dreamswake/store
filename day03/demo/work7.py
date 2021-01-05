list = [1,2,3,4,5,6,7,8,9]
# 实现效果：list = [9,8,7,6,5,4,3,2,1]

for i in range(0,len(list)):
    for j in range(i+1,len(list)):
        if list[i]<list[j]:
            c=list[j]
            list[j]=list[i]
            list[i]=c
print(list)
