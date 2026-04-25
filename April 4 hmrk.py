# print("1-topshiriq")
# def total(*args):
#     all=0
#     for i in args:
#         all+=i
#     return all
#
# print(total(1,2,3,4,5,6,3))
#
# print("2-topshiriq")
# def total(*args):
#     all=0
#     for i in args:
#         if i>=all:
#             all=i
#     return all
#
# print(total(1,2,3,4,4,6,3))
#
# print("3-topshiriq")
# def total(*args):
#     all=0
#     a=len(args)
#     for i in args:
#         all+=i
#     mid=all/a
#     return mid
#
# print(total(1,2,3,4,5,6))
#
# print("4-topshiriq")
# def total(*args):
#     all=[]
#     for i in args:
#         if i%2==0:
#             all.append(i)
#     return all
#
# print(total(1,2,3,4,5,6,3))
#
# print("5-topshiriq")
# def total(*args):
#     all=[]
#     for i in args:
#         all.append(i)
#
#     for j in all:
#         b=1*j
#     return b
# print(total(1,2,3,4,5))
#
# print("6-topshiriq")
# def total(*args):
#     all=[]
#     for j in args:
#         all.append(j)
#     a=all[0]
#     for i in all:
#         if i<=a:
#             a=i
#     return a
#
# print(total(10,1,2,3,4,4,6,3))
#
# print("7-topshiriq")
# def total(*args):
#     all=[]
#     for i in args:
#         all.append(i)
#     a=len(all)
#     return a
#
# print(total(1,2,3,4,4,6,3))
#
# print("8-topshiriq")
# def total(*args):
#     all=[]
#     for i in args:
#         all.append(i)
#     newall=[]
#     for j in all:
#         a=j**2
#         newall.append(a)
#     return newall
# print(total(1,2,3,4,4,6,3))
#
# print("9-topshiriq")
# def long(*args):
#     all=[]
#     for i in args:
#         all.append(i)
#     count={}
#     for j in all:
#         count[len(j)]=j
#     big=max(count.keys())
#     a=count[big]
#     return a
#
# print(long("Akbar, Asqar, Mirvayz, Jaloliddin"))
#
# print("10-topshiriq")
# def total(*args):
#     all=0
#     minus=[]
#     for i in args:
#         if i<=all:
#             minus.append(i)
#     return minus
#
# print(total(1,2,3,4,-6,-8,4,6,-9,3))
#
# print("11-topshiriq")
# def datas(**kwargs):
#     for key,value in kwargs.items():
#         print(f"key={key}, value={value}")
# datas(ism="Akbar",age=18,id=456789)
#
# print("12-topshiriq")
# def datas(**kwargs):
#     for key,value in kwargs.items():
#         print(f" value={value}")
# datas(ism="Akbar",age=18,id=456789)
#
# print("13-topshiriq")
# def datas(**kwargs):
#     a=0
#     for i in kwargs.items():
#         a+=len(i)
#     return a/2
# print(datas(ism="Akbar",age=18,id=456789))
#
# print("14-topshiriq")
# def datas(**kwargs):
#     a=0
#     for key,value in kwargs.items():
#         a+=value
#     return a
# print(datas(anor=18000,gilos=20000,nok=13000))

# def unlimited_numbers(*args,**kwargs):
#     min_num=args[0]
#     for i in args:
#         if i<=min_num:
#             min_num=i
#     count=0
#     for j in kwargs.values():
#         if len(j)>=count:
#             max_word=j
#     return min_num, max_word
# print(unlimited_numbers(1,2,3,4,5,6,-7,10,name="Akbar",name2="Jaloliddin",name3="Ali"))

# def number_sort(*args,**kwargs):
#     for i in kwargs:
#         if kwargs.values()=="true":
#             for j in args:
#                 if j%2==0:
#                     print(j)
#         a=[]
#         elif kwargs .values()=="false":
#             for w in args:
#                 a.append(w)
#             for n in a:
#                 if n%2==0:
#                     del n
#             print(a)
#
# print(number_sort(1,2,3,4,5,6,7,even="true"))

# def number_sort(*args,**kwargs):
#     even=[]
#     not_even=[]
#     for i in args:
#         if i%2==0:
#             even.append(i)
#         else:
#             not_even.append(i)
#     a=list(kwargs.values())[0]
#     b=a.lower()
#     if b=="true":
#         return even
#     elif b=="false":
#         return not_even
#
# print(number_sort(1,2,3,4,5,6,7,even="true"))

def random(*args,**kwargs):
    a = list(kwargs.values())[0]
    low_a=a.lower()
    b= list(kwargs.values())[1]
    low_b=b.lower()
    upp=[]
    rev=[]
    if low_a==True:
        for i in args:
            w=i.upper()
            upp.append(w)
        print(upp)
    if low_b==True:
        for j in args:
            j.reverse()
            rev.append(j)
        print(rev)
random("hello","world",upper=True,reverse=True)

