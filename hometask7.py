#Task 7.1
def nod(*args):
    st=set()
    st1=set()
    res = 1
    for i in args:
        res*=i
    for i in range(1, res+1):
        for j in args:
            if i%j==0:
                st.add(i)
    lst=list(st)
    for i in lst:
        for j in args:
            if i%j!=0:
                st1.add(i)
    d=st.difference(st1)
    return min(list(d))
print(nod(4,5,6,7,8))


#Task 7.2
def code(string,n):
    alphabet='abcdefghijklmnopqrstuvwxyz'
    d=''
    new_alphabet=alphabet*(n+1)
    dct={}
    for i in alphabet:
        dct[i]=new_alphabet[new_alphabet.find(i)+n]
    for i in string:
        d+=dct[i]
    return d
str=input("Введите строку")
a=int(input('Введите шаг'))
print(code(str,a))


#Task 7.3
def func(lst):
    lst1=[]
    for i in lst:
        for j in i:
            lst1.append(j)
    lst2=sorted(lst1,reverse=True)
    return lst2[2], lst2[1], lst2[0]

print(func([[1,2,3],[23,5,6],[1,2,3]]))

