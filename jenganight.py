t=int(input())
while(t>0):
    a,b=map(int,input().split())
    if(b%a==0):
        print("yes")
    else:
        print("no")
    t=t-1
