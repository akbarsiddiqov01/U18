# a=input("1-sonni kiriting: ")
# b=input("2-sonni kiriting: ")
# if a>=b:
#     print(a)
#     print("1-son kattaroq")
# else:
#     print(b)
#     print("2-son kattaroq")

# q=int(input("Yoshingizni kiriting: "))
# if q<=7:
#     print("Bog'cha")
# elif q>=7 and q<=18:
#     print("Maktab")
# elif q>=19 and q<=23:
#     print("Talaba")
# elif q>=80:
#     print("Tirikligingizga qoyil")
# else:
#     print("Ishchi")

# s=int(input("Sonni kiriting: "))
# if s%2==0:
#     print("Juft son")
# if s%5==0:
#     print("5 ga bo'linadi")
# if s%10==0:
#     print("10 ga bo'linadi")

z=input("Loginni kiriting: ")
x=input("Parolni kiriting: ")
if z=="admin":
    if x=="1234":
        print("Xush kelibsiz")
    else:
        print("Parol noto'g'ri")
else:
    print("Bunday foydalanuvchi yo'q")