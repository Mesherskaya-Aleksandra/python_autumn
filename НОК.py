n=int(input())
lst1=[0,1]
for i in range(1, n+1):
    lst2=[0]
    for j in range(i):
        lst2.append(lst1[j]+lst1[j+1])
        print(lst2[-1], end=' ')
    lst2.append(0)
    print()
    lst1=lst2.copy()


