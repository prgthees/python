p = int(input())
r = []
for i in range(1,p+1) :
    if p%i == 0 : 
      r.append(i)
print(*r)
