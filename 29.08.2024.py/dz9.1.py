from typing import List, Dict
from collections import Counter

def popular_words(text: str, words: List[str]) -> Dict[str, int]:
    """
    Підраховує частоту появи слів з заданого списку в тексті.

    :param text: Вхідний текст.
    :param words: Список слів для перевірки.
    :return: Словник, де ключі - слова, а значення - їх частота в тексті.
    """
    # Приводимо текст до нижнього регістру та розділяємо на слова
    text = text.lower()
    word_list = text.split()
    
    # Підраховуємо частоти всіх слів у тексті
    word_counter = Counter(word_list)
    
    # Формуємо словник частот для заданих слів
    word_count = {word: word_counter.get(word, 0) for word in words}
    
    return word_count

# Тестування функції
assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
print('OK')
