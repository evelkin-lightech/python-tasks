

def check_exist(a, b, c):
    return a + b < c or a + c < b or b + c < a


def full_rav_tr(a, b, c):
    return a == b == c


def rav_tr(a, b, c):
    return a == b != c or a == c != b or b == c != a


def tup_angle(a, b, c):
    return a * 2 < c * 2 + b * 2 or b * 2 < c * 2 + b * 2 or c * 2 < a * 2 + b * 2


def sqr_angle(a, b, c):
    return a * 2 == c * 2 + b * 2 or b * 2 == c * 2 + b * 2 or c * 2 == a * 2 + b * 2


def ostr_angle(a, b, c):
    return a * 2 > c * 2 + b * 2 or b * 2 > c * 2 + b * 2 or c * 2 > a * 2 + b * 2


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
        if full_rav_tr(x, y, z):
            msg += f' {property_tr[0]} и {property_tr[4]}'
        elif rav_tr(x, y, z):
            msg += f' {property_tr[1]}'
            if tup_angle(x, y, z):
                msg += f' {property_tr[5]}'
            if sqr_angle(x, y, z):
                msg += f' {property_tr[3]}'
            if ostr_angle(x, y, z):
                msg += f' {property_tr[4]}'
        elif not rav_tr(x, y, z) and tup_angle(x, y, z):
            msg += f' {property_tr[2]} и {property_tr[5]}'

    print(msg)


if __name__ == '__main__':
    print('ok')
    run()
