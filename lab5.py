class Department:
    def __init__(self, name, chairman, dept_id):
        self.name = name
        self.chairman = chairman
        self.dept_id = dept_id

    def __str__(self):
        return f"{self.dept_id}, {self.name}, {self.chairman}"


class Student:
    def __init__(self, name, roll_number, semester, cgpa, department_id):
        self.name = name
        self.roll_number = roll_number
        self.semester = semester
        self.cgpa = cgpa
        self.department_id = department_id

    def __str__(self):
        return f"{self.roll_number} {self.name} {self.semester} {self.cgpa}"
def main():
    departments = [
        Department("Computer Science", "Dr. Jodat Kamal", "CS"),
        Department("Data Science", "Dr. Saad Kamal", "DS"),
        Department("Information Technology", "Dr. Abbas Ali", "IT"),
        Department("Software Engineering", "Dr. Talha Kamal", "SE")
    ]

    students = [
        Student("Noman Fareed", "XXXXXXXX", 1, 3.08, "CS"),

    ]

    for dept in departments:
        print(f"Department: {dept}")
        print("Roll No", "Name", "Semester", "CGPA", sep="\t\t\t")
        for student in students:
            if student.department_id == dept.dept_id:
                print(student.roll_number, student.name, student.semester, student.cgpa, sep="\t\t")
        print()
    print("\nStudents with CGPA less than 1.70:")
    for student in students:
        if student.cgpa < 1.70:
            print(student)

if __name__ == "__main__":
    main()
