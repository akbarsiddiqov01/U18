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

# 4
# a = []
# while True:
#     n=int(input("Son kiriting: "))
#     if int(n)==0:
#         break
#     a.append(n)
# print(sum(a)/len(a))

# 5
# l=[1,3,5,7]
# try:
#     even = []
#     for i in l:
#         if i%2==0:
#             even.append(i)
#     if even[0].isdigit():
#         print(even)
# except IndexError:
#     print("Topilmadi")

# 6
# def bolish(a,b):
#     try:
#         print(f"Bo'linma={a/b}")
#     except ZeroDivisionError:
#         print("0 ga bo‘lib bo‘lmaydi")
#
# bolish(10,0)

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

# 9
# for i in range(1,100):
#     if i%3==0 and i%5==0:
#         print("FizzBuzz")
#     elif i%3==0:
#         print("Fizz")
#     elif i%:5==0:
#         print
