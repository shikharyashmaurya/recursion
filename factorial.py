def factorial(x):
    assert x>=0 ,'number must be 0 or +ve'
    if x==0:
        return 1
    return x * factorial(x-1)

if __name__=='__main__':
    a=int(input('enter a number: '))
    print(factorial(a))