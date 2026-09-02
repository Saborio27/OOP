while ("1"):
    print("1 are of a rectangle")
    print("2 volume of a cube")
    print("3 are of a circle")
    print("4 circumference of a circle")

    choice = input("Enter your choice: ")
    if choice == "1":
        length = int(input("Enter the length of the rectangle: "))
        width = int(input("Enter the width of the rectangle: "))
        area = length * width
        print(area)

    elif choice == "2":
        lenght = int(input("Enter the length of the cube: "))
        width = int(input("Enter the width of the cube: "))
        height = int(input("Enter the height of the cube: "))
        volume = lenght * width * height
        print(volume)

    elif choice == "3":
        radius = int(input("Enter the radius of the circle: "))
        area = 3.14 * radius * radius
        print(area)

    elif choice == "4":
        radius = int(input("Enter the radius of the circle: "))
        circumference = 2 * 3.14 * radius
        print(circumference)

    elif choice == "5":
        exit()
        





