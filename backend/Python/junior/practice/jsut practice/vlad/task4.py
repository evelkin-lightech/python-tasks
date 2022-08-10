def check_exist(a, b, c):
    return a + b < c or a + c < b or b + c < a


def main(a, b, c):
    return [
        a == b == c,
        a == b != c or a == c != b or b == c != a,
        a * 2 < c * 2 + b * 2 or b * 2 < c * 2 + b * 2 or c * 2 < a * 2 + b * 2,
        a * 2 == c * 2 + b * 2 or b * 2 == c * 2 + b * 2 or c * 2 == a * 2 + b * 2,
        a * 2 > c * 2 + b * 2 or b * 2 > c * 2 + b * 2 or c * 2 > a * 2 + b * 2
    ]


def run():
    print('Программа для определения типа треугольника')

    x = float(input('Введите значение первой стороны треугольника: '))
    y = float(input('Введите значение второй стороны треугольника: '))
    z = float(input('Введите значение третьей стороны треугольника: '))

    property_tr = [
        'равносторонний',
        'равнобедренный',
        'разносторонний',
        'прямоугольный',
        'остроугольный',
        'тупоугольный'
    ]

    msg = 'Полученный треугольник:'

    if check_exist(x, y, z):
        msg = 'Трегольника с указанными сторонами не существует!'
    else:
        is_full_rav, is_rav, is_tup, is_sqr, is_ostr = main(x, y, z)
        if is_full_rav:
            msg += f' {property_tr[0]} и {property_tr[4]}'
        elif is_rav:
            msg += f' {property_tr[1]}'
            if is_tup:
                msg += f' {property_tr[5]}'
            if is_sqr:
                msg += f' {property_tr[3]}'
            if is_ostr:
                msg += f' {property_tr[4]}'
        elif not is_rav and is_tup:
            msg += f' {property_tr[2]} и {property_tr[5]}'

    print(msg)


if __name__ == '__main__':
    print('ok')
    run()
