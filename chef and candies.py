import math
t=int(input())
while(t>0):
    n,x=map(int,input().split())
    if(n>x):
        c=n-x
        d=c/4
        print(math.ceil(d))
    else:
        print("0")
    t=t-1
