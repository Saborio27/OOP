def add():
    a = int(input())
    b = int(input())
    c = a+b
    print(c)

def subtract():
    a = int(input())
    b = int(input())
    c = a-b
    print(c)

def multiply():
    a = int(input())
    b = int(input())
    c = a*b
    print(c)

def divide():
    a = int(input())
    b = int(input())
    c = a/b
    print(c)

choice = input("Enter your choice: ")
if choice == "1":
    add()

elif choice == "2":
    subtract()

elif choice == "3":
    multiply()

elif choice == "4":
    divide()
