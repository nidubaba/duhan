names=["杜汗卿","人名帅","高建新","张三","李四","王五"]
import random
while True:
    print("1:随机点名     2：随机处罚>>>:")
    num=input("请输入编号:")
    if num.isdigit():
        num=int(num)
        if num==1:
            rannum=random.randint(0,len(names))
            print(names[rannum])
        elif num==2:
            a=random.randint(0,100)
            print("恭喜您，中了大奖！！！！",a,"遍！")
    elif num=="q" or num=="Q":
        print("欢迎下次光临")
        break
    else:
        print("对不起输入非法字符！！！请重新输入")





