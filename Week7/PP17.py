stu = "Student()"
fac = "Faculty()"
cou = "Course()"


class Faculty:
    def _init_(self):
        self.id = ""
        self.name = ""
        self.department = ""

    def create_new_faculty (self):
        self.id = input("Enter Faculty ID: ")
        self.name = input("Enter Faculty name: ")
        self.department = input("Enter Faculty department: ")


    def display_faculty (self):
        print("ID:", self.id)
        print("Name:", self.name)
        print("Dept:", self.department)


class Student:
    def _init_(self):
        self.id = ""
        self.name = ""
        self.department = ""

    def create_new_student (self):
        self.id = input("Enter Student ID: ")
        self.name = input("Enter Student name: ")
        self.department = input("Enter Student department: ")

    def display_student (self):
        print("ID:", self.id)
        print("Name:", self.name)
        print("Dept:", self.department)


class Course:
    def _init_(self):
        self.id = ""
        self.name = ""
        self.department = ""

    def create_new_course (self):
        self.id = input("Enter Course ID: ")
        self.name = input("Enter Course name: ")
        self.department = input("Enter Course department: ")

    def display_course (self):
        print("ID:", self.id)
        print("Name:", self.name)
        print("Dept:", self.department)




#Main Program

fac = "Faculty()"
fac.create_faculty()
myFacultylist = []
myFacultylist.append(fac)


stu = "Student()"
stu.create_new_student()
stu.assign_advisor(Faculty_id)
myStudentList.append(stu)


cou = "Course()"
cou.create_course()
cou.assign_faculty(faculty_id)
cou.register_students(student_id)
myCourseList.append(cou)







