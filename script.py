province=input("Viloyat nomi: ")
district=input("Tuman nomi: ")
mahalla=input("Mahalla nomi: ")
street=input("Ko'cha nomi: ")
print(f"Siz {province} viloyati, {district} tumani, {mahalla} mahallasi, {street} ko'chasida yashaysiz")

print("1-topshiriq")
a=int(input("1-sonni kiriting: "))
b=int(input("2-sonni kiriting: "))
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

print("2-topshiriq")
s=int(input("Tug'ilgan yilingiz: "))
print(f"Siz {2026-s} yoshdasiz")

print("3-topshiriq")
g1=float(input("1-bahoyingiz: "))
g2=float(input("2-bahoyingiz: "))
g3=float(input("3-bahoyingiz: "))
print(f"Sizning o'rtacha bahoyingiz {(g1+g2+g3)/3}")

print("4-topshiriq")
ism = "Ali"
yosh = 20
print(f"Salom {ism}, Sizning yoshingiz {yosh}da")

print("5-topshiriq")
side=int(input("Tomon="))
print(f"Yuza={side*side}, Periment={side*4}")

print("6-topshiriq")
r=int(input("Radius:"))
L = 2 * 3.14 * r
S = 3.14 * r*r
print(f"L={L}, S={S}")

print("7-topshiriq")
e=int(input("Sonni kiriting: "))
ek=index(1)+index(2)+index(3)
print(f"Yig'indi={ek}")

print("9-topshiriq")
mon=int(input("Pul miqdori($): "))
print(f"Miqdor(sum)={mon*12300}")

print("10-topshiriq")
C=int(input("Kiriting(C): "))
F = C * 9/5 + 32
print(f"Natija: {F} °F")

print("11-topshiriq")
z=input("Son: ")
on = z[0]
bir = z[1]
print(f"O'nlik: {on}")
print(f"Birlik: {bir}")

print("12-topshiriq")
minute=int(input("Nechi daqiqa gaplashdingiz: "))
print(f"Sizdan {minute*500} so'm bo'ldi")

print("13-topshiriq")
n=int(input("Nechi kishi ketmoqda: "))
ne=n//15+1
print(f"{ne} ta avtobus keark")

print("14-topshiriq")
apple=int(input("Olma narxi: "))
banana=int(input("Banan narxi: "))
pie=int(input("Nok narxi: "))
all=(apple*2)+(banana*2)+(pie*2)
print(f"Jami: {all}")
