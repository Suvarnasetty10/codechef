t=int(input())
while(t>0):
    b1,b2,b3=map(int,input().split())
    count=(b1==0)+(b2==0)+(b3==0)
    if(count>=2):
        print("water filling time")
    else:
        print("not now")
    t=t-1
