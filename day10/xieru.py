from  DBUtils import select

from  DBUtils import  update





'''
以下文件是用户的一些数据（姓名、年龄、净资产），要求使用数据库工具将文件中的数据写入到数据库中。并统计所有人的资产总和！

'''


f=open(file="用户.txt",mode="r+",encoding="utf-8")
date=f.readlines()

for i in date :
    print(date)
    a=i.replace("\n","").split(",")
    sql="insert into money values (%s,%s,%s)"
    parm=[a[0],a[1],a[2]]
    update(sql,parm)
sql1="select sum(money) from money"
money=select(sql1,[])
print("总和为:",money[0][0])
f.close()




