prg=input()
pre=0
for i in prg:
	if prg.count(i)>pre:
		pre=prg.count(i)
		j=i
print(j)	
