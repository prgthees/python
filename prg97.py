p = input()
r = len(p)
g = r//2
if r%2 == 1 : 
   t=p[:g] + '*' + p[g+1:]
else :        
   t=p[:g-1] + '**' + p[g+1:]
print(t)
