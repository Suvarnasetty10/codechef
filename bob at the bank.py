t=int(input())
while(t>0):
    w,x,y,z=map(int,input().split())
    s=(w+(x*z))-(y*z)
    print(s)
    t=t-1
