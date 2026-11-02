
# STUDENT STUDY & GRADE TRACKER
# Version 1.1 - Class Management



class StudentClass:
    def __init__(self, name, credits):
        self.name = name
        self.credits = credits
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def display_info(self):
        print(self.name, "-", self.credits, "credits")

    def display_grades(self):
        print("Grades for", self.name)

        if len(self.grades) == 0:
            print("No grades entered yet.")
        else:
            for grade in self.grades:
                print("Grade:", grade)

    def calculate_average(self):
        if len(self.grades) == 0:
            return None
        else:
            total = sum(self.grades)
            average = total / len(self.grades)
            return average



# List to store class objects
classes = []

print("STUDENT STUDY & GRADE TRACKER")

while True:
    print("1. Add Class")
    print("2. View Classes")
    print("3. Calculate Class Average")
    print("4. Determine Letter Grade")
    print("5. Calculate GPA")
    print("6. Enter Grades")
    print("7. View Grades")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("ADD CLASS")

        name = input("Enter class name: ")
        credits = float(input("Enter credit hours: "))

        if credits > 0:
            new_class = StudentClass(name, credits)
            classes.append(new_class)
            print("Class added successfully!")
        else:
            print("Invalid credit hours.")

    elif choice == "2":
        print("MY CLASSES")

        if len(classes) == 0:
            print("No classes added yet.")
        else:
            for i in range(len(classes)):
                print(i + 1, end=". ")
                classes[i].display_info()



    elif choice == "3":
        print("CLASS AVERAGE")

        if len(classes) == 0:
            print("No classes available. Add a class first.")
        else:
            for i in range(len(classes)):
                print(i + 1, "-", classes[i].name)

            selection = int(input("Select a class number: "))

            if selection >= 1 and selection <= len(classes):
                selected_class = classes[selection - 1]

                average = selected_class.calculate_average()

                if average is None:
                    print("No grades entered for this class.")
                else:
                    print("Class:", selected_class.name)
                    print("Class Average:", round(average, 2), "%")

                    if average >= 90:
                        print("Letter Grade: A")
                    elif average >= 80:
                        print("Letter Grade: B")
                    elif average >= 70:
                        print("Letter Grade: C")
                    elif average >= 60:
                        print("Letter Grade: D")
                    else:
                        print("Letter Grade: F")

            else:
                print("Invalid class selection.")


    elif choice == "4":
        print("LETTER GRADE")

        grade = float(input("Enter your percentage: "))

        if grade >= 90:
            print("Letter Grade: A")
        elif grade >= 80:
            print("Letter Grade: B")
        elif grade >= 70:
            print("Letter Grade: C")
        elif grade >= 60:
            print("Letter Grade: D")
        else:
            print("Letter Grade: F")

    elif choice == "5":
        print("GPA CALCULATOR")

        total_points = 0
        total_credits = 0

        num_classes = int(input("How many classes do you have? "))

        for i in range(num_classes):
            print("Class", i + 1)

            class_name = input("Enter class name: ")
            letter = input("Enter letter grade (A-F): ").upper()
            credits = float(input("Enter credit hours: "))

            if letter == "A":
                points = 4.0
            elif letter == "B":
                points = 3.0
            elif letter == "C":
                points = 2.0
            elif letter == "D":
                points = 1.0
            elif letter == "F":
                points = 0.0
            else:
                print("Invalid letter grade.")
                continue

            if credits <= 0:
                print("Invalid credit hours.")
                continue

            total_points += points * credits
            total_credits += credits

            print(class_name, "added to GPA calculation!")

        if total_credits > 0:
            gpa = total_points / total_credits

            print("GPA SUMMARY")
            print("Total Credit Hours:", total_credits)
            print("Estimated Semester GPA:", round(gpa, 2))
        else:
            print("No valid classes entered.")



    elif choice == "6":

        print("ENTER GRADES")

        if len(classes) == 0:

            print("No classes available. Add a class first.")

        else:

            for i in range(len(classes)):
                print(i + 1, "-", classes[i].name)

            selection = int(input("Select a class number: "))

            if selection >= 1 and selection <= len(classes):

                selected_class = classes[selection - 1]

                grade = float(input("Enter grade (0-100): "))

                if grade >= 0 and grade <= 100:

                    selected_class.add_grade(grade)

                    print("Grade saved for", selected_class.name)

                else:

                    print("Invalid grade.")


            else:

                print("Invalid class selection.")


    elif choice == "7":

        print("VIEW GRADES")

        if len(classes) == 0:

            print("No classes available.")

        else:

            for i in range(len(classes)):
                print(i + 1, "-", classes[i].name)

            selection = int(input("Select a class number: "))

            if selection >= 1 and selection <= len(classes):

                selected_class = classes[selection - 1]

                selected_class.display_grades()

            else:

                print("Invalid class selection.")


    elif choice == "8":

        print("Thank you for using Student Study & Grade Tracker!")

        break


    else:
        print("Invalid option. Please try again.")
