t=int(input())
for r in range(t):
    a=input()
    x=""
    y=""
    for i in range (0,len(a)):
        if i%2==0:
            x+=str(a[i])
        else:
            y+=str(a[i])
    print(x,end=" ")
    print(y)


