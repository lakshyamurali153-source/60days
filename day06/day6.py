with open("fizzbuzz.txt", "w") as f:
   x=int(input("Enter a integer number: "))
   for i in range(1,x+1):
     if i % 3 == 0 and i % 5 == 0:
        f.write("fizzbuzz\n")
     elif i % 3 == 0:
        f.write("fizz\n")
     elif i % 5 == 0:
        f.write("buzz\n")
     else:
        f.write(f"{i}\n")