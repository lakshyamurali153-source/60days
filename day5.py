user="admin"
attempts=0
while attempts < 3:
    x = input("enter username: ")
    y = input("enter password: ")
    if x == user and y == "admin123":
        print("login successful")
        break
    attempts += 1
    print("login failed, attempts left:", 3 - attempts)
else:
    print("login failed")