def issort(x):
    if len(x)==0 or len(x)==1:
        return True
    if x[0]>x[1]:
        return False
    return issort(x[1:])
a=[int(x) for x in input().split()] 
print(issort(a))
