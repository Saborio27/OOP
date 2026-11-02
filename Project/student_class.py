
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
