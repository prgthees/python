p,r=map(int,input().split())
g=p*r
t=g*g
if(t%p==0):
    print("yes")
else:
    print("no")
