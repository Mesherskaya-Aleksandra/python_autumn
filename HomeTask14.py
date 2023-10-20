#Task 14.1
def func(n):
    if n < 10:
        return 1
    else:
        n/=10
        return 1 + func(n)
print(func(int(input('Введите число для расчета количества его цифр'))))

#Task 14.2
def func(n):
    if n < 10:
        return n
    else:
        s=n%10
        n //= 10
        return s + func(n)
print(func(int(input('Введите число для расчета суммы его цифр'))))

#Task 14.3
def tri_2(n):
    print("*" * n)
    n-=1
    if n>0:
        tri_2(n)
    if n>0:
        print("*"*(n+1))
    return
tri_2(int(input('Введите число для треугольника')))