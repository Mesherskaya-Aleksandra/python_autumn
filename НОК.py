s=list(map(int, input().split()))
def nod(a,b):
    while a!=0 and b!=0:
        if a>b:
            a=a%b
        else:
            b=b%a
    return a+b
def nok2(a,b):
    return a*b//nod(a,b)
x=1
for i in s:
    x=nok2(x,i)
print(x)



