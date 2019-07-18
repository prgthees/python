pr=input()
g=str(input())
t=('a','e','i','o','u')
for i in g:
    if i in t:
        g=g.replace(i,"")
print(g[::-1])
