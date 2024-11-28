import struct

student_format = "11s30s2si11sf"
student_size = struct.calcsize(student_format)
grades_format = "20s11sf"
grades_size = struct.calcsize(grades_format)
file='student.bin'
grades_file='grades.bin'
text_file='temp.bin'
def quit_program():
    print("Exiting the program.")

def add_student(file):
    roll_number = input("Enter roll_number: ")
    name = input("Enter name: ")
    department_code = input("Enter department code: ")
    semester = int(input("Enter semester: "))
    percent_marks = float(input("Enter last semester percent marks: "))
    phone_number = input("Enter phone number: ")
    roll_number = roll_number.encode('utf-8')[:11].ljust(11, b'\0')
    name = name.encode('utf-8')[:30].ljust(30, b'\0')
    department_code = department_code.encode('utf-8')[:2].ljust(2, b'\0')
    phone_number = phone_number.encode('utf-8')[:11].ljust(11, b'\0')

    if not check_duplicate(file, roll_number):
        student_data = struct.pack(student_format, roll_number, name, department_code, semester, phone_number, percent_marks)
        with open(file, 'ab') as fil:
            fil.write(student_data)
        print("Student added successfully!")
    else:
        print("Student with the same roll number already exists.")

def check_duplicate(file, roll_number):
    try:
        file=open(file,'rb')
    except FileNotFoundError:
        return False
    while True:
        data = file.read(student_size)
        if not data:
            break
        student = struct.unpack(student_format, data)
        if student[0].decode() == roll_number:
            file.close()
            return True
    file.close()
    return False
def student_by_rollno(file):
    roll_no=input("Enter roll no : ")
    file=open(file,'rb')
    while True:
        data=file.read(student_size)
        if not data:
            break
        student=struct.unpack(student_format,data)
        if student[0].decode()==roll_no:
            print(student[0].decode(),student[1].decode(),student[2].decode())
            file.close()
            break
def edit_student_by_rollno(file):
    roll_no = input("Enter roll no: ")
    updated_records = []
    with open(file, 'rb+') as f:
        while True:
            data = f.read(student_size)
            if not data:
                break
            student = struct.unpack(student_format, data)
            if student[0].decode() == roll_no:
                print("Student found. Enter updated details:")
                roll_number = input("Enter roll_number: ")
                name = input("Enter name: ")
                department_code = input("Enter department code: ")
                semester = int(input("Enter semester: "))
                percent_marks = float(input("Enter last semester percent marks: "))
                phone_number = input("Enter phone number: ")
                roll_number = roll_number.encode('utf-8')[:11].ljust(11, b'\0')
                name = name.encode('utf-8')[:30].ljust(30, b'\0')
                department_code = department_code.encode('utf-8')[:2].ljust(2, b'\0')
                phone_number = phone_number.encode('utf-8')[:11].ljust(11, b'\0')
                updated_student = struct.pack(student_format, roll_number, name, department_code, semester, phone_number, percent_marks)
                updated_records.append((len(data), updated_student))
            else:
                updated_records.append((len(data), data))

        f.seek(0)
        for record in updated_records:
            f.write(record[1])
        f.truncate()
def delete_student(file):
    roll_no = input("Enter roll no: ")
    updated_records = []
    with open(file, 'rb+') as f:
        while True:
            data = f.read(student_size)
            if not data:
                break
            student = struct.unpack(student_format, data)
            if student[0].decode() == roll_no:
                print("Student found and deleted.")
            else:
                updated_records.append((len(data), data))

        f.seek(0)
        for record in updated_records:
            f.write(record[1])
        f.truncate()
def student_by_semester(file):
    semesters = {}
    with open(file, 'rb') as f:
        while True:
            data = f.read(student_size)
            if not data:
                break
            student = struct.unpack(student_format, data)
            roll_no = student[0].decode()
            semester = student[1].decode()
            if semester in semesters:
                semesters[semester].append(roll_no)
            else:
                semesters[semester] = [roll_no]
    
    print("Students by Semester:")
    for semester, students in semesters.items():
        print("\nSemester:", semester)
        for student in students:
            print(student)

def list_students_by_name(file):
    with open(file, 'rb') as f:
        while True:
            data = f.read(student_size)
            if not data:
                break
            student = struct.unpack(student_format, data)
            print(student[1].decode())
def print_students_list(file):
    with open(file, 'rb') as f:
        while True:
            data = f.read(student_size)
            if not data:
                break
            student = struct.unpack(student_format, data)
            print(student[0].decode(), student[1].decode(), student[2].decode(), student[3], student[4])   
            
def add_grade(file, grades_file):
    roll_no = input("Enter roll no: ")
    course_code = input("Enter course code: ")
    grade = input("Enter grade: ")

    if not check_duplicate_grade(file, roll_no, course_code):
        grade_data = struct.pack(grades_format, roll_no.encode('utf-8'), course_code.encode('utf-8'), float(grade))
        with open(grades_file, 'ab') as f:
            f.write(grade_data + b'\n')
        print("Grade added successfully!")
    else:
        print("Duplicate grade found for the same student and course.")

def check_duplicate_grade(file, roll_no, course_code):
    try:
        file = open(file, 'rb')
    except FileNotFoundError:
        return False
    while True:
        data = file.read(grades_size)
        if not data:
            break
        grade = struct.unpack(grades_format, data)
        if grade[0].decode() == roll_no and grade[1].decode() == course_code:
            file.close()
            return True
    file.close()
    return False


def import_grades(file, grades_file, text_file):
    with open(text_file, 'r') as f:
        lines = f.readlines()

    for line in lines:
        values = line.strip().split('\t')
        roll_no = values[0]
        course_code = values[1]
        grade = values[2]

        if not check_duplicate_grade(file, roll_no, course_code):
            grade_data = struct.pack(grades_format, roll_no.encode('utf-8'), course_code.encode('utf-8'), float(grade))
            with open(grades_file, 'ab') as f:
                f.write(grade_data + b'\n')
            print("Grade added successfully!")
        else:
            print("Duplicate grade found for the same student and course.")

def view_grades_of_student(grades_file):
    roll_no = input("Enter roll no: ")
    with open(grades_file, 'rb') as f:
        while True:
            data = f.read(grades_size)
            if not data:
                break
            grade = struct.unpack(grades_format, data)
            if grade[0].decode() == roll_no:
                print(grade[0].decode(), grade[1].decode(), grade[2])

def edit_grades(grades_file, roll_no, course, new_marks):
    updated = False
    with open(grades_file, 'r+b') as f:
        while True:
            data = f.read(grades_size)
            if not data:
                break
            grade = struct.unpack(data)
            if grade[0] == course and grade[1] == roll_no:
                updated = True
                f.seek(-grades_size, 1)
                f.write(struct.pack(course, roll_no, new_marks))
                break
    
    if updated:
        print("Grades for Student", roll_no, "and Course", course, "have been updated.")
    else:
        print("No grades found for Student", roll_no, "and Course", course)


def delete_grades_of_student(grades_file, roll_no, course):
    deleted = False
    with open(grades_file, 'r+b') as f:
        while True:
            data = f.read(grades_size)
            if not data:
                break
            grade = struct.unpack(data)
            if grade[0] == course and grade[1] == roll_no:
                deleted = True
                f.seek(-grades_size, 1)
                f.write(b'\x00' * grades_size)
                break
    
    if deleted:
        print("Grades for Student", roll_no, "and Course", course, "have been deleted.")
    else:
        print("No grades found for Student", roll_no, "and Course", course)
    

def list_student_grade(file):
    student_rollno = input("Enter student roll no: ")
    with open(file, 'rb') as f:
        while True:
            data = f.read(grades_size)
            if not data:
                break
            grade = struct.unpack(grades_format, data)
            if grade[0].decode() == student_rollno:
                print(grade[1].decode(), grade[2])
                
def list_course_grade(file, course_code):
    print("Course Grade Sheet")
    print("Roll No\tGrade")
    with open(file, 'rb') as f:
        while True:
            data = f.read(grades_size)
            if not data:
                break
            grade = struct.unpack(grades_format, data)
            if grade[1].decode() == course_code:
                print(grade[0].decode(), "\t", grade[2])

def print_award_sheet(grades_file, course):
    with open(grades_file, 'rb') as f:
        print("Award Sheet for Course", course)
        print('--------------------------')
        while True:
            data = f.read(grades_size)
            if not data:
                break
            grade = struct.unpack(data)
            if grade[0] == course:
                print("Student Roll No:", grade[1])
                print("Percent Marks:", grade[2])
                
def print_summary_sheet(students_file, grades_file, course):
    print("Summary Sheet for Course", course)
    print('----------------------------')

    students = {}
    with open(students_file, 'rb') as f:
        while True:
            data = f.read(student_size)
            if not data:
                break
            student = struct.unpack(data)
            students[student[0]] = student[1:5] 

def generate_transcripts(students_file, grades_file):
    print("Transcripts for Students")
    print('----------------------------------------------------')
 
    students = {}
    with open(students_file, 'rb') as f:
        while True:
            data = f.read(student_size)
            if not data:
                break
            student = struct.unpack(grades_format,data)
            students[student[0]] = student[1]
def menu():
    print("1. Quit")
    print("2. Add student")
    print("3. view student by roll no ")
    print("4. edit student by roll no ")
    print("5. delete student by roll no ")
    print("6. list students by semester ")
    print("7. list students by name ")
    print("8. print students list ")
    print("9. Add grade ")
    print("10. import grades ")
    print("11. view grades of student ")
    print("12. edit grade of students ")
    print("13. delete grade of students ")
    print("14. List Student wise (1 student) grade of courses ")
    print("15. List Course wise grade (1 course) of students ")
    print("16. Award sheet ")
    print("17. Summary sheet ")
    print("18. Transcripts ")
def main():
    while True:
        menu()
        choice = int(input("Enter choice: "))
        if choice == 1:
            quit_program()
            break
        elif choice == 2:
            add_student(file)
        elif choice==3:
            student_by_rollno(file)
        elif choice==4:
            edit_student_by_rollno(file)
        elif choice==5:
            delete_student(file)
        elif choice==6:
            student_by_semester(file)
        elif choice==7:
            list_students_by_name(file)
        elif choice==8:
            print_students_list(file)
        elif choice==9:
            course_name=input()
            add_grade(file,course_name)
        elif choice==10:
            import_grades(file, grades_file, text_file)
        elif choice==11:
            view_grades_of_student(grades_file)
        elif choice==12:
            edit_grades(grades_file)
        elif choice==13:
            roll_no=input("Enter roll no ")
            course=input("Enter course ")
            delete_grades_of_student(grades_file,roll_no,course)
        elif choice==14:
            list_student_grade(file)    
        elif choice==15:
            course=input("Enter course ")
            list_course_grade(grades_file,course)
        elif choice==16:
            course=input("enter course ")
            print_award_sheet(grades_file,course)
        elif choice==17:
            course=input("Enter course ")
            print_summary_sheet(file,grades_file,course)
        elif choice==18:
            generate_transcripts(file,grades_file)
        else:
            print("Invalid input please enter again ")
            
if __name__ == "__main__":
    main()
