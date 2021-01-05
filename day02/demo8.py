a=int(input("请输入第一条边长:"))
b=int(input("请输入第二条边长:"))
c=int(input("请输入第三条边长:"))
if a>0 and b>0 and c>0:
    if a+b>c and b+c>a and a+c>b:
        if a!=b and a!=c:
            print("可以构成三角形")
        elif a==b and b!=c and a!=c:
            print("可以构成等腰三角形")
        elif a==c and a!=b and a!=c:
            print("可以构成等腰三角形")
        elif b==c and a!=b and a!=c:
            print("可以构成等腰三角形")
        elif a==b==c:
            print("可以构成等边三角形")
    else:
        print("不能构成三角形")
else:
    print("请输入三个大于0的数")



