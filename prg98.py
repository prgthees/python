p = int(input())
if p==2 : 
  print('no')
else :
    flag = 0
    for i in range(2,p) :
        if p%i == 0 :
           print('yes')
           break
    else :
        print('no')
