def mergesort(arr):
    print(f'arr: {arr}')
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    print(f'mid :{mid}')
    left=mergesort(arr[:mid])
    print('left')
    print(left)
    right=mergesort(arr[mid:])
    print('right')
    print(right)
    return merge(left,right)

def merge(left,right):
    print(f'left: {left},right: {right}')
    if len(left)==0:
        return right
    if len(right)==0:
        return left
    if left[0]<right[0]:
        return [left[0]]+merge(left[1:],right)
    return [right[0]]+merge(left,right[1:])

a=[int(x) for x in input().split()]
print(mergesort(a))