def search(x,y):
    if len(x)==0:
        return False
    if x[0]==y:
        return True
    return search(x[1:],y)
a=[int(x) for x in input().split()]
b=int(input())
print(search(a,b))
    
    
