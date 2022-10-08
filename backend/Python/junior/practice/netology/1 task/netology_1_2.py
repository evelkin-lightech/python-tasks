TASK_LIST = dict()


def append_task():
    for i in range(3):
        date = input('Введите дату: ')
        task = input('Введите задачу: ')
        TASK_LIST[date] = task


def print_all_task():
    for key in TASK_LIST:
        print(f'{key} {TASK_LIST[key]}')


if __name__ == '__main__':
    append_task()
    print_all_task()
