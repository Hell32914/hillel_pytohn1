from student import Student

class Group:
    def __init__(self, number: str) -> None:
        self.number = number
        self.group: set[Student] = set()

    def add_student(self, student: Student) -> None:
        if len(self.group) >= 10:
            raise Exception("Неможливо додати більше 10 студентів до групи")
        self.group.add(student)

    def delete_student(self, last_name: str) -> None:
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name: str) -> Student | None:
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self) -> str:
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Група: {self.number}\nСтуденти:\n{all_students}'
