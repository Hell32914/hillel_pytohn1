import re

def first_word(text: str) -> str:
    """
    Знаходить перше слово в рядку, яке може містити апострофи.
    
    :param text: Вхідний текст
    :return: Перше слово, що містить тільки букви або апострофи
    """
    # Видаляємо початкові пробіли та знаки пунктуації, які не є частиною слова
    text = text.lstrip('., ')

    # Використовуємо регулярний вираз для знаходження першого слова
    match = re.match(r"[a-zA-Z']+", text)

    if match:
        return match.group(0)
    return ""


# Тестування функції
assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'

print('OK')

