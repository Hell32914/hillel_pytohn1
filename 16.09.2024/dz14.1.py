class GroupLimitError(Exception):
    """Виняток, що піднімається при спробі додавання більше 10 студентів до групи."""
    def __init__(self, message: str) -> None:
        super().__init__(message)


class Human:
    def __init__(self, gender: str, age: int, first_name: str, last_name: str) -> None:
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}, {self.age} років, стать: {self.gender}"


class Student(Human):
    def __init__(self, gender: str, age: int, first_name: str, last_name: str, record_book: str) -> None:
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self) -> str:
        main_info = super().__str__()
        return f"{main_info}, залікова книжка: {self.record_book}"


class Group:
    def __init__(self, number: str) -> None:
        self.number = number
        self.group: set[Student] = set()

    def add_student(self, student: Student) -> None:
        if len(self.group) >= 10:
            raise GroupLimitError("Група вже містить 10 студентів. Немає можливості додати більше.")
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


# Приклади використання
st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 20, 'John', 'Doe', 'AN143')
st4 = Student('Female', 23, 'Anna', 'Smith', 'AN144')
st5 = Student('Male', 21, 'Peter', 'Parker', 'AN146')
st6 = Student('Male', 22, 'Bruce', 'Wayne', 'AN147')
st7 = Student('Female', 20, 'Natasha', 'Romanoff', 'AN148')
st8 = Student('Male', 22, 'Tony', 'Stark', 'AN149')
st9 = Student('Male', 24, 'Clark', 'Kent', 'AN150')
st10 = Student('Female', 23, 'Diana', 'Prince', 'AN151')
st11 = Student('Male', 25, 'Barry', 'Allen', 'AN152')

gr = Group('PD1')

try:
    # Додаємо 10 студентів
    gr.add_student(st1)
    gr.add_student(st2)
    gr.add_student(st3)
    gr.add_student(st4)
    gr.add_student(st5)
    gr.add_student(st6)
    gr.add_student(st7)
    gr.add_student(st8)
    gr.add_student(st9)
    gr.add_student(st10)
    
    print(gr)  # Вивести список студентів

    # Спроба додати 11-го студента, що викличе виняток
    gr.add_student(st11)
except GroupLimitError as e:
    print(f"Помилка: {e}")
