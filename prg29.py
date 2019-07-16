a=list(input())
b=len(a)
for i in range (0,b,2):
  a[i],a[i+1]=a[i+1],a[i]
print(a,sep="")
