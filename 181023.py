# def div(x,y):
#     return x/y
# try:
#     result=div(100,0)
#     print(result)
# except ZeroDivisionError as e:
#     print ("Ошибка", e)
# except KeyError as e:
#     print("ключ", e)

# def div(x,y):
#     return x/y
# try:
#     d={1:11}
#     print(d[2])
#     result=div(100,0)
#     print(result)
# except ZeroDivisionError as e:
#     print ("Ошибка", e)
# except KeyError as e:
#     print("ключ", e)

# def div(x,y):
#     return x/y
# try:
#     d={1:11}
#     result=div(100,0)
# except Exception as e:
#     print(Exception, e)

# def divide(x,y):
#     try:
#         out=x/y
#     except:
#         try:
#             import math
#             out=math.inf*x/abs(x)
#         except:
#             out=None
#         finally:
#             return out
# print(divide(0,0))

# try:
#     raise Exception("что-то")
# except Exception as e:
#     print("Сообщение: "+str(e))
#
# def validate(name):
#     if len(name)<10:
#         raise ValueError
# try:
#     name=input('--->')
#     validate(name)
# except ValueError:
#     print('Короткое')
# else:
#     print('Ок')

# class NameTooShortError(ValueError):
#     pass
# def validate(name):
#     if len(name)<10:
#         raise NameTooShortError
# print(input('name'))

# class Positive(ValueError):
#     pass
# class Negative(ValueError):
#     pass
# def f(lst):
#     for i in lst:
#         try:
#             if i > 0: raise Positive
#             elif i<0:raise Negative
#         except Positive:
#             print("Положительное")
#         except Negative:
#             print("Отрицательное")
#         else:
#             print(0)
#     return
# f([1,-2,11,-22,0])

# def bounder_repeater(value,max_repeats):
#     count=0
#     while True:
#         if count>=max_repeats:
#             return
#         count+=1
#         yield value, count
# for x in bounder_repeater('Раз', 4):
#     print(x)

# def rep123():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
# print(*rep123())
# print(2 in rep123())
# print(5 in rep123())
# n1,n2,n3, n4=rep123()
# print(n1,n2,n3)
# gen=rep123()
# print(next(gen))
# gen=rep123()
# print(next(gen))
# print(next(gen))
# print(next(rep123()))
# print(next(gen))
# print(next(rep123()))
# print(next(rep123()))

# def f(lst):
#     yield from lst
# for i in f([11,22,33]):
#     print(i)

# def fg1():
#     yield 'Red'
#     yield 'Green'
#     yield 'Blue'
# def fg2():
#     yield 'Round'
#     yield from fg1()
#     yield 'Square'
# print(*fg2())

# lc=[i for i in range(10)]
# print(lc)
# print(len(lc))
# lc= (i for i in range(10))
# print(*lc)
# lc= (i for i in range(10))
# print(next(lc),next(lc))
# for i in lc:
#     print(i)

    # def inte(n):
    #     for i in range(n):
    #         yield i
    # def evens(iterable):
    #     for i in iterable:
    #         if i%2==0:
    #             yield i
    # def sq(iterable):
    #     for i in iterable:
    #         yield i*i
    # chain=sq(evens(inte(10)))
    # print(*chain)
    #
    # def inte(n):
    #     for i in range(n):
    #         yield i
    # def evens(iterable):
    #     for i in iterable:
    #         if i%2:
    #             yield i
    # def sq(iterable):
    #     for i in iterable:
    #         yield i**3
    # chain=sq(evens(inte(10)))
    # print(*chain)


# def inte(n):
#     for i in range(65,n):
#         yield i
# def evens(iterable):
#     for i in iterable:
#         yield chr(i)
# chain=evens(inte(100))
# print(*chain)

# def numb(a=65,z=91):
#     yield from range(a,z)
# def rhc (iterable):
#     for i in iterable:
#         yield chr(i)
# chain=rhc(numb(a=97, z=97+26))
# print(*chain)


# print(ord("а"))


def numb(a=65,z=97):
    yield from range(a,z)
def rhc (iterable):
    for i in iterable:
        yield chr(i)
chain=rhc(numb(a=1072, z=1072+32))
print(*chain)

