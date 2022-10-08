TASK_LIST = dict()


def append_task():
    for i in range(3):
        date = input('Введите дату: ')
        task = input('Введите задачу: ')
        TASK_LIST[date] = task


if __name__ == '__main__':
    append_task()
