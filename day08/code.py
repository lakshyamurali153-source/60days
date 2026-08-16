arr = [21, 34, 42, 55, 68, 70, 83, 92]
print("Simulated User Data (Ages):", arr)
count = 0
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        count += 1
print("The number of even elements in the array is:", count)