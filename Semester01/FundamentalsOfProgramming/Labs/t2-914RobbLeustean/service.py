from repository import StudentRepository

class StudentService:
    def __init__(self, repository):
        self.repository = repository

    def add_new_student(self, student):
        self.repository.add_student(student)

    def get_students_sorted_by_grade(self):
        return self.repository.get_students_sorted_by_grade()

    def give_bonuses(self, p, b):
        self.repository.apply_bonus(p, b)

    def get_students_by_name(self, search_string):
        return self.repository.get_students_by_name(search_string)
