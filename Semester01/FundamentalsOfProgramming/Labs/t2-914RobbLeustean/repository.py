from student import Student

class StudentRepository:
    def __init__(self, file_name):
        self.file_name = file_name
        self.students = self.load_students()

    def load_students(self):
        try:
            with open(self.file_name, 'r') as file:
                students = []
                for line in file:
                    data = line.strip().split(', ')
                    student = Student(int(data[0]), data[1], int(data[2]), int(data[3]))
                    students.append(student)
                return students
        except FileNotFoundError:
            return []

    def save_students(self):
        with open(self.file_name, 'w') as file:
            for student in self.students:
                file.write(f"{student.student_id}, {student.name}, {student.attendance_count}, {student.grade}\n")

    def add_student(self, student):
      existing_ids = {s.student_id for s in self.students}
      if student.student_id in existing_ids:
            print(f"Error: ID {student.student_id} is already assigned to a student.")
            return
         
      self.students.append(student)
      self.save_students()

    def get_students_sorted_by_grade(self):
        sorted_students = sorted(self.students, key=lambda x: (-x.grade, x.name))
        return sorted_students

    def apply_bonus(self, p, b):
        for student in self.students:
            if student.attendance_count >= p:
                student.grade = min(10, student.grade + b)
        self.save_students()

    def get_students_by_name(self, search_string):
        filtered_students = [student for student in self.students if search_string.lower() in student.name.lower()]
        sorted_students = sorted(filtered_students, key=lambda x: x.name)
        return sorted_students
