# author：jason
'''
    程序的三个结构：
    1.顺序结构
    2.循环结构
        for，while
    3.选择结构
        if：单
        if...else：双
        if...elif....elif.............................else：多
'''
# input 可以从键盘输入数据  "89"  -int("89")->  89
score = input("请输入您的分数：")
score = int(score)

if score >= 90  and score <= 100:
    print("优秀！Excellent!")
elif score >= 80  and score < 90:
    print("良！good!")
elif score >= 70  and score  < 80:
    print("一般般！just so so!")
elif score >= 60 and score < 70:
    print("及格，小伙子你很危险！")
elif score >= 0 and score < 60:
    print("不及格！恭喜你，您的试卷正在路上！")
else:
    print("成绩不合法!成绩您自己改的吧！")









'''
age = 15
if age >= 18:
    print("客官，您可以进来了！")
else:
    print("小屁孩，没到18岁，写瞎溜达！")
'''





