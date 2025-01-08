def feb(x):
    assert x>=0,'no negative numbers'
    if x==0 or x==1:
        return x
    return feb(x-1)+feb(x-2)

a=int(input())
print(feb(a))