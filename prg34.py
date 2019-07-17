abc=int(input())
dem=list(map(int,input().split()[:abc]))
print(sorted(dem))
for i in dem:
  print(i,end=" ")
