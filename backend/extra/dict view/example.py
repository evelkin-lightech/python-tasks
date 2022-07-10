# create simple dict for example
persons = {
    'Sam': '79001350620',
    'Jack': '79289553312',
    'Smith': '79516634081',
    'Sue': '79618880002',
}

print('=' * 50)
print('Simple dict for demo: ')
print(persons)

# create some values for store dict object views
names = persons.keys()
phones = persons.values()
items = persons.items()

print('=' * 50)
print(f'names = persons.keys() => {names}')
print(f'phones = persons.values() => {phones}')
print(f'items = persons.items() => {items}')

# demonstration of methods for processing
# 1. len - return count of dict obj view
print('=' * 50)
print('Demonstration of methods for processing')
print('# 1. len - return count of dict obj view')
print(f'  len(phones): {len(phones)}')

# 2. iter - return an iterator over the keys, values or items
print('=' * 50)
print('# 2. iter - return an iterator over the keys, values or items')
print(f'  iter(names): {iter(names)}')
i = iter(names)
print(f'  next(iter(names)): {next(i)}')
print(f'  next(iter(names)): {next(i)}')
print('and so on...')

test1 = zip(persons.values(), persons.keys())
test2 = [(v, k) for (k, v) in persons.items()]

# 3. x in dictview - construction for check keys, values and items in dict
print('=' * 50)
print('# 3. x in dictview construction for check keys, values and items in dict')
print(f"  'Sam' in names: {'Sam' in names}")
print(f"  '911' in phones: {'911' in phones}")
print(f"  ('Sam','79001350620') in items: {('Sam','79001350620') in items}")

# 4. reversed(dictview) - return a reverse iterator over the keys, values or items
print('=' * 50)
print('4. reversed(dictview) - return a reverse iterator over the keys, values or items')
print(f'  reversed(names): {reversed(names)}')
rv = reversed(names)
print(f'  next(reversed(names)): {next(rv)}')
print(f'  next(reversed(names)): {next(rv)}')
print('and so on...')
