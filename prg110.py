import math
p,r=map(int,input().split())
g=math.gcd(p,r)
t=(p*r)/g
print(math.ceil(t))
