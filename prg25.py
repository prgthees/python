a=int(input())
b=0
while(a>0):
  digit=a%10
  b=b*10+digit
  a=a//10
print(b)
