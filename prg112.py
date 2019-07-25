p=input()
r=[]
for i in p:
    if(i.isnumeric()):
        r.append(i)
print(''.join(r))
