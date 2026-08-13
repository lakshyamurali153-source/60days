arr=list(map(int,input().split()))
prefix_sum = [0] * len(arr)
for i in range(len(arr)):
    prefix_sum[0]=arr[0]
    prefix_sum[i] = prefix_sum[i-1] + arr[i] if i > 0 else arr[i]
    print(prefix_sum,end=" ")
