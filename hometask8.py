#Task 8.1
def repl(s):
    d=s.replace('АГ', 'ГА')
    f=d.replace('ЦТ', 'ЦАГТ')
    return f
print(repl(input("Введите генетический код")))

#Task 8.2
lst = [[675765756776,7],[1,5,3], [2,44,1, 4], [3,3], [44,55,66]]
dct={}
ctd={}
s=-1
d=''
for i in lst:
    s+=1
    for j in i:
        d=d+str(j)
        dct[s]=len(d)
for i in dct:
    ctd[i]=dct.get(i,0)-dct.get((i-1),0)
sorted_dict = {}
for i in sorted(ctd.values()):
    for k in ctd.keys():
        if ctd[k] == i:
            sorted_dict[k] = ctd[k]
            break
lst1=[]
for i in sorted_dict:
    lst1.append(sorted(lst[i], reverse=True))
print(lst1)

#Task 8.3
def f(x):
    st=set()
    for i in x:
        st.add(i)
    l=len(st)
    return l
lst = input('Введите список через пробел').split()
print(sorted(sorted(lst), key = f, reverse=True))
