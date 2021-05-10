users = [
]
s = 0
f = open(file="scores.txt",mode="r+",encoding="utf-8")
f1 = open(file="成绩.txt",mode="w+",encoding="utf-8")
data = f.readlines()
for i in data:
    da = i.replace("\n","").split(",")
    users.append(da)
    table = users[0 + s][1:]
    s += 1
    a = sum(list(map(int, table)))
    f1.write(da[0] + "总分：" + str(a) + "分" + "\n")





