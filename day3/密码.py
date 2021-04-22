name="root"
mima="admin"
count=0
while   True:
    name1=input("请输入您的用户名")
    mima=input("请输入您的密码")
    count=count+1
    if  count==3:
        print("账户被冻结")
        break
    if mima=="admin"and name1=="root":
        print("登录成功")
        break
    else:
        print("登录失败,用户名或密码错误")
