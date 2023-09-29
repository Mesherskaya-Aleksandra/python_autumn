#Task 5.1
n =int(input('Введите число для треугольника Паскаля'))
lst = []
for i in range(0, n):
    s = [1] * (i + 1)
    for j in range(i + 1):
        if j != 0 and j != i:
            s[j] = lst[i-1][j-1] + lst[i-1][j]
    lst.append(s)
for i in lst:
    print(*i)


#Task 5.2
n=int(input("Введите число, чтобы определить его делители"))
lst=[]
lst1=[]
for i in range(2,n):
    if n%i==0:
        lst.append(i)
print(*lst)

#Task 5.3
n=int(input("Введите число, до которого включительно хотите получить последовательность Фибоначчи"))
lst=[1,1]
if n<0:
    print('ошибка')
if n==1:
    print(1)
else:
    for i in range(n-2):
        lst.append(lst[i]+lst[i+1])
    print(*lst)











