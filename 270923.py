# s = input().split()
# a, b = int(s[0]), int(s[2])
# dct={"+": a+b,
#      "-": a-b,
#      "*": a*b,
#      "/": a/b}
# print(dct)
# print(dct[s[1]])
#
# n=int(input())
# m={}
# for i in range(n):
#     for j in range(n):
#         m[i,j]=0
# x, y, dx, dy = 0, 0, 0, 1
# for k in range(1, n*n +1):
#     m[x,y]=k
#     if m.get((x+dx, y+dy), -1)!=0:
#         if (dx,dy) == (0,1):
#             dx=1; dy=0
#         elif (dx, dy) == (1, 0):
#             dx = 0; dy = -1
#         elif (dx, dy) == (0, -1):
#             dx = -1; dy = 0
#         elif (dx, dy) == (-1, 0):
#             dx = 0; dy =1
#     x+=dx
#     y+=dy
# len_nn = len(str(n*n))
# for i in range(n):
#     for j in range(n):
#         print(f"{m[i,j]:{len_nn}}", end=" ")

# import string
# print(*dir(string))
# print(*string.ascii_letters)
# print(*string.digits)
#
# tpl = (123, 234, 345, 456, 567, 678, 789, 890)
# n=int(input())
# if n<=tpl[0]:
#     res= (n,)+tpl
# elif n>= tpl[-1]:
#     res=tpl+(n,)
# else:
#     for i in range(len(tpl)-1):
#         if tpl[i]<=n<=tpl[i+1]:
#             res=tpl[:i+1]+(n,)+tpl[i+1:]
#             break
# print(res)
#

#
# dct={1:111,
#      2:222,
#      2:333}
# print(dct.get(4, -123))
# print(dct)
# print(dct.setdefault(5,555))
# print(dct)

# n=int(input())
# syn={}
# for i in range (n):
#     s = input("два синонима").split()
#     syn[s[0]]=s[1]
#     syn[s[1]]=s[0]
# while True:
#     p=input()
#     if p=='exit': break
#     print(syn[p])

# dct = {1:111,
#        2:222}
# dct.clear()
# print(dct)

# dct = {1:111,
#        2:222}
# tcd=dct.copy()
# print(tcd)

# dct = {1:111,
#        2:222}
# for key,value in dct.items():
#     print(key,value)
# x=dct.values()
# print(x)
# dct[3]=333
# print(x)
# for k in dct:
#     print(k)


# lst=list(map(int, input().split()))
# dct={}
# for i,j in enumerate(lst):
#     if j in dct:
#         dct[j].append(i)
#     else:
#         dct[j]=[i]
# print(dct)

# dct = {1:111,
#        2:222}
# for i, j in dct.items():
#     print(i, j)

# dct = {1:111,
#        2:222}
# for i in dct.items():
#     print(f'{i=}{i[0]=,}{i[1]=}')

# x=dict.fromkeys([1,2,3,4,1],0)
# print(x)

# dct={1:111,
#      2:222}
# tcd={3:333,
#      4:444}
# dct.update(tcd)
# print(dct)

# sales_report={}
# s=0
# while True:
#     s=input()
#     if s=='0':
#         break
#     p=s.split()
#     if p[0] not in sales_report:
#         sales_report[p[0]]=0
#     sales_report[p[0]]+=int(p[1])
# for i, j in sales_report.items:
#     print(i,j)

# print(round(1.14535, 1))

# f=float(input())

# a=float('inf')
# print(a)


# for i in range(16):
#     print(i, bin(i), hex(i))

# print(int('10', 16))

# x=int(input())
# sec=x%60
# print(sec)
# y=x//60
# minu=y%60
# hour=y//60
# print(hour,minu,sec)

# a=123_456_789
# print(a)

# n=int(input())
# for i in range(2,n):
#     if n%i==0:
#         print('Составное')
#         break
#     else:
#         print('Простое')
