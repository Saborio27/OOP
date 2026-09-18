#Menu-driven to implement Add, del, replace

i = 1
mycourses = {}
while True:

    print("1. Add course")
    print("2. Remove course")
    print("3. Replace course")
    print("4. Print course")
    print("5. Exit")

    choice = input("enter your choice:")
    if choice == 1:
        course_name = int(input("Enter course_name"))
        mycourses.update({"c"+str(i):course_name})
        i = i+1
        print(mycourses)

    elif choice == 2:
        index = input("Enter the index of the Remove mycourse")
        del mycourses["c"+index]
        print(mycourses)

    elif choice == 3:
        old_course = int(input("Enter the course you want to replace"))
        new_course = int(input("Enter new course"))

        index = 0
        for i in mycourses:
            if i == old_course:
                break
            index = index + 1
        mycourses[index] = new_course
        print(mycourses)

    elif choice == 4:
        print(mycourses)


    elif choice == 5:
        print("Exit")


course_name = int(input("Enter the name for the course "))

mycourses.update({"course_name"+str(i):course_name})
i = i + 1
print(mycourses)






