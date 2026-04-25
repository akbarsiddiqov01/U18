# print("1-topshiriq")
data=input("Ma'lumotlarni kiriting: ").split()
a=[]
b=[]
c=[]
for i in data:
    i=i.replace(',',' ')
    i=i.replace('"',' ')
    i=int(i)
    if i.isdigit():
        a.append(i)
    elif i.replace(".","").isdigit():
        c.append(i)
    else:
        b.append(i)
print(a)
print(b)
print(c)

# a=[]
# b=[]
# c=[]
# for i in datas:
#     i.replace(","," ")
#     i.replace('"',' ')
#     print(i)
# count=0
# for i in a:
#     if i>=0:
#         sum(i)
# print(a)
# print(b)
# print(c)

# print("2-topshiriq")
# d=[]
# while True:
#     numbers=input("Sonlarni kiriting: ")
#     for i in numbers:
#         d.append(i)
#     if numbers=="stop":
#         break
# print(d)
# just=0
# for w in d:
#     just=w+0
#     just>w
# print(just)

# print("3-topshiriq")
# new=[]
# info=input("Ma'lumotlarni kiriting: ").split()
# info=int(info)
# new.append(info)


# data = input("Ma'lumotlarni kiriting: ").split()
#
# tozalangan = []
#
# for i in data:
#     i = i.replace(',', '')
#     i = i.replace('"', '')
#     tozalangan.append(i)
#
# print(tozalangan)