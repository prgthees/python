pr=int(input())
gt=0
if pr>2:
    for i in range(3,int(pr/2)):
        if pr%i==0:
            gt=1
            print("no")
            break
if gt==0 or pr==2:
    print("yes")
