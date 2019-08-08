d1,d2=map(str,input().split())
y=0
if len(d1)>len(d2):
  d1,d2=d2,d1
p=0
while p<len(d1):
  y+=(ord(d2[p])-ord(d1[p]))
  p+=1
for p in range(p,len(d2)):
  y+=ord(d2[p])-ord('a')+1
print(y)
