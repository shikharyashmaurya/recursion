def power2(x):
    if x==0:
        return 1
    return 2*power2(x-1)

a=int(input())
print(power2(a))