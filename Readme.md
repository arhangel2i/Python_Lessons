# Изучение языка Python
## Оглавление
1. [Урок 1. Знакомство с языком Python](#Lesson1)

## <a name="task1"></a>Урок 1. Знакомство с языком Python
В языке Python используется динамическое присваивание типа переменной, т.е. тип переменной присваивается на основе ее значения.<br/>
Пример как в процессе работы скрипта меняется тип переменной:
```Python
a=1
print(a, type(a))
a='hello'
print(a, type(a))
```
Вывод:
>1 <class 'int'><br/>
>hello <class 'str'>

### Список операторов:
Оператор|Комментарий
:-|:-
**print(value)**|*Вывод переменной на экран*
**value=input()**|*Ввод перемеременной с экрана*