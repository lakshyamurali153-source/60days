arr=list(map(int,input().split()))
prefix_sum = [arr[0]]
for i in range(1,len(arr)):
    prefix_sum.append(prefix_sum[i-1]+arr[i])
print(prefix_sum)
    
