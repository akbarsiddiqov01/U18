# print("1-topshiriq")
# data=input("Ma'lumotlar kiriting: ").split()
# a=[]
# for i in data:
#     i=i.replace('"',"")
#     i=i.replace(',','')
#     a.append(i)
#
# b=[]
# c=[]
# d=[]
# for j in a:
#     if "." in j:
#         c.append(j)
#     else:
#         try:
#             num=int(j)
#             b.append(j)
#         except:
#             d.append(j)
# summa=[]
# for w in b:
#     w=int(w)
#     if w>=0:
#         summa.append(w)
# print(b)
# print(c)
# print(d)
# print(sum(summa))

# print("2-topshiriq")
# n=[]
# while True:
#     num=input("Sonlarni kiriting: ")
#     if num=="stop":
#         break
#     number = int(num)
#     n.append(number)
# # print(n)
# max=max(n)
# min=min(n)
# print(f"max={max}")
# print(f"min={min}")
# print(f"Jami={sum(n)-max-min}")

print("3-topshiriq")
numbers=input("Sonlarni kiriting: ").split()
a=[]
for i in numbers:
    i=i.replace(","," ")
    i = int(i)
    a.append(i)
b=set(a)
# print(b)
even=[]
ten=[]
for j in b:
    if j%2==0:
        even.append(j)
    elif j>10:
        ten.append(j)
print(sum(even))
print(sum(ten))








# list=[]
# list.append(numbers)
# b=set(numbers)
# a=[]
# for i in b:
#     i=i.replace(","," ")
#     for j in b:
#         if j==i:
#             a.append(i)
# print(a)
