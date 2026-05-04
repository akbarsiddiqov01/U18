# 1
# try:
#     n = int(input("Sonni kiriting: "))
#     if n%2==0:
#         print(n**2)
#     else:
#         print(n**3)
# except ValueError:
#     print("Son kiriting")
#
# 2
# l=[1, "2", 3, "salom", 4.5]
# count=0
# for i in l:
#     if type(i)==int or type(i)==float:
#         count+=i
# print(count)
#
# 3
# a=input("Ma'lumot kiriting: ")
# strip=0
# num=0
# for i in a:
#     if i.isalpha():
#         strip += 1
#     elif i.isdigit():
#         num += 1
# print(f"Harflar {strip} va sonlar {num} ta")
#
4
a = []
while True:
    n=int(input("Son kiriting: "))
    if int(n)==0:
        break
    a.append(n)
print(sum(a)/len(a))

5
l=[1,3,2,5,7]
even = []
for i in l:
    if i%2==0:
        even.append(i)
if len(even)>0:
    print(even)
else:
    print("Topilmadi")
#
# 6
# def bolish(a,b):
#     try:
#         print(f"Bo'linma={a/b}")
#     except ZeroDivisionError:
#         print("0 ga bo‘lib bo‘lmaydi")
#
# bolish(10,0)
#
# 7
# data=input("Ma'lumot kiriting: ")
# letter=""
# for i in data:
#     if i==letter:
#         print("Repeat bor")
#     else:
#         letter=i
# 8
# l=[10, "10", 5.5, False, "hi", 20]
# la=[]
# for i in l:
#     la.append(type(i))
# print(la)
from traceback import print_tb

# 9
# for i in range(1,100):
#     if i%3==0 and i%5==0:
#         print("FizzBuzz")
#     elif i%3==0:
#         print("Fizz")
#     elif i%5==0:
#         print("Buzz")

# 10
# a=input("So'z kiriting: ")
# b=len(a)-1
# c=""
# while b>=0:
#     c+=a[b]
#     b-=1
# print(c)
# 11
# l=[23,54,765,25,76,24,678,1000,1]
# count=0
# for i in l:
#     if i>=count:
#         count=i
# print(count)
#
# 12
# a={"Akbar":25,
#    "Jaloliddin":26,
#    "Asqar":30,
#    "Yaxyo":11}
# for i in a.values():
#     if i%2==0:
#         print(i)

# 13
# word=input("So'z kiriting: ")
# for i in word:
#     if i=="a" or i=="o" or i=="u" or i=="e" or i=="a":
#         print(i)

# 14
# word=input("So'z kiriting: ")
# l=len(word)-1
# a=""
# for i in word:
#     a+=word[l].upper()
#     l-=1
# print(a)

# 15                                                       nc
# word=input("So'z kiriting: ")
# up=0
# low=0
# for i in word:
#     if i==i.upper():
#         up+=1
#     elif i==i.lower():
#         low+=1
# if up>0 and low>0:
#     print("Mixed")
# elif up>0:
#     print("UPPER")
# elif low>0:
#     print("lower")

# 16                                                            nc
# animals=["cat", "elephant", "dog", "tiger"]
# count=0
# for i in animals:
#     if len(i)>count:
#         count=len(i)
# for j in animals:
#     if count==len(j):
#         print(j)

# 17                                                        sdfvc
# try:
#     a=input("Matn kirit: ")
#     if len(a)==0:
#         print("xato")
# except:
#     print("Qabul qilindi")

# 18
# while True:
#     num = int(input("Musbat son kiriting: "))
#     if num>0:
#         print("Qabul qilindi")
#         break
#     print("Xato")

# 19
# a=[23,-54,-76,234,885,-3446,7,655,-3]
# plus=[]
# minus=[]
# for i in a:
#     if i>0:
#         plus.append(i)
#     else:
#         minus.append(i)
# print(f"Musbat sonlar{plus} | Manfiy sonlar {minus}")

# 20
# beo={"a":[1,2], "b":[3,4]}
# count=0
# for i in beo.values():
#     for j in i:
#         count+=j
# print(count)

# import time
# start=time.time()
# max(1,2,3,4,5,6,5,4)
# end=time.time()
# print(end-start)

# import time
# def timee(f):
#     def abc():
#         start = time.time()
#         time.sleep(1)
#         f()
#         end = time.time()
#         print(end-start-1)
#     return abc
# @timee
# def count():
#     print("Ish jarayonda")
#
# count()

# l=[1,2,3,4,5]
# print(0.1+0.2)
# with open("Akbar1.txt","r") as file:
#     print(file.readlines())