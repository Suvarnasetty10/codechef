t=int(input())
while(t>0):
    a,b=map(int,input().split())
    c=a*b
    if(c<100):
        print("0")
    else:
        d=c//100
        print(d)
    
    t=t-1
