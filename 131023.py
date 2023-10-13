# import datetime, locale
# locale.setlocale(locale.LC_ALL, 'ru')
# a=datetime.datetime.today()+datetime.timedelta(days=74)
# print(a)
# c=datetime.timedelta(days=30)
# for _ in range(5):
#     a+=c
#     print(a.strftime('%A, %d %m %y',))

# import datetime, locale
# print(datetime.datetime.strptime('22/04/2023 19.33, %A %d/%m/%y'))

# import calendar
# year, month=tuple(map(int,input().split()))
# print(year, month)
# print(*calendar.monthcalendar(year,month))

# import itertools
# for i in itertools.chain('abc', [1,2,3,4], (11,12,14,15)):
#     print(i, end='')

# import itertools
# lst=[[1,2,3],[11,22,33],[111,222,333]]
# for i in itertools.chain(*lst):
#     print(i,end=', ')
# for i in itertools.chain(lst):
#     print(i,end=', ')

# for i in zip('abc', [1,2,3,4], (11,22,33,44,55)):
#     print(i)

# import itertools
# for i in itertools.zip_longest('abc', [1,2,3,4], (11,22,33,44,55), fillvalue=0):
#     print(i)

# x=1
# y=2
# maxi=x if x>y else y
# print(maxi)

# number=5
# abso=number if number>=0 else - number
# print(abso)

# def flipflop(x):
#     return 'flip' if x=='flop' else 'flip'
# x='flip'
# for i in range(5):
#     print(flipflop(x))

# print([x**2 for x in range(5) if x%2==0])
# print(list(map(lambda x: x**2 if x**2%2==0 else "", range(5))))
#
# print([x**4 for x in range(20) if x%3==0])
#
# print([x for x in range(21) if x%2==0])

# lst=[1,-1,0,2,-33,123]
# new_list=[i if i>0 else 0 for i in lst]
# print(new_list)

# from string import ascii_letters
# letters='abcabcорпо'
# print([f'{let}-ДА' if let in ascii_letters else f'{let}-НЕТ ' for let in letters])

# from string import ascii_letters
# letters='abcabcорпо'
# vowels='aeiouAEIOU'
# print([f'{let}' if let in vowels else "" for let in letters])

# s=input()
# vowel=[i for i in s if i in 'aeiouAEIOU']
# print(''.join(vowel))



# def fb(x):
#     return 'FB' if x%15==0 else 'F' if x%3==0 else "B" if x%5==0 else x
# print(fb(15))
# for i in range(20):
#     print(fb(i), end=' ')

# words=['Я', "изучаю", 'Python']
# res=[letter for word in words for letter in word]
# print(res)

# key=['name', 'age', 'weight']
# value=['Lylu', '25', '100']
# print([(x,y) for x in key for y in value])

# matrix=[[i*j for i in range(5)] for j in range(5)]
# print(matrix)

# matrix=[[0,1,2], [3,4,5], [6,7,8]]
# flat=[num for row in matrix for num in row]
# print(flat)

# b=[x for x in range(1000)]
# a=(x for x in range(1000))
# for i in a:
#     print(i)
# print(type(a))
# import sys
# print(sys.getsizeof(a))
# print(sys.getsizeof(b))

# d={}
# for key in range(1,10):
#     d[key]=key**2
# print(d)
#
# d={key:key**2 for key in range(1,10)}
# print(d)
#
# d={key for key in range(1,10)}
# print(type(d), d)
#
# d={key:key**2 for key in range(1,10) if key%2==0}
# print(d)
#
# ages={'kevin':12,
#       'marcus':9,
#       'evan':31,
#       'nik':31,
#       'frik':36}
# f={k:v for k,v in ages.items() if v>16 if v%2==0}
# print(f)
#
# names=['Harry', 'Hermione', 'Ron', 'Nevill', 'Luna']
# index={k:v for k,v in enumerate(names)}
# print(index)
#
# dogits=['ноль', 'один', 'два','три','четыре','пять','шесть']
# dig={k:v for k,v in enumerate(dogits)}
# print(dig)

# def int_to_word(x):
#     str_x=str(x)
#     return ' '.join([d[int(i)] for i in str_x])
# int_to_word(int(input('-->')))

# from functools import cmp_to_key
# def ff(x, y):
#     if x>y: return 1
#     elif x == y: return 1
#     else: return -1
# lst=[1,5,2,-3,4,0]
# a=sorted(lst,key=cmp_to_key(ff))
# print(a)

from functools import cmp_to_key
def cmp_string(x,y):
    if len(x)<len(y): return -1
    elif len(x) == len(y): return 0
    else: return 1
x=['d','cc', 'bbb', 'aaaa']
print(sorted(x))
print(sorted(x, key=cmp_to_key(cmp_string)))
