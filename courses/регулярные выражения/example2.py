import re

regexp1 = r'\b[Ее]д[ауы]\b'
regexp2 = r'[\d]'  # [0-9]
regexp3 = r'[^\d]'  # [^0-9]
regexp4 = r'[^\w]'  # [^а-яА-Я0-9]

text = 'Еда, беда, гряда, едок, 50'

match = re.findall(regexp1, text)
print(match)

match = re.findall(regexp2, text)
print(match)

match = re.findall(regexp3, text)
print(match)

match = re.findall(regexp4, text)
print(match)
