t=int(input())
while(t>0):
    a,b=map(int,input().split())
    c=a-b
    d=(a*10//100)
    e=a+d
    print(e-c)
    t=t-1



