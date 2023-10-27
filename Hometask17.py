#Задача 7.1

import re
def func(x):
    regex = r'(\w+)(\s+\1)+'
    return re.sub(regex, r'\1', x)
x=input('Введите текст')
print(func(x))


#Задача 7.2
def clue(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        res=""
        for i in args:
            res+=i.upper()
        return res
    return wrapper
@clue
def test(*args): return None
print(test('aaa', 'bbb', 'ccc'))
@clue
def comp_str(x , y):
    return x>y
print(comp_str('d', 'b'))

#Задача 7.3
class Shape:
    def __init__(self, colour, square):
        self.colour=colour
        self.square=square
a=Shape('Red', 500)
b=Shape('Blue', 1000)
print(a.colour)
print(b.colour)
print(a.square)
print(b.square)


