# #Task 4.1
s=input('Введите числовое выражение').split()
d=0
if s[1]=="+":
    d=int(s[0])+int(s[2])
    print(d)
elif s[1]=="-":
    d=int(s[0])-int(s[2])
    print(d)
elif s[1]=="*":
    d=int(s[0])*int(s[2])
    print(d)
elif s[1]=="/":
    d=int(s[0])//int(s[2])
    print(d)

#Task 4.2
n = int(input("Введите число для расчета спирали"))
matrix=[]
for i in range(n):
	matrix.append(0)
for i in range(n):
	matrix[i] = [0] * n
x = 0
y = 0
dx = 1
dy = 0
for i in range(n * n):
	matrix[y][x] = i + 1
	if dx==1:
		direction = x + dx
	else:
		direction = y + dy
	if direction < 0 or direction == n or matrix[y + dy][x + dx] != 0:
		dx, dy = -dy, dx
	x += dx
	y += dy
for y in range(n):
	print(matrix[y])


#Task 4.3

s1=input('Введите предложение 1')
s2=input('Введите предложение 2')
marks = '''! ()-[]{};?@#$%:'"=+\,0123456789./^&amp;*_'''
sentence1=''
for i in s1:
	if i not in marks:
		sentence1=sentence1+i
sentence2=''
for i in s2:
	if i not in marks:
		sentence2=sentence2+i
dct1={}
for k in sentence1:
    dct1[k]=dct1.get(k,"")+k
dct2={}
for k in sentence2:
    dct2[k]=dct2.get(k,"")+k
if dct1==dct2:
    print(True)
else:
    print(False)
