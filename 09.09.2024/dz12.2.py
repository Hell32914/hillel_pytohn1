from typing import Dict

class Item:
    def __init__(self, name: str, price: int, description: str, dimensions: str):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self) -> str:
        return f"{self.name}, price: {self.price}"


class User:
    def __init__(self, name: str, surname: str, numberphone: str):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self) -> str:
        return f"{self.name} {self.surname}, phone: {self.numberphone}"


class Purchase:
    def __init__(self, user: User):
        self.products: Dict[Item, int] = {}
        self.user = user
        self.total = 0  # Додаємо поле для загальної вартості

    def add_item(self, item: Item, cnt: int) -> None:
        self.products[item] = cnt  # Без перевірки, просто додаємо товар з кількістю

    def get_total(self) -> int:
        self.total = 0
        for item, cnt in self.products.items():
            self.total += item.price * cnt  # Ціна товару * кількість
        return self.total

    def __str__(self) -> str:
        result = f"User: {self.user.name} {self.user.surname}\n"
        result += "Items:\n"
        for item, cnt in self.products.items():
            result += f"{item.name}: {cnt} pcs.\n"
        return result


# Тестування

lemon = Item('lemon', 5, "yellow", "small")
apple = Item('apple', 2, "red", "middle")

print(lemon)  # lemon, price: 5

buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)  # Ivan Ivanov

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 20 pcs.
"""

assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
assert cart.get_total() == 60, "Всього 60"
assert cart.get_total() == 60, 'Повинно залишатися 60!'

# Оновлення кількості яблук
cart.add_item(apple, 10)  # Оновлюємо кількість яблук
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 10 pcs.
"""

assert cart.get_total() == 40, 'Повинно бути 40 після зміни кількості яблук'
