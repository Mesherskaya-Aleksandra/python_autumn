n=input('Введите число')
lst1=[0,1,2,3,4,5,6,7,8,9]
for i in lst1:
    print(i, "-", n.count(str(i)))
