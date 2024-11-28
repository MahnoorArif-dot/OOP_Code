class Person:
    def __init__(self, name, contact_number):
        self.name = name
        self.contact_number = contact_number

class Student(Person):
    def __init__(self, name, contact_number, department, semester):
        Person.__init__(self,name, contact_number)
        self.department = department
        self.semester = semester

class Teacher(Person):
    def __init__(self, name, contact_number, course, office_number):
        Person.__init__(self,name, contact_number)
        self.course = course
        self.office_number = office_number

class TA(Teacher, Student):
    def __init__(self, name, contact_number, course, office_number, department, semester):
        Student.__init__(self, name, contact_number, department, semester)
        Teacher.__init__(self, name, contact_number, course, office_number)

    def __str__(self):
        return f'TA(name={self.name}, contact_number={self.contact_number}, Course={self.course}, Office_Number={self.office_number}, Department={self.department}, Semester={self.semester})'

def main():
    p = TA('Aliya', 123, "IT", 2, "Computer Science", 3)
    print(p)

if __name__ == "__main__":
    main()
