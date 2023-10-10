# #NOD 1
# s=list(map(int, input().split()))
# res=1
# for k in s:
#     res*=k
#     print(res)
# for n in range(res,0,-1):
#     for m in s:
#         if n%m:
#             break
#     else:
#         nok=n
# print(nok)

# #NOD 2
#
# s=list(map(int, input().split()))
# def nod(a,b):
#     while a!=0 and b!=0:
#         if a>b:
#             a=a%b
#         else:
#             b=b%a
#     return a+b
# def nok2(a,b):
#     return a*b//nod(a,b)
# x=1
# for i in s:
#     x=nok2(x,i)
#     print(x)

#
# #Cesar
# def code(string, n):
#     res=""
#     for i in string:
#         new_ord=ord(i)+n
#         if chr(ord('a'))<=i<=chr(ord('a')+25):
#             new_ord=ord('a')+(new_ord-ord("a"))%26
#             res+=chr(new_ord)
#         elif chr(ord("A"))<=i<=chr(ord("A")+25):
#             new_ord=ord("A")+(new_ord-ord("A"))%26
#         else:
#             res+=i
#     return res
# while True:
#     print(code(input(),int(input())))



# lst=[[1,2,3],[5,6,7],[5,6,7]]
# cmn=[]
# for i in lst:
#     cmn.extend(i)
# print(sorted(cmn)[-3:])

# for i in zip([1,2,3],'sfsgasg', (22,33,44)):
#     print(i)
#
# for k in reversed('asfsdf'):
#     print(k, end='')
# print()
# print('asfsdf')

#
# def chet(x):
#     if x%2:
#         return False
#     else:
#         return True
# print(list(filter(chet, {1,2,3,4,5,6,7})))
#
#
# def chet(x):
#     if x<5:
#         return True
#     else:
#         return False
# print(list(filter(chet, {1,2,3,4,5,6,7})))
#
# s,z=map(int, input().split())
# print(s,z)

# s,z,x=map(int, ['1','23','45'])
# print(s,z,x)

# print(sorted('dsasgsg'))
# print(sorted('aA'))
# print(list(map(ord, 'Aa')))
#
# print(sorted([1,-4,-5,2,3], key=abs))

# def quad(x):
#     return x*x
# print(sorted([1,-4,-5,2,3], key=quad))

# print(sorted(['123', '1', '2', 'adafsg', 'd'], key=len))
# print(sorted(['123', '1', '2', 'adafsg', 'd']))

# def quad(x):
#     return -x*x
# print(sorted([1,-4,-5,2,3], key=quad))

# import math
# print(*dir(math))
# print(math.pi)
# print(math.e)
# print(math.factorial(6))

# from math import sqrt
# print(sqrt(16))

# from math import *
# print(sqrt(81))
# print(sqrt(16))
# print(degrees(pi))
# print(gcd(24,36,48))
# print(lcm(24,36,48))#наименьшее общее кратное

# from math import pi
# def circle  (r):
#     return pi*r*r
# d=float(input())
# print(circle(d))

# from math import pi
# def circle_area(d):
#     return pi*d**2/4
# d=float(input())
# print(circle_area(d))

# import math as mt
# print(mt.sqrt(4))
# print(help('modules'))

# crt=[(1,2),(0,2),(1,1),(1,0),(2,2)]
# print(sorted(crt))
# crt=[(1,2),(0,2),(1,1),(1,0),(2,2)]
# def s(x):
#     return x[0], -x[1]
# print(sorted(crt, key=s))
#
# crt=[(1,2),(0,2),(1,1),(1,0),(2,2)]
# def s(x):
#     return -x[0], x[1]
# print(sorted(crt, key=s))
#
# crt=[(1,2),(0,2),(1,1),(1,0),(2,2)]
# def s(x):
#     return -x[1], x[0]
# print(sorted(crt, key=s))

# crt=[(1,2),(0,3),(0,5),(0,2),(1,1),(1,0),(2,2)]
# def s(x):
#     return -x[1]+ x[0]
# print(sorted(crt, key=s))

# lst=[19,22,37,41,20]
# def f(n):
#     return n%10
# print(sorted(lst, key=f))

# lst=[0,200,19,19,12,202,22,37,41,20]
# def f(n):
#     return n%10, n
# print(sorted(lst, key=f))

# lst=[0,200,19,19,12,202,22,37,41,20]
# def f(n):
#     return n%10, -n
# print(sorted(lst, key=f))
#
# n=123
# print(str(n)[-1])

# lst=[0,200,19,19,12,202,22,37,41,20]
# print(sorted(lst, reverse=True))

# x=5
# print(eval('12+5'))
# print(eval('12+x'))
# print(eval('abs(-123)'))

# def f(x):
#     return x**2
# print(eval('f(x)'))
# g=f
# p=x
# print(eval('g(p)'))

# x='a=15'
# exec(x)
# print(a)

# print('35432523sfdg'.find('3',2,3))
# print('35432523sfdg'.rfind('3'))
# print('35432523sfdg'.replace('3','z'))
# print('35432523sfdg'.strip('3'))

# print('dfasHGJJ'.lower())
# print('dfasHGJJ'.upper())
# print('dfasHGJJ fdgsg'.capitalize())
# print('dfasHGJJ fdsgfrg'.title())

# print('3134'.isdigit())
# print('dagrd'.isalpha())
# print('dagrd'.isalnum())
# print('dagrd'.find('da'))
# print('dagrd123ghj123jhkj123'.replace('123','asd',1))
# print("+".join(['a','x','b']))
# print("*".join(['a','x','b']))
# print("\n".join(['a','x','b']))
# print('1-2-3'.split('-'))
# print('+'.join('1-2-3'.split('-')))
# print('1234532'.partition('34'))
# print('123434532'.count('34'))

# def f(x):
#     return x%10
# print(sorted([123,12,33], key=f))


print(sorted([123,12,33], key=lambda x: x%10))
