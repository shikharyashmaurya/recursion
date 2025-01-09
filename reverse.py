def reverse(s):
    if len(s)==0:
        return ''
    if len(s)==1:
        return s[0]
    return s[-1]+reverse(s[:-1])

a=input()
print(reverse(a))
    