t=int(input())
while(t>0):
    x=int(input())
    if(x<=100):
        print(x)
    elif(x>100 and x<=1000):
        d=(x-25)
        print(d)
    elif(x>1000 and x<=5000):
        e=(x-100)
        print(e)
    else:
        f=(x-500)
        print(f)
    t=t-1
