def count_letter(word_list: list, ch: str):
    qq = 0
    for word in word_list:
        if word.count(ch):
            qq += 1
    return qq


if __name__ == '__main__':
    example = ['python', 'c++', 'c', 'scala', 'java']
    char = input('Введи букву для посика в списке слов: ')
    result = count_letter(
        word_list=example,
        ch=char
    )
    print(f"Буква '{char}' встречается в списке слов {result} раз(а)")
