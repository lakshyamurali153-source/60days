def maxsubarray(arr):
    res=arr[0]
    max_sum=arr[0]
    for i in range(1, len(arr)):
        max_sum=max(max_sum+arr[i], arr[i])
        res=max(res, max_sum)
    return res

arr=list(map(int,input().split()))
print(maxsubarray(arr))