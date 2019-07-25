import sys, string, math
p,r = map(int,input().split())
for i in range(max(p,r), p*r+1) :
    if (i%p == 0) and (i%r == 0) :
        g = i
        break
print(g)
