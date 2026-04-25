# print("1-topshiriq")
# num=input("Son kiriting: ")
# try:
#     num = int(num)
#     a = num / 10
#     print(a)
# except:
#     print("Son kiritmadingiz")
#
# print("2-topshiriq")
# number=input("Son kiriting: ")
# try:
#     number=int(number)
#     print(number)
# except:
#     print("Son kiritmadigingiz")
#
# print("3-topshiriq")
# datas=input("Ma'lumotlarni kiriting: ").split()
# ind=input("index ni kiriiting: ")
# try:
#     ind=int(ind)
#     print(datas[ind])
# except:
#     print("to'g'ti indeks kiriting")
#
# print("4-topshiriq")
# dic={
#     "names":"Dilshod",
#     "age":"43",
#     "status":"family"
# }
# print(dic)
# try:
#     value=input("Qiymatni so'rang: ")
#     print(dic[value])
# except:
#     print("Qiymat xato")
#
# print("5-topshiriq")
# num1=input("1-sonni kiriting: ")
# num2=input("2-sonni kiriting: ")
# try:
#     e = int(num1)
#     b = int(num2)
# except ValueError:
#     print("Sonni kiriting")
# try:
#     a=e/b
#     print(a)
# except ZeroDivisionError:
#     print("0 kiritmang")
from operator import index

print("1-mashq")
a=int(input("1-sonni kiriting: "))
b=int(input("2-sonni kiriting: "))
c=int(input("3-sonni kiriting: "))
all=(a+b+c)/3
print(all)

print("2-mashq")
info=input("Matn kiriting: ")
big=info.upper()
print(big)

print("3-mashq")
sent=input("Matn kiriting: ")
w=list(sent)
number=len(w)
for i in range(0,number,2):
    print(w[i])