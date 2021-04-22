import random
du=random.randint(0,101)
count=0
jinbi=10000
while True:
    count=count+1
    jinbi=jinbi-500
    du1=input("请输入您要猜的数字：")
    du1=int(du1)
    if count==7:
        print("账户冻结，退出系统")
        break
    if du1>du:
        print("大了")
    elif du1<du:
        print("小了")
    else:
        print("回答正确！！！","du","你本次猜了",count,"次！！！","剩下",jinbi,"金币")
        break