p,r=map(int,input().split())
g=list(map(int,input().split()))
for i in range (0,r):
    g=[g[-1]]+g[:-1]
print(*g,end='')
