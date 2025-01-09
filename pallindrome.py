def same(s,i,j):
    if i>j:
        return True
    if s[i]!=s[j]:
        return False
    return same(s,i+1,j-1)

a=input()
print(same(a,0,len(a)-1))