# Task 1
def fun(res,element):
    tes = []
    def num(dct):
        res=[]
        for i, j in dct.items():
            if type(j)==int:
                res.append([i,j])
            elif type(j)==dict:
                res.extend(num(j))
        return res
    for i in num(res):
        if i[0]==element:
            tes.append(i[1])
    return tes
res={1:1, 2:2, 3:{2:22, 3:{1:111, 2:222, 3:{0:1111, 1:2222, 2:3333}}, 1:11,}, 6:22}
element=1
print(fun(res,element))


# Task 2
import re
string=input('Введите номер машины')
regex = r'[A-Z]\d{3}[A-Z]{2}178|[A-Z]\d{3}[A-Z]{2}78'
print(re.findall(regex, string))


# Task 3
text=input('Введите номер телефона')
import re
regex = r"\+?7\(\d{3}\)\d{3}-\d{2}-\d{2}|\+?7\(\d{3}\)\d{3}-\d{4}"
s=re.findall(regex, text)
print(s)
