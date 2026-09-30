#Putting objects into a class(template) Abstraction
#List of students' Names - Class Student

#properties (Member Variables)
#behavior - function - member functions act upon MV
#Abstraction
#Encapsulation
class Student:
    def _init_(self):   #Constructor
        self.id = ""
        self.name = ""
        self.department = ""
        self.age = ""

    def create_new_student (self):
        self.id = input("Enter Student ID: ")
        self.name = input("Enter Student name: ")
        self.department = input("Enter Student department: ")
        self.age = input("Enter Student age: ")

    def display_student (self):
        print("ID:", self.id)
        print("Name:", self.name)
        print("Dept:", self.department)
        print("Age:", self.age)


#Main Program
myStudents = []      #Store Student Objects
Stu = Student()

Stu.create_new_student()
Stu.display_student()

myStudents.append(Stu)     #New
Stu = Student()
Stu.create_new_student()
Stu.display_student()

myStudents.append(Stu)    #New
print(myStudents)

