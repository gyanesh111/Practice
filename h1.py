# # a='good morning'
# # # print(a)
# # print(a[::-1])

# a,b=int(input("value")),int(input("value"))
# print(c)

# a='hello'
# print(a[4])

# a=eval(input("enter the value"))
# print(type(a),a)

# n=int(input("value"))
# print(abs(n))

# a,b,c=int(input("")),int(input("value")),int(input(""))
# if a>b and a>c:
#     print("a is greater")
# elif b>c:
#     print("b is greater")
# else:
#     print("c is gretaer")

# un='gyan'
# pd='math11'
# uname=input("enter the username")
# pwd=input("enter the password")
# if uname==un:
#     if pwd==pd:
#         print("login")
#     else:
#         print("wrong password")
# else:
#     print("wrong username")

# dt='hel'
# if len(dt)%2==0:
#     print("students are GREAT")
# else:
#     print("they arent")

# data=eval(input("enter tha data "))
# if type(data) in [str, list, set, dict, tuple]:
#     if len(data)%2==0:
#         print("studens are great")
#     else:
#         print("arent")
# else:
#     print("not the collection")
# n=int(input("value"))
# sum=0
# while n!=0:
#     ld=n%10
#     sum=sum+ld
#     n=n//10 
#     # here we are taking he last didgit out of the value 
# print(sum)
            
# s=input("value")
# i=0
# while i<len(s):
#     if 'A'<=s[i]<='Z':
#         i=i+s[i]
#         print(i)
#     else:
#         print("no")
#         break

# l=eval(input("list collection"))
# i=0
# while i<len(l):
#     if type(l[i])==complex:
#         print(l[i])
#     i=i+1

# def natural():
#     n=int(input("enter the no"))
#     sum=0
#     for i in range(1,n+1):
#         sum=sum+i
#     return sum
# print(natural()

# def pr(n):
#     n=int(input("enter the no"))
#     if n%2==0:
#         return True
#     else:
#         return False
# print(pr(n))


# def num(n):
#     return n%2==0
# print(num(7))
    
# def sma():
#     return 10,20,30
# print(sma())

# def singlepc(*a):
#     print(type(a))
#     print(a)
#     print()
# singlepc(10,20,30,40, 6.7,50,3+5j)
# singlepc(23)

# singlepc()
# a=(1,2,3,4)


# def unpck(v1,v2,v3,v4):
#     print(v1,v2,v3,v4)
# unpck(*(1,2,3,4))

# x=10
# y=20
# def hello():
#     a='hai'
#     c='bye'
#     print(x,y)
#     print('nothing')
#     print(a,c)
# hello()
# print(x,y)
# # print(a)

# def hi(n, i=1):
#     if i>n:
#         print(i, end='')
#         hi()

# class python:
#     classroom=203
#     trainer='keshav'
# s1=python()
# s2=python()
# print(s1)
# print(s2)
# print(python)


# class hello:
#     bname='hdfc'
#     location="bengaluru_urban"
#     def __init__(self, ename, address, phno, dept ):
#         self.ename=ename
#         self.address=address
#         self.phno=phno
#         self.dept=dept
#     def display(self):
#         print(self.ename, self.address, self.phno, self.dept)
#     def withdraw()

# class A:
#     __a=10
#     __b=20
#     def __init__(self, c,d):
#         self.c=c
#         self.d=d
#     @classmethod
#     def __disp(cls):
#         print(cls.__a, cls.__b)
#     @staticmethod
#     def __hello():
#         print("good morning")
# obj1=A(100,100)
# # A.__disp() 
# A._A__

# a=[10,20,30,40]
# i=iter(a)
# print(i)
# print(next(i))
# print(next(i))

# def sm():
#     print('hai')
#     yield 1
#     print("hello")
#     yield 2
#     print("chelllo")
#     yield 3
#     print("bello")
#     yield 3
# # print(sm()) 
# print(list(sm())) 


# def sam():
#     n=int(input("enter the value"))
#     for i in range(1,n+1):
#         yield i
# print(list(sam()))


# def lent():
#     s="there is no class tomorrow"
#     t=s.split()
#     for i in t:
#         yield len(i)
# print(list(lent()))

# def fb(func):
#     def inner(*args, **kwargs):
#         print("go to fb.com")
#         print("login")
#         func(*args, **kwargs)
#         print("logout")
#     return inner
# @fb
# def A():
#     print("upload a photo")
# @fb
# def B():
#     print("comment")
# B()

# def f(func):
#     def inner(*args,**kwargs):
#         import time
#         start=time.time()
#         func(*args,**kwargs)
#         end=time.time()
#         print("the time dealy is ",start-end)
#     return inner
# @f
# def hh():
#     for i in range(1,100):
#         print(i)
# @f
# def j(a,b):
#     sum=a+b
#     print(sum)
# j(10,20)

# print([i for i in eval(input()) if type(i)==int])


# a=open(r'c:\Users\sanjay sp\Desktop\gnv.txt.txt','r')
# res=a.read()
# print(res)

# def div():
#     try:
#         a=int(input("value"))
#         b=int(input("enter the value"))
#         c=a/b
#         print(c)
#     except ZeroDivisionError:
#         print("value for b should ot be 0")
# div()

# sqr=lambda x: x**2
# print(sqr(4))

# rt=lambda y: y**3
# print(rt(5))


# ev_odd=lambda m: m%2==0
# print(ev_odd(5))

# tre=(lambda n: n**2 if n%2==0 else n**3)
# print(tre(4))

# prt=lambda string,str: str in string
# print(prt("hai","n"))

a=[1,2,3,4,5]
print(tuple(map(lambda x: x**2, a)))
