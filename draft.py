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