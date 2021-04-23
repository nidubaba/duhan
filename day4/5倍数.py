a = [1,5,21,30,15,9,30,24,20,25,11]
b = len(a)
c = 0
d = 0
while c < b:
    if a[c] % 5 ==0:
        d = d + a[c]
        c =c+1
    else:
        c=c+1
print(d)

