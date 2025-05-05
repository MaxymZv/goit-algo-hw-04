from data import get_file_info
'''
Це була наскладніша яастина для мене,
тому що я не міг опрацювати данні в списку, 
завджди поверталось None, або 1000
'''

def total_salary(Path: str) -> int: # Приймає шлях до файлу
    try: # намагається опрацювати файл
        salary_data = get_file_info(Path) # отримує вміст файлу
        salary = [] # створює пустий список для зберігання зарплат
        for line in salary_data: # проходить по кожному рядку вмісту файлу
            salary_items = line.strip().replace("\n", ",").split(',') # видаляє пробіли, заміняє символ нового рядка на кому, та розділяє рядки комами
            salary_numbers = [int(i) for i in salary_items if i.isdigit()] # перетворює рядки в числа, якщо це можливо
            salary.extend(salary_numbers) # додає числа до списку зарплат
        if salary: # перевіряє чи список зарплат не пустий
            sum_salary = sum(salary) # обчислює суму зарплат
            avarage_salary = sum_salary // len(salary) # обчислює середню зарплату
            return sum_salary, avarage_salary # повертає суму та середню зарплату
    except ZeroDivisionError: # якщо ділення на нуль
        return ZeroDivisionError("На нуль неможливо ділити") # повертає помилку

total, avarage = total_salary('hw01/salary.txt') # викликає функцію з файлом salary.txt

print(f'Загальна сума зарплат: {total},\nСередня зарплата: {avarage}') # виводить загальну та середню зарплату


