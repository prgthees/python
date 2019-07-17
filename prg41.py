p1,p2=map(int,input().split())
lis=[]
if(p1>1 and p2>1):
    for i in range (p1,p2+1):
        for j in range (2,i):
            if (i%j==0):
                break
        else:
            lis.append(i)
print(len(lis))
