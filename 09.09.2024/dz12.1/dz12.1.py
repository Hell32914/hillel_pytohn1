import codecs
import re
from pathlib import Path
from typing import Optional


def delete_html_tags(html_file: str, result_file: Optional[str] = 'cleaned.txt') -> None:
    """Видаляє HTML-теги з файлу та записує очищений текст у новий файл."""
    
    # Отримання шляху до папки зі скриптом
    current_dir = Path(__file__).parent
    
    # Створення повного шляху до файлу
    html_file_path = current_dir / html_file
    result_file_path = current_dir / result_file
    
    # Читання HTML-файлу
    with codecs.open(html_file_path, 'r', 'utf-8') as file:
        html = file.read()
    
    # Видалення HTML-тегів за допомогою "нелюблячого" регулярного виразу
    clean_text = re.sub(r'<[^>]+?>', '', html)
    
    # Видалення порожніх рядків
    lines = clean_text.splitlines()
    non_empty_lines = [line for line in lines if line.strip() != '']
    cleaned_text = '\n'.join(non_empty_lines)
    
    # Запис очищеного тексту у новий файл
    with codecs.open(result_file_path, 'w', 'utf-8') as output_file:
        output_file.write(cleaned_text)

# Виклик функції
delete_html_tags('draft.html')