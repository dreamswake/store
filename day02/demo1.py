score=input("请输入您的分数:")
score=int(score)
if score>=90 and score<=100:
    print("优秀！excellent")
elif score>=80 and score<90:
    print("良好！good")
elif score>=70 and score<80:
    print("一般！just so so!")
elif score>=60 and score<70:
    print("及格，小伙子你很危险！")
elif score>=0 and score<60:
    print("不及格，恭喜你，你的试卷正在路上！")
else:
    print("成绩不合法，您的成绩自己改的吧！")