# print("1-topshiriq")
# a=input("Matn kiriting: ")
# b=input("So'zni kiriting: ")
# print(f"Uzunlik:{len(a)}")
# print(f"So'z indeksi:{a.find(b)}")
# print(f"Birinchi 5:{a[0:5]}")
# print(f"Oxirgi 5:{a[-5:]}")
# print(f"UPPER:{a.upper()}")
# print(f"lower:{a.lower()}")

# print("2-topshiriq")
# email=input("Emailni kiriting: ")
# aemail=email.find("@")
# if "@" in email and "." not in email[:aemail] and email.endswith(".com"):
#     print("Email to'g'ri")
# else:
#     print("Email noto'g'ri")

# print("3-topshiriq")
# count=0
# overall=0
# while True:
#     ball=input("Ballni kiriting: ")
#     if ball=="stop":
#         break
#     else:
#         score=int(ball)
#         overall+=score
#         count+=1
# total=overall/count
# print(f"Ballar soni: {count}")
# print(f"O'rtacha: {total}")
# if total>=90:
#     print("Ntaija: A'lo")
# elif total>=70 and total<=89:
#     print("Ntaija: Yaxshi")
# elif total>=50 and total<=69:
#     print("Ntaija: Qoniqarli")
# else:
#     print("Ntaija: Qoniqarsiz")

# print("4-topshiriq")
# total = 0
# all = 0
# count = 0
# while True:
#     n=int(input("N sonini kiriting: "))
#     if n>0:
#         break
# for i in range(1,n+1):
#     total+=i
#     all += i ** 2
#     if i%2==0:
#                 count+=1
# print(f"Yig'indi: {total}")
# print(f"Kvadratlar yig'indisi: {all}")
# print(f"Juft sonlar soni:{count}")

# print("5-topshiriq")
# fruit=list(input("Mevalarni kiriting: ").split())
# costs= {}
# narx=input("Narxlarini kiriitng: ").split()
# for j in narx:
#     a = j.find(":")
#     keys=j[:a]
#     values=j[a+1:]
#     costs[keys]=values
# search=input("Qidirilgan meva: ")
# new=input("Yangi meva: ")
# fruits=[]
# for i in fruit:
#     i=i.replace(",","")
#     fruits.append(i)
# fruits.append(new)
# print(f"Mevalar soni: {len(fruits)}")
# print(f"Birinchi meva: {fruits[0]}")
# print(f"Oxirgi meva: {fruits[-1]}")
# print(f"Birinchi 3 ta meva: {fruits[0:3]}")
# long=[]
# for j in fruits:
#     if len(j)>4:
#         long.append(j)
# print(f"Uzun nomli mevalar: {long}")
# x = costs.get(search)
# if x is not None:
#     print(f"Qidirilgan meva narxi: {x}")
# else:
#     print("Topilmadi")
# print("Narxlar:")
# for u,i in costs.items():
#     print(f"{u} -> {i}")


# olma, anor, banan, shaftoli
# olma:12000, anor:18000, banan:22000, shaftoli:25000

print("1-mashq")
def back(word):
    print(word[::-1])

back("hello my fellas")

print("2-mashq")
def mid(number1,number2):
    