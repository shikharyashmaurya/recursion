def power(a,b):
    if b==0:
        return 1
    if b==1:
        return a
    c=power(a,b//2)
    if b%2==0:
        return c*c
    else:
        return a*c*c

a=int(input())
b=int(input())
print(power(a,b))