def count(x):
    if x==0:
        return
    print(x)
    count(x-1)

a=int(input())

count(a)