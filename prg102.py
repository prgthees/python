p=input()
r=[]
for i in range(0,len(p)):
  if(int(p[i])%2==1):
     r.append(p[i])
print(*r,end="")
