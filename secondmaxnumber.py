n=int(input())
for i in range(n):
    n=list(map(int,input().split()))
    n.remove(max(n))
    print(max(n))

