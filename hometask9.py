#Task 9.1
DNK=['G', 'C', 'T', 'A']
RNK=['C','G','A','T']
DNK_RNK={}
DNK_RNK=dict(zip(DNK,RNK))
def dnk_transform(s):
    n=''
    for i in s:
        n+=DNK_RNK[i]
    return n
print(dnk_transform(input('Введите ДНК')))

#Task 9.2
s=input("Введите одно слово")
d=input('Введите слова через пробел').split()
vowels='ауоыиэяюёе'
lst1=[]
lst2=[]
t=0
for i in s:
    t=t+1
    if i in vowels:
        lst1.append(t)
for i in d:
    f = 0
    lst3=[]
    for j in i:
        f = f + 1
        if j in vowels:
            lst3.append(f)
    lst2.append(lst3)
p=-1
for i in lst2:
    p+=1
    if i==lst1:
        print(d[p])

#Task 9.3
text=input('Введите текст')
dct={}
for i in text.lower():
    dct[i]=dct.get(i,0)+1
def s(x):
    return -x[1], x[0]
sorted_dct=dict(sorted(dct.items(), key=s))
w = 0
for i, j in sorted_dct.items():
    w += 1
    print(i, '-', j)
    if w==10:
        break