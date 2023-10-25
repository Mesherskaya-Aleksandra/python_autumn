#Задача 16-1
import re
text = input("Введите текст")
def func(x):
    return x[0][0].capitalize()
s = re.sub(r'\b\w+\b', func, text)
t = re.split(r'[\s,:;!&./-]+', s)
print("".join(t))

#Задача 16-3
def lowercase_deco(func):
    def wrapper():
        return func().capitalize()
    return wrapper
def h():
    s=input("Введите текст")
    return s
h=lowercase_deco(h)
print(h())