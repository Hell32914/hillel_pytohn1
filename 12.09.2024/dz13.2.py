class Counter:
    def __init__(self, current: int = 1, min_value: int = 0, max_value: int = 10) -> None:
        self.current = current
        self.min_value = min_value
        self.max_value = max_value

    def set_current(self, start: int) -> None:
        """Встановлює поточне значення лічильника."""
        self.current = start

    def set_max(self, max_value: int) -> None:
        """Встановлює максимальне значення лічильника."""
        self.max_value = max_value

    def set_min(self, min_value: int) -> None:
        """Встановлює мінімальне значення лічильника."""
        self.min_value = min_value

    def step_up(self) -> None:
        """Збільшує значення лічильника на 1, якщо не досягнуто максимуму."""
        if self.current >= self.max_value:
            raise ValueError("Досягнуто максимуму")
        self.current += 1

    def step_down(self) -> None:
        """Зменшує значення лічильника на 1, якщо не досягнуто мінімуму."""
        if self.current <= self.min_value:
            raise ValueError("Досягнуто мінімуму")
        self.current -= 1

    def get_current(self) -> int:
        """Повертає поточне значення лічильника."""
        return self.current


# Тести для перевірки
counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()
assert counter.get_current() == 10, 'Test1'

try:
    counter.step_up()  # ValueError
except ValueError as e:
    print(e)  # Достигнуто максимуму
assert counter.get_current() == 10, 'Test2'

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()
assert counter.get_current() == 7, 'Test3'

try:
    counter.step_down()  # ValueError
except ValueError as e:
    print(e)  # Достигнуто мінімуму
assert counter.get_current() == 7, 'Test4'