t,s,f=map(int,input().split())
i=0
sum=0
while i<t:
  sum=sum+s
  s=s+f
  i=i+1
print(sum)
