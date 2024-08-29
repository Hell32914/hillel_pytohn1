from typing import List, Dict

def popular_words(text: str, words: List[str]) -> Dict[str, int]:

    # Приводимо текст до нижнього регістру та розділяємо на слова
    text = text.lower()
    word_list = text.split()
    
    # Створюємо словник для зберігання частот
    word_count = {}
    
    # Підраховуємо частоту кожного слова зі списку
    for word in words:
        # Рахуємо кількість входжень слова в тексті
        count = word_list.count(word)
        # Додаємо до словника
        word_count[word] = count
    
    return word_count

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')
