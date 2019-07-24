prg,pre=input().split()
prh=abs(len(prg)-len(pre))
for i in range(len(prg)):
    if len(pre)==1 and pre[i] in prg:
        break
    if prg[i]!=pre[i]:
        prh+=1
print(prh)
