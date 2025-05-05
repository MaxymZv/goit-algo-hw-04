def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.lower().strip()
    return cmd, *args

def add_contacts(args, contacts):
    name, phone = args
    contacts[name] = phone
    return 'Contact added!'

def main():
    contacts = {}
    print('Welcome to assistant bot!')
    while True:
        user_input = input('Enter command: ')
        command, *args = parse_input(user_input)

        if command in ['exit', 'close']:
            print('Goodbye!')
            break
        elif command == 'hello':
            print('How can i help you?')
        elif command == 'add':          
            print(add_contacts(args, contacts))
        elif command == 'all':
            print(f'All contacts: {contacts}')
        elif command == 'change':
            name, new_phone = args
            if name in contacts:
                contacts[name] = new_phone
                print(f'Contact {name} changed to {new_phone}!')
            else:
                print(f'Contact {name} not found!')
        elif command == 'phone':
            name = args[0]
            if name in contacts:
                print(f'{name}: {contacts[name]}')
            else:
                print(f'Contact {name} not found!')
        else:
            print('Invalid command!')

if __name__ == '__main__':
    main()

