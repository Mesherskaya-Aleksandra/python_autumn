# def roman_to_decimal(number):
#     dct = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#     res = 0
#     while number!="":
#         for i in dct:
#             if number.startswith(i):
#                 res+=dct[i]
#                 number=number[len(i):]
#                 break
#         return res
# print(roman_to_decimal(input()))


# s=set(input().split(", "))
# z=set(input().split(", "))
# print(len(s.intersection(z)))

# tes={}
# mno=set()
# print(type(tes), type(mno))
#
# def pod_nalog(dokhod):
#     result=dokhod*0,13
#     return result
#
# while True:
#     dokhod=float(input())
#     if dokhod<=0: break
#     print(dokhod, pod_nalog(dokhod), dokhod*0,13)


# def pod_nalog(dokhod, percent=13):
#     result = dokhod * percent/100
#     return result
# while True:
#     dokhod1 = float(input())
#     percent1=float(input())
#     if dokhod1 <= 0: break
#     print(dokhod1, pod_nalog(dokhod1, percent1))
#     print(dokhod1, pod_nalog(dokhod1))

# def my_function(arg1, arg2, arg3):
#     print(arg1, arg2, arg3)
# my_function(arg2=2,arg3=3, arg1=1)

# def my_function(arg1, arg2, *args):
#     print(arg1, arg2)
#     for i in args:
#         print(i)
# my_function(123, 111, 222, 45645,4,7,8)

# def multi(*args):
#     res = 1
#     for i in args:
#         res*=i
#     return res
# print(multi(100))

# def multi(**kwargs):
#     print(kwargs)
#     res=1
#     for i in kwargs.values():
#         res*=i
#     return res
# print(multi(a=100, b=200))

# def multi(**kwargs):
#     print(kwargs)
#     res=1
#     for i,j in kwargs.items():
#         res*=j
#     return res
# print(multi(a=100, b=200))

# def multi(**kwargs):
#     res1=1
#     res2=""
#     for j in kwargs.values():
#         if type (j)==int:
#             res1*=j
#         elif type(j)==str:
#             res2+=j
#         else:
#             print(j)
#     return res1, res2
#     return res
# print(multi(a='100', c=200000, x='rer', b=200, f=5.4, k=[3,3,3]))


# def all_args(var1, *args, **kwargs):
#     print(var1)
#     print(args)
#     print(kwargs)
#
# all_args(1,2,3, x=100)

# def all_args(var1, *args, **kwargs):
#     print(var1)
#     print(args)
#     print(kwargs)
#
# all_args(1, x=100)

# def all_args(var1, *args, **kwargs):
#     print(var1)
#     print(args)
#     print(kwargs)
#
# all_args(1)

# def all_args(var1, xyz, *args, **kwargs):
#     print(var1)
#     print(args)
#     print(kwargs)
#
# all_args(1,True)

# def pod_nalog(dokhod, *args):
#     if len(args)==0:
#         return dokhod*13/100
#     else:
#         return dokhod*args[0]/100
#
# print(pod_nalog(100,13))
# print(pod_nalog(100,13,10,20))
# print(pod_nalog(100))
#
#
# def pod_nalog(dokhod, *args):
#     if args==():
#         return dokhod * 13 / 100
#     else:
#         res=[]
#         for i in args:
#             res.append(dokhod*i/100)
#         return res
#
#
# print(pod_nalog(100, 13))
# print(pod_nalog(100, 13, 10, 20))
# print(pod_nalog(100))


# def uni_let(lst):
#     dct={}
#     for i in lst:
#         dct[i]=dct.get(i,0)+1
#     return dct.keys(), dct.values()
# print(uni_let(['All', 'your', 'need', 'is', 'love']))

# def uni_let(lst):
#     s=''.join(lst)
#     string=''.join(sorted(set(s)))
#     return string, len(string)
# print(uni_let(['all', 'your', 'need', 'is', 'love']))
# print(uni_let([]))
# print(uni_let('rgrqgrqg'))

# def func(n):
#     def func_1(p):
#         return p*p
#     def func_2(w):
#         return w+w
#     if n<10:
#         return func_1(n)
#     else:
#         return func_2(n)
# x=int(input())
# print(func(x))
#
# x=100
# def ddd(y):
#     z=y*y
#     return z
# print(ddd(x))


# x=100
# def ddd(y):
#     global z
#     z=y*y
#     return z
# print(ddd(x))
# print(z)

num =123
print(111,num)
def counter():
    num=0
    def incr():
        nonlocal num
        num+=1
        return num
    x=incr()
    x = incr()
    return x
print(counter())
print(222, num)


















