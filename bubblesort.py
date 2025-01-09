def bubble(x):
    if len(x)==0 or len(x)==1:
        return x
    else:
        for i in range(len(x)-1):
            if x[i]>x[i+1]:
                x[i],x[i+1]=x[i+1],x[i]
        return bubble(x[:-1])+[x[-1]]
x=[int(i) for i in input().split()]
print(bubble(x))