def correct_sentence(text: str) -> str:
    # Перетворюємо текст на рядок + видаляємо пробіли на початку та в кінці
    text = str(text).strip()
    
    # Якщо тексту немає
    if not text:
        return ""
    
    # Щоб перша літера була велика
    cor_text = text[0].upper() + text[1:]
    
    # Додаємо крапку, якщо її немає
    if not cor_text.endswith('.'):
        cor_text += '.'
    
    return cor_text


# Перевірка роботи
assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'

print('ОК')
