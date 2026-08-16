try :
    marks=int(input("enter your marks:"))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()

if marks<0 or marks>100:
    print("Invalid marks. Please enter a number between 0 and 100.")
    exit()

if marks>=90:
    print("Grade: A")
    print("status: passed")
elif marks>=75:
    print("Grade: B")
    print("status: passed")
elif marks>=50:
    print("Grade: C")
    print("status: passed") 
else:
    print("Grade: Fail")
    print("status: failed")
