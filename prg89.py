pr=int(input())
gt=list(map(int,input().split()))
he=1
for i in gt:
	if gt.count(i)==he:
		es=i
print(es)
