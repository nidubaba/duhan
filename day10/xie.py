a=input("请输入路径")
f1 = open(file=a,mode="r+",encoding="utf-8")
f2= open(file="E:\\python\\b.txt",mode="w+",encoding="utf-8")
b=f1.read()
f2.write(b)
f2.close()
f1.close()







