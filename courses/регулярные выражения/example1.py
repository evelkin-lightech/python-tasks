import re

text = 'Какая то длинная фраза для поиска'

match = re.findall(r'ка', text)

print(match)
