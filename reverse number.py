t=int(input())
while(t>0):
    rev=0
    n=int(input())
    while(n>0):
        u=n%10
        rev=rev*10+u
        n=n//10
    print(rev)
    t=t-1
