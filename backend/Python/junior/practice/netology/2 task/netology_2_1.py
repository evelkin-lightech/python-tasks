def help_function():
    print("""
        help - справка по программе
        add - добавление задачи
        show - показать все задачи
        exit - выход из программы
    """)


def add_function():
    task = input('Введи название задачи: ')
    TASKS.append(task)
    print('Задача добавлена')


def show_function():
    for task in TASKS:
        print(f'{task}')


def run():
    is_run = True
    while is_run:
        req_command = input("Введите команду: ")
        if req_command not in COMMANDS.keys():
            print("Неизвестная команда")
            break
        elif req_command == 'exit':
            print('Спасибо за использование! До свидания!')
            break
        else:
            COMMANDS[req_command]()


COMMANDS = {
    'help': help_function,
    'add': add_function,
    'show': show_function,
    'exit': None,
}

TASKS = []

if __name__ == '__main__':
    run()
