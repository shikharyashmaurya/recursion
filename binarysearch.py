def search(x,s,e,y):
    if s>e:
        return -1
    t=s+(e-s)//2
    if x[t]==y:
        return t
    elif x[t]>y:
        return search(x,s,t-1,y)
    else:
        return search(x,t+1,e,y)
    
a=[int(x) for x in input().split()]
b=int(input())
print(search(a,0,len(a)-1,b))
    