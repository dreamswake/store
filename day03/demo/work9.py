
# 姓名  年龄  性别  编号   任职公司   薪资   部门编号
names = [
    ["何登勇",56,"男","106","IBM", 500 ,"50"],
    ["曹东雪",19,"女","230","微软", 501 ,"60"],
    ["刘营营", 19, "女", "210", "Oracle", 600, "60"],
    ["李汉聪", 45, "男", "230", "Tencent", 700 , "10"]
]
#1,统计每个人的平均薪资
num=0
for i in range(0,len(names)):
#   for j in range(0,len(names[i])):
    num=num+names[i][5]
print("平均薪资为:",num//len(names))

#统计每个人的平均年龄
num1=0
for i in range(len(names)):
    num1=num1+names[i][1]
print("平均年龄为:",num1//len(names))

#添加新员工到表中
names.append(["张佳伟",45,"男","220","alibaba",500,"30"])
print(names)

#统计公司男女人数
man=0
women=0
for i in range(len(names)):
    if names[i][2]=="男":
        man=man+1
    else:
        women=women+1
print(man,women)

#每个部门的人数
a1=0
a2=0
a3=0
a4=0
for i in range(len(names)):
    if names[i][6]=="50":
        a1=a1+1
    elif names[i][6]=="60":
        a2=a2+1
    elif names[i][6]=="10":
        a3=a3+1
    elif names[i][6]=="30":
        a4=a4+1
print("50部门有:",a1,"\n60部门有:",a2,"\n10部门有:",a3,"\n30部门有:",a4)





