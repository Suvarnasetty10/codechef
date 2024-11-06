t=int(input())
while(t>0):
    a=list(map(int,input().split()))
    c=0
    b=(max(a))
    #print(b)
    a.remove(b)
    for i in a:
        c=c+i
    #print(c)
    if(b>c):
        print("yes")
    else:
        print("no")
    
    t=t-1
