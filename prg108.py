p=list(input())
r=[]
for i in p:
    if i not in r:
        r.append(i)
if(p==r):
    print("Yes")
else:
    print("No")
