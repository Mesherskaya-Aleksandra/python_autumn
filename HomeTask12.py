#Task 1
def t(x):
    lst=[[],[]]
    s=-1
    for i in x:
        s+=1
        if i==min(x):
            lst[0].append(s)
    r=-1
    for i in x:
        r+=1
        if i==max(x):
            lst[1].append(r)
    return lst
print(t(list(map(int, input('Введите список').split()))))

#Task 2
n=10
print(*[k for k in range(1,n+1) for s in range(1,k+1)], sep=", ")

#Task3
def f(s):
    lst=(s.split(','))
    lst1=[]
    lst2=[]
    lst3=[]
    lst4=[]
    t=-1
    for i in lst:
        lst1.append(i.split('-'))
    for i in lst1:
        t += 1
        lst2.append([])
        for j in i:
            lst2[t].append(int(j))
    for i in lst2:
        if i[1]-1>i[0]:
            for k in range(i[0]+1, i[1]):
                i.append(k)
        elif i[1]==i[0]:
            i.pop()
    for i in lst2:
        lst3.append(sorted(i))
    for i in lst3:
        for j in i:
            lst4.append(j)
    return lst4
print(f(input('Введите диапазон в формате: "1-2,4-4,3-6"')))