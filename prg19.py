a,g=list(map(int,input().split()))
for i in range(a+1,g):
  f=len(str(i))
  b=i
  c=0 
  while b>0:
    d=b%10
    b=b//10
    e=d**f
    c=c+e
  if i==c:
    print(c)
