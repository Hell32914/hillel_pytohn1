from human import Human

class Student(Human):
    def __init__(self, gender: str, age: int, first_name: str, last_name: str, record_book: str) -> None:
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self) -> str:
        main_info = super().__str__()
        return f"{main_info}, залікова книжка: {self.record_book}"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Student):
            return str(self) == str(other)
        return False

    def __hash__(self) -> int:
        return hash(str(self))
