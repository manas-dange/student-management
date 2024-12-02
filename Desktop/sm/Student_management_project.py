class Student:
    def __init__(self, name, roll_no, marks);
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

class StudentSystem:
    def __init__(self):
        self.students = []

    def add_student(self, name, roll_no, marks):
        student = Student(name, roll_no, marks)
        self.students.append(student)
        print(f"Student {name} added successfully!")

    def display_info(self):
        if not self.students:
            print("No records found.")
            return
        for student in self.students:
            print(f"Name: {student.name}, Roll No: {student.roll_no}, Marks: {student.marks}")

    def search_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                print(f"Student found: Name: {student.name}, Roll No: {student.roll_no}, Marks: {student.marks}")
                return
        print("No student found with that roll number.")

    def remove_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                self.students.remove(student)
                print(f"Student with Roll No {roll_no} removed successfully!")
                return
        print("No student found with that roll number.")

    def total_no_student(self):
        print(f"Total number of students: {len(self.students)}")
sms = StudentSystem()

while True:
    print("""\n1. Add Student
2. Display All Students
3. Search Student
4. Remove Student
5. Total Number of Student
6. Exit""")
    enter = int(input("Enter what you want to do: "))
    
    if enter == 1:
        a = input("Enter the name of the student: ")
        b = input("Enter the roll number of the student: ")
        c = input("Enter the marks of the student: ")
        sms.add_student(a, b, c)
    elif enter == 2:
        sms.display_info()
    elif enter == 3:
        d = input("Enter the roll number: ")
        sms.search_student(d)
    elif enter == 4:
        e = input("Enter the roll number: ")
        sms.remove_student(e)
    elif enter == 5:
        sms.total_no_student()
    elif enter == 6:
        print("Thanks for using the Student Management System!")
        break
    else:
        print("Invalid choice. Please try again.")
