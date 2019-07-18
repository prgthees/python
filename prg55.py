pre=int(input())
p=0
r=1
g=1
for i in range(pre):
	print(g,end=' ')
	g=p+r
	p=r
	r=g
