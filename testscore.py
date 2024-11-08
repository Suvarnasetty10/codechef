t=int(input())
while(t>0):
    a,b,c=map(int,input().split())
    if(c%b==0):
        print("yes")
    else:
        print("no")
    t=t-1
