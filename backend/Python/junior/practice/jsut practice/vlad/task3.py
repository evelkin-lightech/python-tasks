def end():
    return print('Работа со справочником окончена!', people)


people = {'Иванов': 'Рубен Семенович',
          'Петров':'Самуил Федорович',
          'Сидоров':'Эдгар Никифорович'}
print('Справочник электромонтеров ЧАЭС')
last_name = input('Введите фамилию  ')
yeah = ('Да', 'ДА', 'да', 'дА')
no = ('Нет', 'нет', 'неТ', 'НЕТ')
if last_name in people.keys():
    print(people[last_name])
else:
    add_new = input(f'В справочнике не найдено фамилии {last_name}, хотите добавить новую запись/не добавлять новую запись/изменить фамилию (Да/Нет/Введите фамилию)'  )
    if add_new in yeah:
        name = input('Введите имя, отчество  ')
        people.update({last_name: name})
        end()
    elif add_new in no:
        end()
    else:
         while add_new in people.keys():
            add_new = input(f'Вы пытаетесь ввести фамилию, которая уже есть в справочнике: {add_new, people[add_new]}, повторите ввод')
         else:
            other_name = input('Введите имя, отчество  ')
            people.update({last_name : other_name})
            end()

if __name__ == '__main__':
    print('ok')
