#Task 3.1

s = 0
i = 0
while True:
    salary = int(input('Введите зарплату'))
    if salary < 0:
        print('ошибка')
    else:
        s = s + salary
        i = i + 1
        if salary == 0:
            break
print(s / (i - 1))

# Task 3.2

n=input('Введите число')
lst=[]
for i in n:
    lst.append(i)
st=set(lst)
lst1=list(st)
for i in lst1:
    print(f'{i} - {n.count(i)}')

# Task 3.3

phrase=input('Введите слова через пробел')
lst1=phrase.split(' ')
lst2=[]
lst3=[]
for i in lst1:
    lst2.append(len(i))
maximum=max(lst2)
for i in lst1:
    if len(i)==maximum:lst3.append(i)
for i in lst3:
    print(i, end = " ")