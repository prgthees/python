from itertools import combinations
(o,x) =input().split()
x=int(x)
arr=[]
comb=combinations(o,len(o)-x)
comb=list(comb)

for i in (comb):
    arr.append("".join(i))

print(min(arr))
