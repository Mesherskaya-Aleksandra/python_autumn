# a=tuple(i for i in range(5))
# print(a)

# b=[i**3 if i%2 ==1 else i**2 for i in range(1,11)]
# print(b)

# import functools
# print(functools.reduce(lambda x,y:x*y, [10,20,30]))
# import functools
# print(functools.reduce(lambda x,y:x+y, [10,20,30]))
# import functools
# print(functools.reduce(lambda x,y:x+y, ['a', 'c', 'ff'], 'x='))
# import functools
# s=int(input())
# print(functools.reduce(lambda x,y:x*y,range(2,s+1),1))

# from functools import cmp_to_key
# def mul(x,y):
#     if x>y:return -1
#     elif x==y: return 0
#     else: return 1
# print(sorted([1,0,-1,3,4], key=cmp_to_key(mul)))

# import itertools
# for k in itertools.combinations([1,2,3,4],2):
#     print(k)

# import itertools
# for k in itertools.combinations_with_replacement([1,2,3,4],2):
#     print(k)

# import itertools
# for k in itertools.combinations_with_replacement([1,2,5,10],3):
#     print(k, sum(k))
# else:
#     print()

# import itertools
# for k in itertools.combinations([1,2,5,10],3):
#     print(k,sum(k))

# import itertools
# tes=set()
# for k in itertools.combinations([1,2,5,10],3):
#     tes.add(sum(k))
# print(tes)

# import itertools
# tes=set()
# for k in itertools.combinations([1,1,2,2,5,5,10,10],3):
#     # print(k)
#     tes.add(sum(k))
# print(tes)

# import itertools
# tes=set()
# for k in itertools.combinations([1,2,5,10]*2,3):
#     # print(k)
#     tes.add(sum(k))
# print(tes)

# try:
#     a=1/0
# except ZeroDivisionError:
#     print("Возникло исключение")
#     a=0
# else:
#     print('Ok')
# finally:
#     print('Далее')

# try:
#     print('До')
#     a=1//1
# except ZeroDivisionError:
#     print("Возникло исключение")
#     a=0
# else:
#     print('Ok')
# finally:
#     print('Далее',a)


# while True:
#     try:
#         a=int(input('---->'))
#         print(a)
#         if a==0: break
#     except ValueError:
#         print('Ошибка, повторите ввод')

# a=[1,2,3]
# try:
#     print(a[3])
# except IndexError:
#     print("***")


# for i in '123':
#     print('Попытка', i)
#     try:
#         u=input('--->')
#         f=open(u, encoding='utf-8')
#         s = f.read()
#         print("Файл 'mmm11111.txt' найден")
#     except FileNotFoundError:
#         print("Файл не найден, введите другое имя")

# def fun(n):
#     for x in range(n):
#         print('до', x)
#         yield x*x
#         print('после', x)
# g=fun(3)
# print(g)
# for k in g:
#     print('перед печатью')
#     print('k=',k)
#     print('после печати')

# def fun(n):
#     for x in range(n):
#         if x%2==0:
#             print('четный',x)
#             yield x*x
#         else:
#             print('нечетный', x)
#             yield x**3
# g=fun(8)
# print(g)
# for k in g:
#     print('k=',k)

# def fun(n):
#     for x in range(n):
#         if x%2==0:
#             yield x*x
#         else:
#             yield x**3
# g=fun(4)
#
# try:
#     print(next(g))
#     print(next(g))
#     print(next(g))
#     print(next(g))
#     print(next(g))
# except StopIteration:
#     print('Все закончено')

# def fun(n):
#     for x in range(n):
#         if x%2==0:
#             yield x*x
#         else:
#             yield x**3
# g=fun(4)
# for k in g:
#     print(k)

# def fun(n):
#     for x in range(n):
#         if x%2==0:
#             yield x*x
#         else:
#             yield x**3
# g=fun(4)
# for k in range(10):
#     try:
#         print(next(g))
#     except StopIteration:
#         print('Конец')
#         break

# def factorial(n):
#     f,k=1,1
#     while True:
#         print(k, end=' ')
#         yield f
#         k+=1
#         if k>n-1:break
#         f*=k
# for m in factorial(10):
#     print(m)

# def factorial():
#     f,k=1,1
#     while True:
#         print(k, end=' ')
#         yield f
#         k+=1
# gf=factorial()
# while True:
#     print(next(gf))
#     input()

# lst=[1,2,4,8,16,32]
# def sum_firsts():
#     s=0
#     for i in lst:
#         s+=i
#         yield s
# gf = sum_firsts()
# for k in gf:
#     print(k)

# lst=[1,10,100,1000,10000,100000]
# def sum_firsts():
#     s=0
#     for i in lst:
#         s+=i
#         yield s
# while True:
#     print(next(sum_firsts()))
#     input()

def f123():
    n=1
    while True:
        for i in range(n):
            yield n
        n+=1

gf=f123()
for i in range(20):
    print(next(gf), end=' ')
