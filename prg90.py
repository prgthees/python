prg=int(input())
pre=[]
for j in range(0,prg):
 prh=input()
 pre.append(prh)
prt=[]
for j in zip(*pre):
    if(j.count(j[0])==len(j)):
        prt.append(j[0])
    else:
     break
print(''.join(prt))
