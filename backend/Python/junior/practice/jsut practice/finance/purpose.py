import sys


def input_of_initial_data():
    try:
        accumulated_funds = int(input('Введи сумму в рублях: '))
        inflation = int(input('Введи годовой процент инфляции: '))
        period = int(input('Введи срок в месяцах: '))
    except Exception as ex:
        print(f'Error: {ex}')
        sys.exit()
    return accumulated_funds, inflation, period


def run():
    x, y, z = input_of_initial_data()
    s = x * (1 + y / 100) ** (z / 12)
    p = s / (z / 12) / 12
    result = f"""
            С учетом годовой инфляции в {y} % мы за {round(z / 12)} года/лет ({z} месяцев)
            должны накопить {round(s)} рублей. При этом каждый месяц мы должны
            будем откладывать около {round(p)} рублей.
        """
    return result


if __name__ == '__main__':
    print(run())
