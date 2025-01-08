def reach(x,y):
    print(x, '--' ,y)
    if x==y:
        return
    if x<y:
        reach(x+1,y)
    else:
        reach(x-1,y)

a=int(input())
b=int(input())
reach(a,b)