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
        print(mylist)

    elif choice == 2:
        element = int(input("Remove element"))
        mylist.remove(element)
        print(mylist)

    elif choice == 3:
        print("list all elements")
        print (mylist)

    elif choice == 4:
        mylist.sort()
        print(mylist)

    elif choice == 5:
        old_element = int(input("Enter the element you want to replace"))
        new_element = int(input("Enter new element"))

        index = 0
        for i in mylist:
            if i == old_element:
                break
            index = index + 1
        mylist[index] = new_element
        print (mylist)

    elif choice == 6:
        print(mylist)
        print("Exit")
        break






