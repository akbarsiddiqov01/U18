# print("1-mashq")
# a=int(input("Yoshingizni kiriting: "))
# if a<=6:
#     print("Bog'cha")
# if a>=7 and a<=18:
#     print("Maktab")
# if a>=19 and a<=23:
#     print("Talaba")
# if a>=24:
#     print("Ishchi")
#
# print("2-mashq")
# b=int(input("Sonni kiriting: "))
# if b%2==0:
#     print("Juft son")
# if b%5==0:
#     print("5 ga bo'linadi")
# if b%10==0:
#     print("10 ga bo'linadi")
#
# print("3-mashq")
# login=input("Loginni kiriting: ")
# password=input("Parolni kiriting: ")
# if login=="admin":
#     if password=="1234":
#         print("Xush kelibsiz")
#     else:
#         print("Parol xato")
# else:
#     print("Login xato")
#
# print("1-topshiriq")
# power=int(input("Zaryadka nechi: "))
# if power>=20:
#     print("Ishlatish mumkin")
# else:
#     print("Quvvat kam")
#
# print("2-topshiriq")
# prize=int(input("Summani kiriting: "))
# if prize>=50000:
#     print("Kirish mumkin")
# else:
#     print("Mablag' yetarli emas")
#
# print("3-topshiriq")
# key=input("Parolni kiriting: ")
# if key=="12345":
#     print("Kirish tasdiqlandi")
# else:
#     print("Parol xato")
#
# print("4-topshiriq")
# money=int(input("To'lov miqdori(%): "))
# if money>=88 and money<=100:
#     print("Darsga kirish mumkin")
# else:
#     print("Kirish taqiqlanadi")
#
# print("5-topshiriq")
# age=int(input("Yoshingizni kiriting: "))
# job=input("Doimiy ish joyi bormi: ")
# salary=int(input("Oylik miqdori: "))
# black=input("Qora ro'yxatdamisiz: ")
# if age>=22:
#     if job=="bor":
#         if salary>=5000000:
#             if black=="yoq":
#                 print("Kredit tasdiqlandi")
#             else:
#                 print("Kredit rad etiladi")
#         else:
#             print("Kredit rad etiladi")
#     else:
#         print("Kredit rad etiladi")
# else:
#     print("Kredit rad etiladi")
#
# print("6-topshiriq")
# agee=int(input("Yoshingizni kiriting: "))
# health=input("Tibbiy ko'rikdan o'tganmi: ")
# test=int(input("Test natijasi: "))
# doping=input("Doping: ")
# if agee>=18:
#     if health=="ha":
#         if test>=70:
#             if doping=="aniqlanmagan":
#                 print("Sport musobaqasiga xush kelibsiz")
#             else:
#                 print("Ruxsat etilmaydi")
#         else:
#             print("Ruxsat etilmaydi")
#     else:
#         print("Ruxsat etilmaydi")
# else:
#     print("Ruxsat etilmaydi")
#
# print("7-topshiriq")
# prod=input("Mahsulot omborda mavjudmi: ")
# cheque=input("To'lov qilinganmi: ")
# address=input("Manzil kiritilganmi: ")
# delivery=input("Yetkazib berish xizmati: ")
# if prod=="ha":
#     if cheque=="ha":
#         if address=="ha":
#             if delivery=="faol":
#                 print("Buyurtma muvofaqiyatli yuborildi")
#             else:
#                 print("Buyurtma yuborilmadi")
#         else:
#             print("Buyurtma yuborilmadi")
#     else:
#         print("Buyurtma yuborilmadi")
# else:
#     print("Buyurtma yuborilmadi")
#
# print("8-topshiriq")
# email=input("Email kiriting: ")
# if "@" in email:
#     if email.endswith(".com"):
#         print("Email to'g'ri")
#     else:
#         print("Email noto'g'ri")
# else:
#     print("Email noto'g'ri")

# print("9-topshiriq")
# word=input("Username kiriting: ")
# if word.isalpha() and len(word)>=3 and word.islower():
#     print("Username to'g'ri")
# else:
#     print("Username xato")

print("10-topshiriq")
number=int(input("Raqamingizni kiriting: "))
if number.isdigit() and len(number)==9:
    print("Raqam qabul qilindi")
else:
    print("Raqam xato")