##Генетический код
# s=input()
# res=''
# for i in range(len(s)-1):
#     if s[i]+s[i+1]=='АГ': res+='ГА'
#     elif s[i]+s[i+1]=='ГА': res+='АГ'
# print(res)

# s=list(input())
# i=0
# while i<len(s)-1:
#     if s[i]+s[i+1] in 'АГА':
#         s[i],s[i+1]=s[i+1],s[i]
#         i+=1
#     elif s[i]+s[i+1] in 'ТЦТ':
#         s.insert(i+1, "АГ")
#         i+=2
#     i+=1
# print("".join(s))

# lst=[[1,5,3],[2,44,1,4],[3,3]]
# def digits(lst):
#     res=0
#     for i in lst:
#         res+=len(str(i))
#     return res
# def digits_str(lst):
#     return len(str(lst))
# new_lst = sorted(lst, key=digits_str)
# print(new_lst)
# res=[]
# for i in new_lst:
#     res.append(sorted(i,reverse=True))
# print(res)

# def digits_str(lst):
#     return len(str(lst)):
# new_lst=sorted(lst, key=digits_str)

# lst=['sadasd', 'sdafdf', 'dafd']
# print(sorted(lst, key=lambda x:(-len(set(x)),x)))

# (lambda x:x%10)(1234)

# for i in range(10):
#     print(i, (lambda u: u*u)(i))

# quadrad=(lambda u:u*u)
# for i in range(10):
#     print(quadrad(i))
#
# s=(lambda x,y, *args, **kwargs: x*y)
# print(s(2,3))

# s=(lambda x,y=3:x*y)
# print(s(2))
#
# full_name=lambda f,s:f'Full_name:{f.title()} {s.title()}'
# print(full_name(' guido','van rossum'))


# gnirts=lambda s: s.lower()[::-1]
# print (gnirts('abcABCxyzXYZ'))
# gnirts=lambda s: s.swapcase()[::-1]
# print (gnirts('abcABCxyzXYZ'))

# lst=[1,2,462,3,4,5,6,7,8,9]
# print(sorted(lst, key = lambda x: (x%2,-x)))

# s=['abc','XYZ','Cde', 'uvW', 'All', 'you']
# print(sorted(s,key=lambda y: y.lower()))

# lst=[0,11,22,3]
# x=2
# print(min(lst, key=lambda y: abs(y-x)))

# lst=[0,1,2,3,4,5,6,7,8,9,10]
# print(list(filter(lambda x:x%3 ==0, lst)))
# print(lst)

# lst=[0,1,2,3,4,5,6,7,8,9,10]
# print(list(map(lambda x:x%3 ==0, lst)))

# lst=[123,234,345,456]
# print(list(map(lambda x:sum(map(int, (str(x)))), lst)))
#
# x=123
# print(sum(map(int, str(x))))
#
# spisok=[222,31,1,711,82,322]
# print(sorted(spisok,key=lambda x: str(x)[0]))
#
# spisok=[222,31,1,711,82,322]
# print(sorted(spisok,key=lambda x: str(x)[-1]))
#
# spisok=[222,31,1,711,82,322]
# print(sorted(spisok,key=lambda x: -int(str(x)[-1])))

# x,y=1,2
# maxi=x if x>=y else y
# print(maxi)

# lower = (lambda x,y: x if x<=y else y)
# print(lower(3,5))
# print((lambda x,y: x if x<=y else y)(10,8))

# dokhod=int(input())
# nalog=(lambda x: x*0.13 if x<=5000000 else 5000000*0.13+0.15*(x-5000000) )
# print(nalog(dokhod))

# lst=[("b", 100),("c", 1000),("x", 500),("e", 100),("a", 200)]
# s_s=sorted(lst ,key=lambda x: (x[0],x[1]))
# for name, bonus in s_s:
#     print(name, bonus)
# print((lambda x,y:x*y)(2,3))

# dct=dict.fromkeys([0,True,'a', 'b', (1,2),1],0)
# print(dct)
# dct.update({'a':123})
# print(dct)

# a={True:"abc", False:(lambda x:x*x), 3:{1,2,3}, '1': [1,2], "Город":"Спб"}
# print(a[False](3))
#
# st={0:{'name': "Ivanov", 'age':22},
#     1: {'name': "Petrov", 'age':23}}
# for i, j in st.items():
#     for s, t in j.items():
#         print(i,s,t)
#
# dct={1:123, 2:234, 3:{1:111, 2:222}}
# x=1
# for i, j in dct.items():
#     if i==x:
#         print(dct[i])
#         if type(j)==dict:
#             for a,v in j.items():
#                 if a==x:
#                     print(j[a])

# dct={1:123, 2:234, 3:{1:111, 2:222}}
# x=1
# for i, j in dct.items():
#     if type(j)==dict:
#         for a,v in j.items():
#             if a==x:
#                 print(j[a])

