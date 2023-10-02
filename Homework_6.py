#Task 6.1
DATABASE = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
while True:

    n = input('Введите римское число')
    last = n[-1]
    if last not in DATABASE:
        break
    else:
        res = DATABASE[last]
        for i in n[-2::-1]:
            if i not in DATABASE:
                break
            else:
                if DATABASE[i] >= DATABASE[last]:
                    res += DATABASE[i]
                else:
                    res -= DATABASE[i]
                last = i
    print(res)

#Task 6.2

n1=input('Книги, которые прочитал первый ученик (через запятую с пробелом)')
n2=input('Книги, которые прочитал второй ученик (через запятую с пробелом)')
set1=set(n1.split(", "))
set2=set(n2.split(", "))
w=set1.intersection(set2)
print(len(w))

#Task 6.3

s=str(input('Введите строку'))
numbers=""
letters=""
characters=""
for i in s:
    if i.isdigit()==True:
        numbers+=i
    elif i.isalpha()==True:
        letters+=i
    else:
        characters += i
for i in set(letters):
    print(i, end="")
else:
    print()
for i in set(numbers):
    print(i, end="")
else:
    print()
for i in set(characters):
    print(i, end="")

