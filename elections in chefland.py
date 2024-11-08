t=int(input())
while(t>0):
    n,x=map(int,input().split())
    v=list(map(int,input().split()))
    d=0
    for i in v:
        if(i>=x):
            d=d+1
    print(d)
    
    t=t-1
