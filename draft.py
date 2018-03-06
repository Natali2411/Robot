# 1. Тебе необходимо написать функцию, которая перевернет массив неопределенной длины. Условие - нельзя использовать встроенный метод length.
def reverseList(list):
    l2 = []
    for i in reversed(list):
        l2.append(i)
    return l2

print(reverseList([1,2,3,4,5,6,7,8]))

#2. Реализовать функцию которая отфильтрует все буквы в строке, которые встречаются более одного раза (> 1). Пример: => "agcdcgia": "agc"
def filtrStr(s):
    d = {}
    s2 = ''
    for i in s:
        if i not in d:
            d.setdefault(i, 1)
        else:
            d[i] += 1
            d.update({i: d[i]})
    for i in d:
        if d[i] > 1:
            s2 += i
    return s2

print(filtrStr('AADDTFGOOFF'))
'''
3. Необходимо написать функцию, которая заменит значение объекта в массиве, по переданному id. Условие - все данные должны быть immutable.
Входящие данные:
    array = [
        {'id': 1, 'state': True},
        {'id': 2, 'state': True},
        {'id': 8, 'state': False}
    ]

Пример:
=> update(2, False)
[{'id': 1, 'state': True}, {'id': 2, 'state': False}, {'id': 8, 'state': False}]

=> update(8, True)
[{'id': 1, 'state': True}, {'id': 2, 'state': True}, {'id': 8, 'state': True}]

=> update(7, True) # Ничего не произойдет.
[{'id': 1, 'state': True}, {'id': 2, 'state': True}, {'id': 8, 'state': False}] '''

def update(key, val):
    array = [
        {'id': 1, 'state': True},
        {'id': 2, 'state': True},
        {'id': 8, 'state': False}
    ]
    for i in range(len(array)):
        if key == array[i]["id"]:
            array[i]["state"] = val
    return array

print(update(2, False))

'''
4. Необходимо нормализовать строку убрав все дополнительные символы возле слов.
Пример:
=> normalize("X > %Y")
    "X > Y"

=> normalize("  X >      Y    >")
    "X > Y"

=> normalize("\"X\" >'Y'> I  \t> 1Z2")
    "X > Y > I > 1Z2"

Дополнительные символы:
    !"$&\'*+,-./:;<=?[\\]^`{|}~\t\n\x0b\x0c\r
'''
import re
def normalize(s):
    r = ""
    #pattern = re.compile(r'[\s+]')
    pattern = re.compile(r'[\s\t\n\x0b\x0c\r%!"$&\'*,-./:;<=?\\^`{|}~]')
    txt = re.sub(pattern, '', s).split('>')
    for i in range(len(txt)):
        r += str(txt[i]) + ' ' + '> '
    return r[:-2]


print(normalize("X > % Y"))
print(normalize("  X >      Y    >"))
#print(normalize("\"X\" >'Y'> I  \t> 1Z2"))