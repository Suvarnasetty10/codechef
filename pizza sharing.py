import math
t=int(input())
while(t>0):
    a,b=map(int,input().split())
    c=a*b
    d=c/4
    e=math.ceil(d)
    print(e)
    t=t-1
