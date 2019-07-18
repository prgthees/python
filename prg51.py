p=input()
r=0
for i in p:
  if i.isalpha():
    pass
  elif i.isdigit():
    pass
  elif i.isspace():
    pass
  else:
    r+=1
print(r)
