
# Функція для парсингу введеного рядка
def parse_input(user_input):                           
    cmd, *args = user_input.split()                      #Розділяє введений користувачем рядок на команду та розпаковані аргументи
    cmd = cmd.lower().strip()                            #Перетворює команду на нижній регістр та видаляє пробіли
    return cmd, *args                                    #Повертає команду та аргументи

# Функція додавання контактів
def add_contacts(args, contacts): 
    name, phone = args                                   #Приймає як аргументи ім'я контакту та його номер
    contacts[name] = phone                               #Додає контакт до словника
    return 'Contact added!'                              #Повертає повідомлення про додавання контакту

# Функція для зміни номера контакту
def change_contacts(args, contacts): 
    name, new_phone = args                               #Приймає як аргументи ім'я контакту та його новий номер
    if name in contacts:                                 #Перевіряє чи існує контакт
        contacts[name] = new_phone                       #Якщо існує, змінює номер контакту
        return f'Contact {name} changed to {new_phone}!'
    else:                                                #Якщо контакт не існує, повертає повідомлення про помилку
        return f'Contact {name} not found!'

# Функція для відображення номеру контакту    
def show_phone(args, contacts): 
    name = args[0]                                       #Приймає як аргумент ім'я контакту
    if name in contacts:                                 #Перевіряє чи існує контакт
        return f'{name}: {contacts[name]}'               #Повертає номер контакту
    else:
        return f'Contact {name} not found!'              #Якщо контакт не існує, повертає повідомлення про помилку
    
# Функція для відображення всіх контактів
def show_all_contacts(contacts): 
    result = []                                          #Створює пустий список для зберігання контактів
    for name, phone in contacts.items() :
        result.append(f'{name}: {phone}')                #Додає контакти до списку
    return result                                        #Повертає список контактів


# Основна функція програми де реалізується логіка вище вказаних функції
def main():
    contacts = {}                                        #Створює пустий словник для зберігання контактів
    print('Welcome to assistant bot!')                   #Виводить привітальне повідомлення
    while True:                                          #Нескінченний цикл для очікування команди
        user_input = input('Enter command: ')
        command, *args = parse_input(user_input)

        if command in ['exit', 'close']:
            print('Goodbye!')
            break                                        #В разі команди exit або close виходить з нескінченного циклу та завершує роботу програми
        elif command == 'hello':
            print('How can i help you?')
        elif command == 'add':          
            print(add_contacts(args, contacts))
        elif command == 'all':
            print(f'All contacts: {show_all_contacts(contacts)}')
        elif command == 'change':
            print(change_contacts(args, contacts))
        elif command == 'phone':
            print(show_phone(args, contacts))
        else:                                             #В разі введення невірної команди виводить повідомлення про помилку
            print('Invalid command!') 

if __name__ == '__main__':                                
    main()

