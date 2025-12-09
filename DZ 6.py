# 1)
my_dict = {1.12: 'aa', 67.9: 45, 3.11: 'ccc', 7.9: 'dd', 9.2: 'ee',
           7.1: 'ff', 0.12: 'qq', 1.91: 'aa', 10.12: [1, 2, 3], 99.0: {9, 0, 1}}

print(min(my_dict) + max(my_dict))

# 2)
users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
         {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
         {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
         {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
         {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
         {'name': 'John', 'phone': '233-421-32', 'email': ''},
         {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
         {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
         {'name': 'Robert', 'phone': '420-2011', 'email': ''},
         {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
         {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
         {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
         {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
         {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
         {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
         {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]

users_phone_end_8 = []
for user in users:
    if  user['phone'].endswith('8'):
        users_phone_end_8.append(user['name'])

users_phone_end_8.sort()
print(' '.join(users_phone_end_8))

# 3)
users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
         {'name': 'Helga', 'phone': '555-1618'},
         {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
         {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
         {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
         {'name': 'John', 'phone': '233-421-32', 'email': ''},
         {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
         {'name': 'Alina', 'phone': '+7948-799-2434'},
         {'name': 'Robert', 'phone': '420-2011', 'email': ''},
         {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
         {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
         {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
         {'name': 'Roman', 'phone': '+7459-145-8059'},
         {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
         {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
         {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]

user_without_email = []
for user in users:
    if 'email' not in user or user['email'] == '':
        user_without_email.append(user['name'])

user_without_email.sort()
print(' '.join(user_without_email))

# 4)
a = int(input('Введите натуральное число: '))
numbers = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
           '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}

number_to_str = ''
for number in str(a):
    number_to_str += f'{numbers[number]} '

print(number_to_str)

# 5)
cource = input('Введите номер курса: ')
university = {'CS101': ['3004', 'Хайнс', '8:00'], 'CS102': ['4501', 'Альварадо', '9:00'],
              'CS103': ['6755', 'Рич', '10:00'], 'NT110': ['1244', 'Берк', '11:00'], 'CM241': ['1411', 'Ли', '13:00']}
print(f'{cource}: {', '.join(university[cource])}')

# 6)
world = input('Введите слово: ')
keyboard = {1: '.,?!:', 2: 'abc', 3: 'def',
            4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs',
            8: 'tuv', 9: 'wxyz', 0: ' '}

for i in world.lower():
    for j in keyboard:
        if i in keyboard[j]:
            print(j, end='')

# 7)
world = input()
alphabet = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
            'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
            'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
            'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
            'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
            'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----',
            '2': '..---', '3': '...--', '4': '....-', '5': '.....',
            '6': '-....', '7': '--...', '8': '---..', '9': '----.'}

for i in world.upper():
    if i in alphabet:
        print(alphabet[i], end=' ')

# 8)
result = {}
for i in range(11, 16):
    result[i] = i ** 2

# 9)
dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}

result = {}
result.update(dict1)
result.update(dict2)

for i in dict2:
    if i in dict1:
        result[i] = dict1[i] + dict2[i]

# 10)
text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
result = {}

for i in text:
    result[i] = result.get(i, 0) + 1

# 11)
s = '''orange strawberry barley gooseberry apple apricot barley currant orange
       melon pomegranate banana banana orange barley apricot plum grapefruit banana
       quince strawberry barley grapefruit banana grapes melon strawberry apricot
       currant currant gooseberry raspberry apricot currant orange lime quince
       grapefruit barley banana melon pomegranate barley banana orange barley
       apricot plum banana quince lime grapefruit strawberry gooseberry apple
       barley apricot currant orange melon pomegranate banana banana orange
       apricot barley plum banana grapefruit banana quince currant orange
       melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'''
result = {}
min_result = []

for i in s.split():
    result[i] = result.get(i, 0) + 1

for i in result:
    if result[i] == max(result.values()):
        min_result.append(i)

print(min(min_result))

# 12)
pets = [('Hatiko', 'Parker', 'Wilson', 50),
        ('Rusty', 'Josh', 'King', 25),
        ('Fido', 'John', 'Smith', 28),
        ('Butch', 'Jake', 'Smirnoff', 18),
        ('Odi', 'Emma', 'Wright', 18),
        ('Balto', 'Josh', 'King', 25),
        ('Barry', 'Josh', 'King', 25),
        ('Snape', 'Hannah', 'Taylor', 40),
        ('Horry', 'Martha', 'Robinson', 73),
        ('Giro', 'Alex', 'Martinez', 65),
        ('Zooma', 'Simon', 'Nevel', 32),
        ('Lassie', 'Josh', 'King', 25),
        ('Chase', 'Martha', 'Robinson', 73),
        ('Ace', 'Martha', 'Williams', 38),
        ('Rocky', 'Simon', 'Nevel', 32)]

result = {}

for i in pets:
    if i[1:4] in result:
        result[i[1:4]].append(i[0])
    else:
        result[i[1:4]] = [i[0]]

# 13)
world = input('Введите слово: ').lower()
result = {}
min_result = []
symbols = ['.', ',', '!', '?', ':', ';', '-']

for i in symbols:
    if i in world:
        world = world.replace(i, '')

for i in world.split():
    result[i] = result.get(i, 0) + 1

for i in result:
    if result[i] == min(result.values()):
        min_result.append(i)

print(min(min_result))

# 14)
a = input('Ведите строку: ')
b = {}

for i in a.split():
    if i in b:
        print(f'{i}_{b[i]}', end=' ')
    else:
        print(i, end=' ')
    b[i] = b.get(i, 0) + 1
