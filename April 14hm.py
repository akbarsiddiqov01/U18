# 1
# numbers=input("Sonlarni kiriting: ").strip(",")
# count=0
# a=[]
# for i in numbers:
#     if i.isdigit():
#         a.append(i)
# for j in a:
#     j=int(j)
#     count+=j
# print(count/len(a))
from operator import index
from re import search

# 2
# tuple=(1,2,3,4,5,6,7,8,9,10)
# print(f"Max={max(tuple)} : Min={min(tuple)}")

# 3
# grades={
#     3.5:"Tohir",
#     5:"Ali",
#     4:"Sherzod",
#     3:"Dilshod"
# }
# count=0
# for i in grades.keys():
#     if i>count:
#         count=i
# print(grades[count])

# 4
# text=input("Matn kiriting: ")
# count=0
# for i in text:
#     if i=="a" or i=="o" or i=="u" or i=="i" or i=="e":
#         count+=1
# print(count)

# 5
# set1={1,45,76,24,75,3,10}
# set2={1,665,4,3,23,10,75}
# same=set1.intersection(set2)
# print(same)

# 6
# for i in range(1,100):
#     if i%2==0:
#         print(i)

# 7
# num=int(input("Sonni kiriting: "))
# count=1
# for i in range(1,num+1):
#     count*=i
# print(count)

# 8
# a=[1,2,3,4,5,6,7,8,9]
# all=0
# i=0
# while i<len(a):
#     all+=a[i]
#     i+=1
# print(all)

# 9                                                               sd
# word=input("So'zni kiriting: ").split()
# a=""
# for i in word:
#     a+=i[::-1]
# print(a)

# 10
# for i in range(1,50):
#     if i%3==0:
#         print(i)

# 11
# number=int(input("Son kiritng: "))
# if number>0:
#     print("Musbat son")
# elif number<0:
#     print("Manfiy son")
# else:
#     print("Son 0 ga teng")

# 12
# grade=int(input("Balingizni kiritng: "))
# if grade>100:
#     print("Noto'g'ri")
# elif grade>=90:
#     print("A")
# elif grade>=80 and grade<=89:
#     print("B")
# elif grade>=70 and grade<=79:
#     print("C")
# elif grade>=60 and grade<=69:
#     print("D")
# else:
#     print("F")

# 13
# qwerty=[123,564,234]
# total=0
# for i in qwerty:
#     if i>total:
#         total=i
# print(total)

# 15
# login=input("Login: ")
# parol=input("Parol: ")
# if login=="Akbar":
#     if parol=="1234":
#         print("Xush kelibsiz")
#     else:
#         print("Parol xato")
# else:
#     print("Login xato")

# 16
# n=input("Sonlarni kiriting: ").strip(",")
# a=[]
# even=[]
# for i in n:
#     if i.isdigit():
#         a.append(i)
# for j in a:
#     j=int(j)
#     if j%2==0:
#         even.append(j)
# print(sum(even))

17
de