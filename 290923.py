# n=int(input())
# lst1=[0,1]
# for i in range(1, n+1):
#     lst2=[]
#     for j in range(i):
#         lst2.append(lst1[j])+lst1[j+1])
#         lst2.append(0)
#         print()
# lst1=lst2.copy()
#
#
# n=int(input())
# lst=[0,1,0]
# print(1)
# for i in range(2, n+1):
#     x=lst[0]
#     for j in range(1, i+1):
#         y=x+lst[j]
#         print(y, end=' ')
#         x=lst[j]
#         lst[j]=y
#     print()
#     lst.append(0)

# n=int(input())
# for i in range(1, n+1):
#     if n%i==0:

# n = int(input())
# k=2
# dct={}
# while n>1:
#     while n%k ==0:
#         dct[k]=dct.get(k,0)+1
#         n//=k
#     print(n, k, dct)
#     k+=1
# for k,v in dct.items():
#     print(k,v)
#
# n = int(input())
# a,b=0,1
# for i in range(n):
#     a,b=b, a+b
#     print(a, end=' ')

# dct={1:11, 2:22, 3:33}
# k=2
# print(dct.pop(k,0))
# print(dct)
# print(dct.pop(k,444))
# print(dct)
# print(dct.popitem())
# dct={1:11, 2:22, 3:33}
# print(sorted(dct))
# dct={1:11, 2:22, 3:33}
# print(sorted(dct, reverse = True))
# dct={1:11, 2:22, 3:33}
# print(sorted(dct, reverse = False))
# dct={1:11, 2:22, 3:33}
# print(sorted(dct.values()))


# x=True
# print(True==1)
# print(True+1)
# x=True
# print(str(x))
# print(int(x))
# print(True+True)

#
# print(ord("A"))
# print(chr(65))
# for i in range(65,90):
#     print(chr(i), end="")
# for i in range(97,123):
#     print(chr(i), end="")
# print(chr(1010))
# for i in range(1040,1040+32):

#     print(chr(i), end="")
# print(chr(1072))
# print(chr(1072+32))
# print(ord('ё'), ord('Ё'))
# print(chr(20320))


# ord_a=ord('A')
# for i in range(ord_a, ord_a +26):
#     print(i, chr(i))

# 'a'=='a'
# 'a'>'b'
# 'aa'>'ab' #первый символ где есть расхождение
#
# a=[1,2,3]
# b=a
# a=b
# a is b
#
# a=[1,2,3]
# b=[1,2,3]
# a is b #проверяет, на что ссылается
#
#
# a=[1,2,3]
# b=a
# a is b
#
# x=10
# y=20
# if x>0 or y/0: #Python смотрит что первое усовие True, на второе не обращает внимание, потому печатает
#     print(111)

# x = 10
# y = 20
# if x > 0 and y / 0:
#     print(111)

# if -111:
#     print(0)
# else:
#     print(1)

# lst=[1,2,3]
# if len(lst)>0: #длина lst больше нуля
#     print(0)
# else:
#     print(1)


# year = int(input())
# if year%4!=0:
#     print('Невисокосный')
# elif year%400==0:
#     print('Високосный')
# elif year%100==0:
#     print('Невисокосный')
# else: print('Високосный')

# print(2**3**4)#вычисления справа на лево
# print((2**3)**4)
# print(2**(3**4))

# a=None
# a==None
# dct={None:123}
# dct[None]

# s=input()
# v,c, res=[],[], ""
# for letter in s:
#     if letter in 'aeoiu':
#         v.append(letter)
#     else:
#         c.append(letter)
# if abs(len(v) - len(c))>1:
#     print('Impossible')
# else:
#     if len(v)== len(c):
#         for i in range(len(v)):
#             res+= c[i] + v[i]
#             print(s)
#     elif len(v)<len(c):
#         for i in range(len(v)):
#             res+=c[i]+v[i]
#         res+=c[-1]
#     else:
#         for i in range(len(c)):
#             res += v[i] + c[i]
#         res+=v[-1]
# print(res)

# s=input()
# v,c, res=[],[], ""
# for letter in s:
#     if letter in 'aeoiu':
#         v.append(letter)
#     else:
#         c.append(letter)
# if abs(len(v) - len(c))>1:
#     print('Impossible')
# else:
#     for i, j in zip(c,v):
#         res+=i+j
# print(res)


# a=set([1,2,3, -1, True, False, (1,2,3)])
# print(a, type (a))
# print(len(a))

# lst = []
# dct={}
# st=''
# sss = {}
# print(type(sss))
# sss=set()
# print(type(sss))

# lst=[1,2,2,3,3,3,4,4,4,4]
# tes=set(lst)
# print(tes)
# print(len(tes))
# lst=(1,2,2,3,3,3,4,4,4,4)
# print(len(set(lst)))

# month={'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug'}
# for m in month:
#     print(m, end='')
# print(sorted(month))#множество не сортируется, sorted из всего делает список
# print('May' in month)#срезы индексы не работают

# tes=set(map(int, input().split()))
# print(tes)
# print(sum(tes) / len(tes))
#
# tes=set([1,2,3])
# print(tes)
# tes.add(4)
# print(tes)

# month={'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug'}
# print(month)
# month.add('Sep')
# print(month)

# s=input()
# tes=set(s)
# print(tes)
# print(len(tes)==33)

# a={1,2,3,45}
# b={4,5,6,45}
# print(a-b)
# print(a.difference(b))
# print(a^b)

# s=''
# lst=['мама', "мыла", "раму"]
# for i in lst:
#     s=s+i
# n=set(s)
# print(len(n))

#
# lst=['мама', "мыла", "раму"]
# res=set()
# for i in lst:
#     res|=set(i)
# print(res)


# def summ(x,y):
#     result=x+y
#     return result
# a=100
# b=200
# print(summ(a,b))
# x,y=1,2
# print(summ(x,y))

def convert_to_far(temp):
    result=9/5*temp+32
    return result
print(convert_to_far(18))
