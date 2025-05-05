from pathlib import Path

def get_cats_info(file_path: str): # створюємо функцію cats_infо, яка приймає шлях до файлу

    get_cats_info = [] # створюємо пустий словник для зберігання інформації
    file = Path(file_path).resolve() # визначаємо шлях до файлу
    try:      # намагаємось опрацювати код
        with file.open('r', encoding='utf-8') as f: # відкриваємо файл
            for line in f: # проходимось по кожному рядку
                cat_data = line.strip().split(',') # видаляємо пробіли та розділяємо рядки комами
                if len(cat_data) == 3: # перевіряємо чи рядок містить 3 елементи
                    cat_dict = {'id': cat_data[0], # створюємо словник з інформацією про котів
                                 'name': cat_data[1],
                                 'age': cat_data[2]}
                    get_cats_info.append(cat_dict) # додаємо словник до списку
            return get_cats_info # повертаємо список з інформацією про котів
    except FileNotFoundError: # якщо файл не знайдено
        return FileNotFoundError(f'Файл {Path} не знайдено.') # повертаємо помилку
    
print(get_cats_info('hw02/cats.txt')) # викликаємо функцію з файлом cats.txt
