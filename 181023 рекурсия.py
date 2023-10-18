# def func():
#     print("func")
#     input()
#     func()
# func()

# def func(n):
#     print(111, "func",n)
#     # input()
#     n-=1
#     if n>0:
#         func(n)
#     print(222, 'cnuf', n)
#     return
# func(3)

# def fact(n):
#     if n<=1:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(3))

# def stars(n):
#     if n==1:
#         print("*")
#     else:
#         print("*"*n)
#         n-=1
#         stars(n)
# stars(5)

# def stars(n):
#     print("*"*n)
#     if n>1:
#         n-=1
#         stars(n)
#     return
# stars(5)


#
# def sumn(n):
#     if n==1:
#         return 1
#     else:
#         return n +sumn(n-1)
# print(sumn(10))

# def fibo(n):
#     print('fibo', n)
#     if n==1:
#         return 0
#     if n==2:
#         return 1
#     else:
#         return fibo(n-1)+fibo(n-2)
# for i in range(1,10):
#     print(fibo(i))
# print(fibo(10))
