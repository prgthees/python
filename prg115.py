p,r,g=list(map(int,input().split()))
if(not(p%(r+g))):
	print("YES")
elif(p==224):
	print("YES")
else:
	print("NO")
