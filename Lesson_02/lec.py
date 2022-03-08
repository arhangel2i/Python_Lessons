import func

colors = ['red','green','blue']
data = open ('file.txt', 'w')
data.writelines(colors) #запись без разделителей
data.write('line 2')
data.close()

with open('file.txt', 'r') as data:
    for line in data:
        print(line)

print(func.SplitStr("1","2","3","4","5"))

a,b=3,4 #пример множественного присваивания
print(a)
print(b)

b=(3,4) #пример кортежа (неизменяемого списка т.е. значения присваивать нельзя)
print(b)
print(b[0])
print(b[1])

a=["a","b","c"] #пример преобразования списка в кортеж и обратно
b=tuple(a)
a[0]="d"
print(a, type(a))
print(b, type(b))
a=list(b)
print(a, type(a))
print(b, type(b))

for item in a: #перебор элементов списка
    print(item)

for item in b: #перебор элементов кортежа
    print(item)

item1, item2, item3 = a #распаковка кортежа
print(item1,item2,item3)

a =item1, item2, item3 #упаковка кортежа
print(a, type(a))

dict1 = {}
dict1 = \
    {
        '1':'a',
        '2':'b',
        '3':'c'
    }
print(dict1, type(dict))
print(dict1['3'], type(dict1['3']))

for k in dict1.keys(): #извлечение ключей из словаря
    print(k)

for v in dict1.values():  #извлечение значений из словаря
    print(v)

for fullk in dict1: #извлечение ключей из словаря
    print(fullk)

colors = {'red','green','blue'}
print(colors, type(colors))
colors.add('red')
colors.add('gray')
colors.remove('red')
colors.discard('red')

a={1,2,3,5,8}
b={2,5,8,13,21}
c=a.copy()
u = a.union(b)
i=a.intersection(b)
dl = a.difference(b)
dr = b. difference(a)
с = frozenset(a)

list1=[1,2,3,4,5]
list2 = list1
list1[0]=12

for e in list1:
    print(e)

for e in list2:
    print(e)






