# def qayta(matn):
#     print(matn[::-1])
# qayta("Salom")
#
# print("2-topshiriq")
# def between(n1,n2):
#     a=[]
#     for i in range(n1+1,n2):
#         a.append(i)
#     print(a)
# between(1,6)
#
# print("3-topshiriq")
# def new_even(list):
#     a=[]
#     for i in list:
#         if i%2==0:
#             a.append(i)
#     return a
# b=[1,2,3,4,5,6,7,8,9,10]
# print(new_even(b))
#
# print("4-topshiriq")
# def unli(harf):
#     count=0
#     for i in harf:
#         i=i.lower()
#         if i=="a" or i=="o" or i=="u" or i=="i" or i=="e":
#             count+=1
#     return count
# print(unli("Salom dUnyo"))
#
# print("5-topshiriq")
# def numbers(son):
#     count=0
#     for i in str(son):
#         count+=int(i)
#     return count
# print(numbers(3478))
from wsgiref.types import InputStream

# print("1-topshiriq")
# def qiymat(**kwargs):
#     count=0
#     for i in kwargs.values():
#         count+=1
#     return f"Kalitlar soni {count} ta"
# print(qiymat(ism="Akbar",age=18,id=456789))
#
# print("2-topshiriq")
# def qiymat(**kwargs):
#     count=0
#     for i in kwargs.values():
#         count+=i
#     return f"Mahsulotlar narxi jami {count} so'm"
# print(qiymat(olma=20000,nok=15000,anor=25000))
#
# print("3-topshiriq")
# def qiymat(**kwargs):
#     count=[]
#     string=[]
#     for i in kwargs.values():
#         if type(i)==int or type(i)==float:
#             count.append(i)
#     return count
# print(qiymat(olma=20000.01,nok="Olma",anor=25000))
#
# print("4-topshiriq")
# def juft(*args):
#     a=[]
#     for i in args:
#         if i%2==0:
#             a.append(i)
#     return a
# print(juft(1,2,3,4,5,6,7,8,9,10))
#
# print("5-topshiriq")
# def kopaytma(*args):
#     count=1
#     for i in args:
#         count*=i
#     return count
# print(kopaytma(2,4,6))

# 7
# print("1-topshiriq")
# def juft(*royxat):
#     even=[]
#     for i in royxat:
#         if i%2==0:
#             even.append(i)
#     ttl=0
#     for i in even:
#         ttl+=i
#     return f"Juft sonlar yig'indisi {ttl}"
# print(juft(1,2,3,4,5,6,7,8,9,10))
#
# print("2-topshiriq")
# def yigindi(*args,**kwargs):
#     plus=[]
#     for i in args:
#         if i>=0:
#             plus.append(i)
#     for j in kwargs.values():
#         if type(j)==int or type(j)==float:
#             plus.append(j)
#     total=0
#     for w in plus:
#         total+=w
#     return f"Umumiy yig'indi={total}"
# print(yigindi(12,4,7,-6,-3,a=7,b="Salom",c=4))
#
# print("3-topshiriq")
# def ball(**kwargs):
#     main=0
#     name=""
#     for i in kwargs.values():
#         if i>=main:
#             main=i
#     for key,values in kwargs.items():
#         if values==main:
#             name=key
#     return f"Eng yuqori ball {main}, egasi {name}"
# print(ball(Fozil=90,Komol=85,Jamshid=95))
#
# print("4-topshiriq")
# def bolish(number1,number2):
#     try:
#         print(f"Bo'linma={number1/number2}")
#     except TypeError:
#         print("Son kiriting")
#     except ZeroDivisionError:
#         print("0 ga bo'lib bo'lmaydi")
# bolish(10,"df")
# bolish(10,0)
# bolish(10,2)
#
# print("5-topshiriq")
# def indeks(lst,num):
#     try:
#         print(lst[num])
#     except IndexError:
#         print("Bunday index mavjud emas")
# a=[1,2,3,4,54,67,89]
# indeks(a,6)
# indeks(a,8)

# print("1-topshiriq")
# l=[1,2,3,4,5,6,7,8,9]
# count=0
# all=0
# while count<len(l):
#     all+=l[count]
#     count+=1
# print(f"Yigindi {all}")

# print("2-topshiriq")
# a=input("So'z kiriting: ")
# b=[]
# for i in a:
#     b.append(i)
# print(b)

# print("3-topshiriq")
# for i in range(3,50,3):
#     print(i)

# print("4-topshiriq")
# a=int(input("Son kiriting: "))
# if a>0:
#     print("Musbat son kiritingiz")
# elif a<0:
#     print("Manfiy son kiritingiz")
# else:
#     print("0 kiritdingiz")

# print("5-topshiriq")
# ball=int(input("Ballingizni kiriting: "))
# if ball>100:
#     print("Ball noto'g'ri")
# elif ball>=90:
#     print("A")
# elif ball>=80:
#     print("B")
# elif ball>=70:
#     print("C")
# elif ball>=60:
#     print("D")
# else:
#     print("F")

# inherit
# print("1-topshiriq")
# class Student:
#     def __init__(self,name,group):
#         self.name=name
#         self.group=group
#
#     def get_info(self):
#         return f"Salom {self.name}, siz {self.group}-guruhda o'qiysiz"
#
# a=Student("Akbar",4)
# print(a.get_info())
#
# print("2-topshiriq")
# class Car:
#     def __init__(self,year,brand):
#         self.year=year
#         self.brand=brand
#
#     def get_info(self):
#         return f"Siz olayotgan moshina {self.year}-yil va brendi {self.brand}"
#
# b=Car(2007,"Merc")
# print(b.get_info())
#
# print("3-topshiriq")
# class Book:
#     def __init__(self,title):
#         self.title=title
#
# c=Book("Jinoyat va Jazo")
# print(c.title)
#
# print("4-topshiriq")
# class BankAccount:
#     def __init__(self,card_name,balance):
#         self.card_name= card_name
#         self._balance=balance
#     def deposit(self,amount):
#         if amount>=1000:
#             self._balance += amount
#             print(f"Sizning hisobingizga {amount} so'm pul qo'shildi va sizning hisobingiz: {self._balance} so'm")
#
# card=BankAccount("Humo",5000)
# card.deposit(15000)
#
# print("5-toshiriq")
# class Animal:
#     def __init__(self,name,age):
#         self.name=name
#         self.age = age
#     def sound(self):
#         print(f"Bu yerda {self.age} yoshlik {self.name} degan hayvon bor")
#
# class Cat(Animal):
#     def sound(self):
#         print(f"{self.name} Miyovlab {self.age}ga kirganini aytmoqchi bo'ldi")
# class Dog(Cat):
#     def sound(self):
#         print(f"{self.name} Vovullab {self.age}ga kirganini aytmoqchi bo'ldi")
#
# a=Animal("Bobik",3)
# a.sound()
# b=Cat("Mosh",2)
# b.sound()
# c=Dog("Bobik",4)
# c.sound()

# print("1-topshiriq")
# try:
#     num=int(input("Son kiriting: "))
#     if num%2==0:
#         print(num**2)
#     else:
#         print(num**3)
# except ValueError:
#     print("Son kiritmadingiz")
#
# print("2-topshiriq")
# l=[1, "2", 3, "salom", 4.5]
# count=0
# for i in l:
#     if type(i)==int or type(i)==float:
#         count+=i
# print(count)
#
# print("3-topshiriq")
# number=0
# letter=0
# word=input("Matn kiriting: ")
# for i in word:
#     if i.isdigit():
#         number+=1
#     elif i.isalpha():
#         letter+=1
# print(f"Raqamlar={number}ta | Harflar={letter}ta")
#
print("1-topshiriq")
words=input("Matn kiriting: ")
count={}
for i in words:
    count[i]=0
    for j in words:
        if i==j:
            count[i]+=1
max=0
word=""
for key,value in count.items():
    if value>=max:
        max=value
        word=key
print(f"Eng ko'pi {word} harfi {max} marta ishlatildi")

print("2-topshiriq")
l=[1,2,34,65,1,23,34,"salom","hayr", "salom"]
count={}
repeat=[]
for i in l:
    count[i]=0
    for j in l:
        if i==j:
            count[i]+=1
for key, value in count.items():
    if value>1:
        repeat.append(key)
print(repeat)