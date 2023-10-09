# su, hm = 0,0
# while True:
#     za=int(input())
#     if za==0: break
#     su+=za
#     hm+=1
# print(su/hm)
#
# s=input()
# res=[0]*10
# for k in s:
#     i=int(k)
#     res[i]+=1
# for j in range(10):
#     print(f'{j}-{res[j]}')
#
# sentence=input().split()
# cur_len=0
# for word in sentence:
#     if len(word)>cur_len:
#         cur_len=len(word)
# for word in sentence:
#     if len(word)==cur_len:
#         print(word)


# x,y,z=0,0,0
# cor1=(x,y,z)
# cor1=(100,200,300)
# print(x,y,z)
#
# cort=(123, 234, 345, 456, 567, 678, 789, 890)
# n=int(input())
# index=0
# for i,j in enumerate(cort):
#     index = i
#     if n > j:
#         break
#     else:
#         index=i+1
#         break
# # index=3
# cort1=cort[:index]+tuple((n,))+cort[:index]
# # cort1=(1,2,3)+(4,5,6)
# print(cort1)
#
# tpl=(1,2,3,[11,22,33])
# tpl[3].append(444)
# print(tpl)
# tpl[3].pop()
# tpl1=2*tpl
# print(tpl1)

# hm={}
# s=input()
# for k in s:
#     if k not in hm:
#         hm[k]=0
#     hm[k]+=1
#     print(hm)
# for k in hm:
#     print(k,hm[k])

# s=input()
# dct={}
# for k in s:
#     j=int(k)
#     if k not in dct:
#         dct[j]=0
#     dct[j]=dct[j]+1
#     print(dct)
#
# s={}
# s['name']='Михаил'
# s['фамилия']='Зимнев'
# s['mail']='m.zimnev@yandex.ru'
# s['name']='Маша'
# print(s)
# print(s['name'])
# s['age']=18
#
# for k in s:
#     print(k, s[k])
#
# z=[]
# print(type(s), type(z))
# print('age' in s)
# print('color' in s)

# dct={}
# while True:
#     s=input()
#     if s=='0':
#         break
#     if s in dct:
#         dct[s]+=1
#     else:
#         dct[s]=1
# for k in dct:
#     print(k, dct[k])
#
# dct={}
# dct[True]='aaa'
# dct[False]=123
# print(dct)
# tcd={}
# tcd[False]=123
# tcd[True]='aaa'
# print(tcd)
# print(dct==tcd)
# print([0,1]==[1,0])

#
# dct={1: 'один',
#      2: 'два',
#      3: 'три'}
# n=input()
# for i in n:
#     print(dct[int(i)], end=' ')
#
# s={}#как создать словарь
# s[1]=123
# print(s)

# a=dict(name='m', age='16')
# print(a)

# a=[123,2323]
# b=['fsgf','fgfaf']
# c=dict(zip(a,b))
# print(c)

# month2=[31,28,31,30,31,30,31,31,30,31,30,31]
# month1=['1','2','3','4','5','6','7','8','9','10','11','12']
# month = dict(zip(month1, month2))
# while True:
#     y=int(input())
#     m=int(input())
#     if y==0: break
#     if y%4==0 and m==2: print(29)
#     else:
#         print(month[m])


# month={31:[1,3,5,7,8,10,12],
#        30:[4,6,9,11],
#        28:[28]}
# while True:
#     y=int(input())
#     m=int(input())
#     if y==0: break
#     if y%4==0 and m==2: print(29)
#     else:
#         for i in month:
#             if m in month [i]:
#                 print(i)
#                 break

# dct={}
# dct[1]='adasfa'
# dct['asd']='adasfa'
# dct[True]=False
# dct['print']=print
# del dct[1]
# print(dct)
# print(len(dct))
# print(dct.keys())
# print(dct.values())

# s='я я хочу есть есть'
# dct={}
# for k in s.split():
#     if k not in dct:
#         dct[k]=0
#     dct[k] = dct[k] + 1
# print(dct)
# mi=min(dct.values())
# for i in dct:
#     if dct[i]==mi:
#         print(i)
#
# dct={1:11,
#      2:22}
# x=1
#
# print(dct.get(x, 0))
# x=2
# print(dct.get(x, 0))
# x=3
# print(dct.get(x, 0))
#
# x=11
# print(x in dct.values())
#
# if x in dct:
#     print(dct[x])
# else:
#     print(0)
#
# s=input()
# dct={}
# for k in s:
#     dct[k]=dct.get(k,0)+1
#     print(dct)

# s=input()
# dct={}
# for k in s:
#     dct[k]=dct.get(k,"")+k
#     print(dct)


p, q = input().split()
pp,qq={},{}
for i in p:
    pp[i]=pp.get(i,0)+1
for i in q:
    qq[i]=qq.get(i,0)+1
print(pp==qq)
