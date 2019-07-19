mn=input()
counto=0
for i in mn:
  if (i.isdigit() or i.isalpha()):
    counto+=1
if counto!=0:
  print("Yes")
else:
  print("No")
