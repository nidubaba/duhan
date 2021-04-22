b=input("请输入边")
a=input("请输入边")
c=input("请输入边")
a=int(a)
b=int(b)
c=int(c)
if a+c>b and b+c>a and a+b>c:
    if a==b==c:
         print("等边三角形")
    elif  a==b or a==c or c==b:
        print("等腰三角形")
    elif  a*a+b*b==c*c or +c**2 == a**2 or c*c+a**2==b**2:
        print("直角三角形")
    elif a+b>c or a+c>b or b+c>a:
        print("构成三角形+++++")

else:
    print("不构成三角形")




















