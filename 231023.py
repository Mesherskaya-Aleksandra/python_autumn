# import re
# def fullname(x):
#     s=x.group()
#     print(x.group(),x.start(), x.end())
#     match s:
#         case 'Коля': return "Николай"
#         case "Миша": return "Михаил"
#     if s == "Коля": return "Николай"
#     elif s == "Миша": return "Михаил"
# text='Здравствуй, Коля! Привет, Миша!'
# print(re.sub(r'\b\w{4}', fullname, text))

import re
# def fullname(x):
#     s=x.group()
#     print(x.group(),x.start(), x.end())
#     match s:
#         case 'Коля': return "Николай"
#         case "Миша": return "Михаил"
#     if s == "Коля": return "Николай"
#     elif s == "Миша": return "Михаил"
# text='Здравствуй, Коля! Привет, Миша!'
# print(re.sub(r'\b\w{4}', fullname, text))


# def fullname(x):
#     s=x.group()
#     dct={'LED': "Пулково", 'MSQ': "Шереметьево"}
#     return dct.get(s, 'Unknown')
# text='LED SVO MSQ SVX'
# res=re.sub(r'\b\w{3}\b', fullname, text)
# print(res)

# import re
# text='Коля орпорпо Петя'
# res=re.sub(r'(Коля) (Петя)', r'\1\1 \2\2', text)
# print(res)

# import re
# text='Мещерская Александра Александровна'
# res=re.sub(r'(Александра) (Александровна)', r'\2 \1', text)
# print(res)

# import re
# text='123 first 234 second'
# res=re.findall(r'\d+(\w+)', text)
# print(res)
#
# import re
# text='123 first 234 second'
# res=re.findall(r'(\d)+(\w+)', text)
# print(res)
#
# import re
# text='123 first 234 second'
# res=re.findall(r'(\d)+\w+', text)
# print(res)

# import re
# text='123 first 234 second'
# res=re.findall(r'(\d+)+(\w+)', text)
# print(res)

# import re
# text='123 first 234 second'
# res=re.findall(r'(\d+)[ ](\w+)', text)
# print(res)

# import re
# text='www.itmo.ru www.yandex.ru'
# res=re.findall(r'www.(\w+).(?:ru|com)', text)
# print(res)

# import re
# text='sgargfvaetg'
# res=re.finditer(r'ar', text)
# for i in res:
#     print(i.group(), i.start(), i.end())
#
# import re
# text='s garg fvaetg'
# res=re.finditer(r'^[a]', text)
# for i in res:
#     print(i.group(), i.start(), i.end())
#
# import re
# text='s garg fvaetg'
# res=re.finditer(r'a', text)
# for i, j in enumerate(res):
#     print(j, i.group(), i.start(), i.end())

# import re
# def fu(text):
#     counter=0
#     def change(x):
#         nonlocal counter
#         counter+=1
#         return "A" + str(counter)
#     res=re.sub(r'a', change, text)
#     return res
# print(fu('aaaaaaaa'))

# import re
# text='гамма адажио дододо аллегро нота до ре'
# res=re.findall(r'\b\w+\b', text)
# print(res)
# import collections
# for i in res:
#     x=collections.Counter(i).values()
#     if max(x)>1:
#         print(i, max(x))

# import re
# text='1   +   222*3   -7'
# print(re.split(r'\s+', text))
#
# import re
# text='1   +   222*3   -7'
# print(re.split(r'[\s+*-/]+', text))

# import re
# text='раз, два, три'
# print(re.split(r'[,:;!&./]+', text))

# import re
# text='раз, два, три, 2312312313'
# x='раз'
# print(re.findall(rf'{x}', text))
#
# for i in range(1,6):
#     print(re.findall(rf'{i}', text))

# def fun(f):
#     return f
# def hellow():
#     print('Привет')
# hellow()
# fun(hellow)()
# a=fun(hellow)
# a()

# def speak(text):
#     def whisper(t):
#         return t.lower()
#     res=whisper(text)
#
#     return res
# print(speak('Helow World'))

# def speak():
#     def whisper(t):
#         return t.lower()
#     return whisper
# wr=speak()
# print(wr('Hellow World'))


# def speak(text):
#     def whisper():
#         return text.lower()+"...."
#     return whisper
# f=speak('Hellow World')
# print(f())
# b=speak('Welcome')
# print(b())

# def null_decorator(func):
#     return func
# def hellow():
#     print("Hellow World")
# hellow=null_decorator(hellow)

# def sample_deco(func):
#     def wrapper():
#         print("Начало функции")
#         func()
#         print("Конец функции")
#     return wrapper

# def say():
#     print("Привет")
# say=sample_deco(say)
# say()

# def bye():
#     print('bye')
# bye=sample_deco(bye)
# bye()

def uppercase_deco(func):
    def wrapper():
        or_res=func()
        modi=or_res.upper()
        return modi
    return wrapper

@uppercase_deco
def h():
    return 'Hello'
h=uppercase_deco(h)
print(h())
