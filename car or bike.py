t=int(input())
while(t>0):
    a,b=map(int,input().split())
    if(a>b):
        print("car")
    elif(a<b):
        print("bike")
    else:
        print("same")
    t=t-1

