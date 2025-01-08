def revcount(x):
    if x==0:
        return
    revcount(x-1)
    print(x)

a=int(input())
revcount(a)