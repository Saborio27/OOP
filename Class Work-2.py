mylist = []

while True:
    print("1. Add an element")
    print("2. Remove an element")
    print("3. List all elements")
    print("4. Sort the list")
    print("5. Replace an element")
    print("6. Exit")

    choice = int(input("Enter your choice"))

    if choice == 1:
        element = int(input("Enter element"))
        mylist.append(element)
    elif choice == 2:
        element = int(input("Remove element"))
        mylist.remove(element)




mylist.sort()