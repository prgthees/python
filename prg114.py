p1,p2=map(str,input().split())
r=0
if len(p1)>len(p2):
  p1,p2=p2,p1
g=0
while g<len(p1):
  r+=(ord(p2[g])-ord(p1[g]))
  g+=1
for p in range(g,len(p2)):
  r+=ord(p2[g])-ord('a')+1
print(r)
