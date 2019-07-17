a,b=map(str,input().split())
c=list(a)
d=list(b)
count=0
for i in range(0,len(c)):
  if(c[i]!=d[i]):
    count+=1
if(count==1):
  print("yes")
else:
    print("no")
