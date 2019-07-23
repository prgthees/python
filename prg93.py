import sys, string, math
def reduceN( o, k) :
	if k <= 0 : return o

	if o == 0 : return 10	# Fail
	p1 = reduceN(o//10, k)*10 + n%10
	p2 = reduceN(o//10, k-1)
	if p1 < p2 :
		return p1
	else :
		return p2

o,k = input().split()
o,k = int(o),int(k)
print(reduceN(o,k))
