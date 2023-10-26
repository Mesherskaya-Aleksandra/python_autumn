# import re
# n=int(input('---->'))
# x, y =divmod(n,10)
# print(n,x,y)
# r=[]
# r.append(r'\b\d\b')
# r.append(r'\b10\b')
# if n ==10: regex='|'.join(r[:2])
# elif n<20:
#     r.append(rf"\b1[0-{y}]\b")
#     regex='|'.join(r[:3])
# else:
#     r.append(rf'\b[1-{x-1}]\d\b')
#     r.append(rf'\b{x}[0-{y}]\b')
#     regex   ='|'.join(r[:4])
# print(*re.findall(regex, str(list(range(200)))))

# import re
# text='Миша:123 Коля:234 Сеня:345'
# res=re.findall(r'(\w+):(\d+)', text)
# print(res)
#
#
# import re
# text='sgargfvaetg'
# res=re.finditer(r'a', text)
# for i in res:
#     print(i.group(), i.start(), i.end())
#
# numbers=re.compile(r'\d+')
# text='Я живу в доме 5'
# print(re.findall(numbers,text))


# import re
# string='Косой косой косил траву на косе'
# regex=r'\b\w*ос\w+\b'
# print(re.findall(regex, string))
#
# import re
# def podslovo(text, os):
#     return re.findall(rf'\b{os}', text)
# text='Косой косой косил волос на осине'
# os='ос'
# print(podslovo(text,os))

# def sample_decorator(func):
#     def wrapper():
#         print("начало функции")
#         func()
#         print("конец функции")
#     return wrapper()
# def say():
#     print('Привет мир')
# say=sample_decorator(say)



# import time
# def timer(func):
#     def wrapper(*args, **kwargs):
#         start=time.perf_counter()
#         val=func(*args, **kwargs)
#         end=time.perf_counter()
#         work_time=end-start
#         print("Время выполнения work_time")
#         return val
#     return wrapper
# @timer
# def test(n): return sum([(i/99)**2 for i in range(n)])
# @timer
# def sleep(n): time.sleep(n)
# res1=test(1000)
# res2=sleep(4)
# print(f'результат выполнения функции test={res1}')
# print(f'результат выполнения функции sleep={res2}')


# import time
# def clue(func):
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs)
#         res=""
#         for i in args:
#             res+=i
#         return res
#     return wrapper
# @clue
# def test(*args): return None
# print(test('aaa', 'bbb', 'ccc'))
# @clue
# def comp_str(x , y):
#     return x>y
# print(comp_str('d', 'b'))

class Person:
    def __init__(self, name, money):
        self.name=name
        self.money=money
    def give_money(self, other, x_money):
        if x_money<=self.money:
            other.money+=x_money
            self.money-=x_money
            print(self.money, other.money)
        else:
            print("Мало денег")
    def info(self):
        print(f'{self.name=}, {self.money=}')
    def soc(self, other):
        total=self.money+other.money
        self.money=total/2
        other.money = total / 2
        print(self.money, other.money)



a=Person('Pete', 500)
b=Person('Kate', 1000)
print(a.name, a.money)
a.give_money(b,100000)
b.give_money(a,100)
a.info()
b.info()
a.soc(b)
print(self.money, other.money)