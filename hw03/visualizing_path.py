import sys  #Імпортуєм модуль sys для роботи з аргументами коммандоного рядка
from pathlib import Path #Імпортуємо клас Pathз модуля pathlib для роботи з шляхами
import colorama #Імпортуємо модуль для кольорового виводу в термінал

#Сортувальна функція
def sort_function(item):
      return (item.is_file(), item.name.lower()) #Сортує елементи за типом (файл чи папка) та за назвою в нижньому регістрі

#Функція для візуалізації шляху до директороії з кольоровим виводом
def visualize_directory(directory_path: str, indent: int = 0):
    directory_path = Path(directory_path).resolve() #Перетворює рядок у об'єкт Path та отримує абсолютний шлях
    if not directory_path.exists() or not directory_path.is_dir(): #Перевіряє чи існує директорія та чи є вона папкою
            return colorama.Fore.RED + f'Папка {directory_path} не існує.' + colorama.Style.RESET_ALL #Якщо не існує, повертає повідомлення про помилку
    for item in sorted(directory_path.iterdir(), key=sort_function): #Перебирає всі елементи в директорії, сортує їх за допомогою функції sort_function
        prefix = "  " * indent #Створює префікс для відступу
        if item.is_dir(): #Якщо елемент є директорією
            print(prefix + colorama.Fore.BLUE + f'{item.name}' + colorama.Style.RESET_ALL) #Виводить назву директорії
            visualize_directory(item, indent + 1) #Рекурсивно викликає функцію для візуалізації вмісту директоріїї
        else: 
            print(prefix + colorama.Fore.GREEN + f'{item.name}' + colorama.Style.RESET_ALL) #Якщо елемент є файлом, виводить його назву


if __name__ =='__main__':
    if len(sys.argv) != 2: #Перевіряє чи передано правильну кількість аргументів
        print(colorama.Fore.RED + "Використання: visualizing_path.py <шлях_до_директорії>" + colorama.Fore.RESET) #Виводить повідомлення про помилку
    else:
     visualize_directory(sys.argv[1]) #Викликає функцію для візуалізації директорії, передаючи шлях з аргументів командного рядка
          
        
        
        
