def digit(x):
    if x==0:
        return
    digit(x//10)
    print(x%10)
a=int(input())
digit(a)