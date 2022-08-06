import math


def test():
    print('Программа для вычисления углов треугольника')
    a = int(input('Введите значение первой стороны треугольника: '))
    b = int(input('Введите значение второй стороны треугольника: '))
    c = int(input('Введите значение третьей стороны треугольника: '))
    if a + b < c or a + c < b or b + c < a:
        print('Треугольника с указанными длинами сторон не существует')
    else:
        if a == b == c:
            print('Все углы равны 60 градусов')
        else:
            angle_abc = math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b)) * 180 / math.pi
            angle_acb = math.acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c)) * 180 / math.pi
            angle_bac = 180 - (angle_abc + angle_acb)
            print(f'угол ABC = {angle_abc} градусов, угол ACB = {angle_acb} градусов, угол BAC = {angle_bac} градусов')


if __name__ == '__main__':
    print('ok')
    test()
