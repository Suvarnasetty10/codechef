t=int(input())
while(t>0):
    a,b,c=map(int,input().split())
    d=((b*1)+(c*2))
    #print(d)
    if(a<=d):
        print("Qualify")
    else:
        print("NotQualify")
    t=t-1
