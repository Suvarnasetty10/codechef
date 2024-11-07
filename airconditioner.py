t=int(input())
while(t>0):
    a,b,c=map(int,input().split())
    if((a<=b)and(b>=c)):
        print("yes")
    else:
        print('no')
    t=t-1
