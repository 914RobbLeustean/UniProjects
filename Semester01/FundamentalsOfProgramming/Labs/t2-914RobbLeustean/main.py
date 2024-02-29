from student import Student
from repository import StudentRepository
from service import StudentService
from ui import StudentUI

def main():
    file_name = "students.txt"
    student_repository = StudentRepository(file_name)
    student_service = StudentService(student_repository)
    student_ui = StudentUI(student_service)

    while True:
        print("\nMenu:")
        print("1. Add a new student")
        print("2. Display all students in decreasing order of their grade")
        print("3. Give bonuses to students")
        print("4. Display students whose name includes a given string")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            student_ui.add_new_student()
        elif choice == "2":
            student_ui.display_students_sorted_by_grade()
        elif choice == "3":
            student_ui.give_bonuses_to_students()
        elif choice == "4":
            student_ui.display_students_by_name()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
