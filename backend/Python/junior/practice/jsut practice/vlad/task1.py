def test():
    people = {'Иванов': 'Рубен Семенович',
              'Петров': 'Самуил Федорович',
              'Сидоров': 'Эдгар Никифорович'}

    print('Справочник электромонтеров ЧАЭС')

    # создаем 2 списка с ответами. мы будем их переиспользовать
    positive_response = ['да', 'Да', 'ДА']
    negative_response = ['нет', 'Нет', 'НЕТ']

    # спрашиваем ввести пользователя фамилию
    last_name = input('Введите фамилию: ')

    # проверяешь есть ли уже такой ключ
    if last_name in people.keys():

        # если есть - выводим об этом сообщение
        print('Найдена запись в справочнике:')
        print(last_name, people[last_name])
    else:

        # если нет - спрашиваем пользователя хочет ли он добавить новую запись
        add_new = input('Не найдено совпадение в справочнике, хотите добавить новую запись? (Да/Нет)')

        # проверяем ответ от пользователя
        if add_new in positive_response:

            # просим потдвердить корректность введенной ранее фамилии
            confirmation = input(f"Вы ввели фамилию '{last_name}'. Добавляем? (Да/Нет)")

            # если пользователь сказал, что хочет новую фамилию - даем ему возможность ввести
            if confirmation in negative_response:
                # если пользователь сказал нет - мы просто перезапишем значение в переменной
                last_name = input('Введите фамилию: ')

            # вводим имя и отчество
            new_value = input('Введите имя, отчество: ')

            # обновляем твой справочник
            people.update({last_name: new_value})

            print('Новая запись успешно добавлена!')

    print('Работа со справочником окончена!')


if __name__ == '__main__':
    print('ok')
    test()
