#Task 13.1
n=int(input("Введите число для формирования последовательности"))
s=0
lst=[]
while s<n:
    s += 1
    lst.append(s)
    lst.append(-(s+1))
    s += 1
if n%2==0:
    print(*lst, sep=', ')
else:
    del lst[len(lst)-1]
    print(*lst, sep=', ')

# Task 13.2
def func():
  n = 0
  while True:
      if str(n) == str(n)[::-1]:
          yield n
      n += 1

palindrome = func()
for i in range(100):
  print(next(palindrome))

#Task 13.3
def func(numbers):
  for i in numbers:
      if i % 2 != 0:
          yield i

lst = list(map(int, input().split()))
s = func(lst)
lst1=[]
for i in s:
    lst1.append(i)
print(*lst1, sep=', ')
