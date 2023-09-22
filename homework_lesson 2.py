#Task 2.1
n = int(input("Введите число, таблицу умножения которого хотите определить"))
for i in range(1, 11):
    print(f'{n} * {i} = {n*i}')

# Task 2.2
lst=input("Введите список чисел через запятую без пробела, пример формата: '1212,3412,34'")
g=lst.split(",")
min=g[0]
for i in g:
    if float(i)<float(min): min=float(i)
print(min)


# Task 2.3
n = int(input("Введите число, факториал которого хотите определить"))
f = 1
for i in range(2, n + 1):
    f=f*i
print(f)



