try:
    x = float(input("Enter a number: "))
    y = float(input("Enter a number: "))
    ch = input("Enter an operation (+, -, *, /): ")
    if ch == '+':
        print(x + y)
    elif ch == '-':
        print(x - y)
    elif ch == '*':
        print(x * y)
    elif ch == '/':
        if y == 0:
         print("Error: Division by zero is not allowed.")
    else:
        print(x/y)
except ValueError:
    print("Error: Invalid input. Please enter numeric values.")