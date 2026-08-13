def maxsubarray(arr):
    res=arr[0]
    for i in range(len(arr)):
        sum=0
        for j in range(i,len(arr)):
            sum+=arr[j]
            res=max(res,sum)
    return res

arr=list(map(int,input().split()))
print(maxsubarray(arr))