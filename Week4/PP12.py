i = 1
students = {}
while True:

    print("1. Add student name")
    print("2. Remove student name")
    print("3. Edit student name")
    print("4. Print student name")
    print("5. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter student name: ")
        major = input("Enter student major: ")
        year = input("Which year?")

        students.update({"s"+str(i):
                                    {
                                        "stu_name":name,
                                        "stu_major":major,
                                        "stu_year":year
                                    }

                        })
        i = i+1

    elif choice == "2":
        number = input("Enter student number that you want to remove: ")
        del students["s"+number]





