def add(x):
    if len(x)==0:
        return 0
    if len(x)==1:
        return x[0]
    return x[0]+add(x[1:])

a=[int(x) for x in input().split()]
print(add(a))