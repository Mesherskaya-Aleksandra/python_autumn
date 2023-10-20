# def f(x,y):
#     try:
#         return x/y
#     except:
#         return x,y
#     finally:
#         print('finally')
# print(f(1,2))

# ress = {1: 0, 2: 1}
# def fibo(n):
#     if n not in ress:
#         if n==1: return 0
#         elif n==2: return 1
#         else:
#             ress=fibo(n-1)+fibo(n-2)
#     return ress[n]
# print(fibo(15))
# print(d)

# def fibo(n):
#     match n:
#         case 1:return 1
#         case 2: return 1
#         case _: return fibo(n-1)+fibo(n-2)
# print(fibo(int(input())))
#
# import sys
# print(sys.version)

# def num(lst):
#     res=[]
#     for i in lst:
#         if type(i)==int:
#             res.append(i)
#             print('----',res)
#         elif type(i)==list:
#             res.extend(num(i))
#             print('=====',res)
#     return res
# lst=[1,'a',2,[11,'cd',22,[111,222,[111,222,'sd']]]]
# print(num(lst))

# lst=[1,'a',2,['b',['cd',22,3],'e']]
# def num(lst):
#     res=''
#     for i in lst:
#         if type(i)==str:
#             res+=i
#             print('----', res)
#         elif type(i) == list:
#                 res+=num(i)
#                 print('=====',res)
#     return res
# print(num(lst))

# import sys
# print(sys.getrecursionlimit())

# import re
# string='Числа +99, -72, 81 и 999 делятся на 9'
# print(re.findall(r"[+-]?\d+ ", string))

# print(r'\\\'')

# import re
# string='jhgudf424awyafddfafra4254faeag78gh6i76'
# regex=r'a\d'
# print(re.findall(regex, string))

# import re
# string='1 123 1345 6189 1 12 122'
# regex=r'1\d\d'
# print(re.findall(regex, string))

# import re
# string='Косой косой косил траву на косе'
# regex=r'\b\w+\b'
# print(re.findall(regex, string))

# import re
# string='Косой косой покосил траву на косе'
# regex=r'\b\w*[Кк]ос\w+\b'
# print(re.findall(regex, string))

# import re
# string='Косой косой покосил траву на косе'
# regex=r'\b\w*кос\w*\b|\b\w*Кос\w*\b'
# print(re.findall(regex, string))

# import re
# string='cat cet cit cot cut c#t c{t c2t'
# regex=r'c[a-i]t'
# print(re.findall(regex, string))

# import re
# string='cat cet cit cot cut c#t c{t c2t'
# regex=r'c.t'
# print(re.findall(regex, string))

# import re
# string='cat cet cit cot cut c#t c{t c2t'
# regex=r'c[^a-i]t'
# print(re.findall(regex, string))

# import re
# string='cat cet cit cot cut c#t c{t c2t'
# regex=r'c[^ai]t'
# print(re.findall(regex, string))

# import re
# string='123-456-7890 999-999-9999 123-456-90'
# regex=r'\d{3}-\d{3}-\d{4}|\d{3}-\d{3}-\d{2}'
# print(re.findall(regex, string))

# import re
# string='A123BC78 X987YZ178 P777PP78 V666VV147'
# regex=r'[A-Z]\d\d\d[A-Z]{2}1?78'
# print(re.findall(regex, string))

# import re
# s='Java blablabla'
# print(re.sub(r'Java', r'Python',s))

# import re
# s='Javaerwt blablabla JavaScript'
# res, n = re.subn(r'Java\w+', r'Python',s)
# print(res, n)

# import re
# s='(095) (812) 095 (123)'
# res, n = re.subn(r'(095)', r'812',s)
# print(res, n)

# import re
# s='/095/ /812/ 095 /123/'
# res, n = re.subn(r'/095/', r'/812/',s)
# print(res, n)

import re
s='0 2 3 12 222 5 42 3 43 35 17'
regex=r'\d*[02468]\b'
print(re.findall(regex, s))

# res, n = re.subn(r'/095/', r'/812/',s)
# print(res, n)