def help_function():
    print("""
        help - справка по программе
        add - добавление задачи
        show - показать все задачи
        exit - выход из программы
    """)


def add_function():
    req_date = input('Введи дату для задачи: ').lower().capitalize()
    req_task = input('Введи название задачи: ').lower().capitalize()
    if req_date == 'Сегодня':
        TASKS['today'].append(req_task)
    elif req_date == 'Завтра':
        TASKS['tomorrow'].append(req_task)
    else:
        TASKS['other'].append(req_task)
    print('Задача добавлена')


def show_function():
    for key in TASKS:
        for task in TASKS[key]:
            print(f'{translate(key)} {task}')


def translate(word):
    if word == 'today':
        result = 'Сегодня'
    elif word == 'tomorrow':
        result = 'Завтра'
    else:
        result = 'Другая дата'
    return result


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

TASKS = dict(today=[], tomorrow=[], other=[])

if __name__ == '__main__':
    run()
