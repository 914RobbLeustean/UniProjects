from service import StudentService
from student import Student

class StudentUI:
    def __init__(self, service):
        self.service = service

    def display_students_sorted_by_grade(self):
        students = self.service.get_students_sorted_by_grade()
        if not students:
            print("No students found.")
            return

        print("Students in decreasing order of their grade:")
        for student in students:
            print(f"ID: {student.student_id}, Name: {student.name}, Attendances: {student.attendance_count}, Grade: {student.grade}")

    def give_bonuses_to_students(self):
        p = int(input("Enter the minimum attendance count for bonus: "))
        b = int(input("Enter the bonus amount: "))
        self.service.give_bonuses(p, b)
        print("Bonuses given successfully.")

    def display_students_by_name(self):
        search_string = input("Enter the string to search in student names: ")
        students = self.service.get_students_by_name(search_string)
        if not students:
            print("No students found with the given search string.")
            return

        print(f"Students with names containing '{search_string}', ordered by name:")
        for student in students:
            print(f"ID: {student.student_id}, Name: {student.name}, Attendances: {student.attendance_count}, Grade: {student.grade}")

    def add_new_student(self):
        try:
            student_id = int(input("Enter student ID: "))
            name = input("Enter student name (at least 2 words, separated by space): ")
            attendance_count = int(input("Enter attendance count: "))
            grade = int(input("Enter grade (between 0 and 10): "))

            if len(name.split()) < 2 or len(name.split()[0]) < 3 or len(name.split()[1]) < 3:
                print("Error: Name must have at least 2 words with each word having at least 3 characters.")
                return
            if attendance_count <= 0:
                print("Error: Attendance count must be a positive integer.")
                return
            if not (0 <= grade <= 10):
                print("Error: Grade must be between 0 and 10.")
                return

            new_student = Student(student_id, name, attendance_count, grade)
            self.service.add_new_student(new_student)
            print("New student added successfully.")
        except ValueError:
            print("Error: Invalid input.")
