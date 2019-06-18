a=int(input())
f=len(str(a))
b=a
c=0 
while a>0:
  d=a%10
  a=a//10
  e=d**f
  c=c+e
if b==c: 
  print('yes')
else:
  print('no')
      
