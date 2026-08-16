n=list(map(int,input("Enter numbers separated by space: ").split()))
print("sum:", sum(n))
print("max:", max(n))
print("min:", min(n))
reverse=[]
for i in range(len(n)-1,-1,-1):
    reverse.append(n[i])    
print("reversed:", reverse)
frequency = {}
for num in n:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
print("frequency of each number:")
for num, count in frequency.items():
    print(f"{num}: {count}")
