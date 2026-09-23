mystudents={}

def add_student():
    name = input("Enter student name:")
    lab1 = int(input("Enter lab 1:"))
    lab2 = int(input("Enter lab 2:"))
    lab3 = int(input("Enter lab 3:"))
    lab4 = int(input("Enter lab 4:"))
    lab5 = int(input("Enter lab 5:"))
    Total = lab1 + lab2 + lab3 + lab4 + lab5
    Percetage = (Total / 50) * 100
    Average = Total / 5


    mystudents.update({"student1": {"name": name, "Lab1":lab1, [lab1, lab2, lab3, lab4, lab5]}})

def delete_student():
    mystudents.pop(student)
    name = input("Enter student name:")
    lab1 = int(input("Enter grade lab 1 to delete:"))
    lab2 = int(input("Enter grade lab 2 to delete:"))
    lab3 = int(input("Enter grade lab 3 to delete:"))
    lab4 = int(input("Enter grade lab 4 to delete:"))
    lab5 = int(input("Enter grade lab 5 to delete:"))
    Percentage = int(input("Enter percentage to delete:"))
    Averge = int(input("Enter average grade to delete:"))


while True:
    print("1:Enter Student")
    print("2:Enter Delete Student")
    print("3:Enter Display Student")
    print("4:Enter Exit")

    choice= (input("Enter choice:")
        if choice == 1
            name = input("Enter Student name")

        elif choice == 2
            name = input("Delete Student name")

        elif choice == 3
            name = input("Display Student name")

        elif choice == 4
            name = input("Exit)")

















