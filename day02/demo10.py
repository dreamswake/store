'''
A=56
B=78
C=B-A
print("调整前:","\nA=",A,"\nB=",B,)
A=A+C
B=B-C
print("调整后:","\nA=",A,"\nB=",B,)
'''

i=1
n=3
while i<=3:
    n=n-1
    i=i+1
    user = input("请输入用户名:")
    password = input("请输入密码:")
    print("还有", n, "次错误机会")
    if user=="jason":
        if password=="admin":
            print("登录成功")
        else:
            print("密码错误")
    else:
        if password=="admin":
            print("用户名错误")
        else:
            print("用户名和密码错误")
print("还有",n,"次错误机会")




