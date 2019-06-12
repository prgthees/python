q=list(map(int,input().split()))
d=q[1]
t=list(map(int,input().split()))
s=0
z=len(t)
for i in range(0,z):
    if(i<d):
        s+=t[i]
print(s)
