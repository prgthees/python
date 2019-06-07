a=input()
if a.isalpha():
  b=['a','e','i','o','u','A','E','I','O','U']
  if a in b:
    print("vowel")
  elif a not in b:
    print("constonant")
else:
  print("invalid")
