s = input("Enter a string: ")
print("reverse of the string is:", s[::-1]) #Space Usage: O(n)
print("reverse of the string is:", ''.join(reversed(s))) #Space Usage: O(n)
l=list(s)
l.reverse()
print("reverse of the string is:", ''.join(l)) #Space Usage: O(n)
reverse_str = ""
for ch in s:
    reverse_str = ch + reverse_str
print("reverse of the string is:", reverse_str) #Space Usage: O(n²)