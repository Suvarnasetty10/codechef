t=int(input())
while(t>0):
    a,b,c=map(int,input().split())
    d=c/(a*b)
    e=d*100
    if(e>50):
        print("yes")
    else:
        print("no")
    
    t=t-1
