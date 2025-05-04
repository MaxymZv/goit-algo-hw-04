from pathlib import Path

def get_file_info(file_path): #Приймає шлях до файлу
    file = Path(file_path).resolve() #Визнчає шлях до файлу
    try: # Намагаэться відкрити файлу і опрацювати його
        if file.exists(): #перевіряє чи існцє файл
            with file.open('r', encoding='utf-8') as file: #відкриває файлу
                content = file.read().strip().replace('\n',',').split(',') #зчитує вміст файлу, видаляє пробіли, заміняє символ нвого рядка на кому, та розділяє рядки комами
            return content #повертає вміст файлу
    except FileNotFoundError: #якщо файл не знайдено
        return FileNotFoundError(f"File {file_path} not found.") #повертає помилку
    

    




    
