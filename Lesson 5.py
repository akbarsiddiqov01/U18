# # fruits = ["olma", "nok", "banan", "qulupnay", "mandarin"]
# # print(fruits)
# # print(f"Sizda {len(fruits)} xil meva bor")
# # print(fruits[0:1] )
# from dataclasses import replace
# from traceback import print_tb
#
# print("1-topshiriq")
# fruits = ["olma", "anor", "banan", "shaftoli"]
# print(fruits[1])
#
# print("2-topshiriq")
# numbers = [10, 20, 30, 40, 50]
# print(numbers[4])
#
# print("3-topshiriq")
# numbers = [5, 7, 9, 11]
# numbers[0]=100
# print(numbers)
#
# print("4-topshiriq")
# cars = ["BMW", "Audi", "Kia", "Toyota"]
# print(cars[3])
#
# print("5-topshiriq")
# nums = [1,2,3,4,5]
# print(nums[1]+nums[3])
#
# print("6-topshiriq")
# a=int(input("1-sonni kiriting: "))
# ab=int(input("2-sonni kiriting: "))
# ac=int(input("3-sonni kiriting: "))
# ad=int(input("4-sonni kiriting: "))
# ae=int(input("5-sonni kiriting: "))
# all=[a,ab,ac,ad,ae]
# print(all)
# print(all[2])
#
# print("7-topshiriq")
# name1=input("1-Ism kiriting: ")
# name2=input("2-Ism kiriting: ")
# name3=input("3-Ism kiriting: ")
# name4=input("4-Ism kiriting: ")
# names=[name1,name2,name3,name4]
# print(names)
# print(names[-1])
#
# print("8-topshiriq")
# numb1=int(input("1-sonni kiriting: "))
# numb2=int(input("2-sonni kiriting: "))
# numb3=int(input("3-sonni kiriting: "))
# numb4=int(input("4-sonni kiriting: "))
# numb5=int(input("5-sonni kiriting: "))
# numberss=[numb1,numb2,numb3,numb4,numb5]
# print(numberss)
# print(numberss[1]+numberss[4])
#
# print("9-topshiriq")
# fruit1=input('1-mevani kiriting: ')
# fruit2=input('2-mevani kiriting: ')
# fruit3=input('3-mevani kiriting: ')
# fruitss=[fruit1,fruit2,fruit3]
# print(fruitss)
# print(fruitss[2].upper())
#
# print("10-topshiriq")
# numbe1=int(input("1-sonni kiriting: "))
# numbe2=int(input("2-sonni kiriting: "))
# numbe3=int(input("3-sonni kiriting: "))
# numbe4=int(input("4-sonni kiriting: "))
# numbe5=int(input("5-sonni kiriting: "))
# numbe6=int(input("6-sonni kiriting: "))
# numbe1=0
# numbersss=[numbe1,numbe2,numbe3,numbe4,numbe5,numbe6]
# print(numbersss)
#
# print("11-topshiriq")
# vegetables=["sabzi","bodring","pamidor"]
# for i in vegetables:
#     print(i)
#
# print("12-topshiriq")
# numbeers = [3,5,7,9,11]
# for w in numbeers:
#     print(w*2)
#
# print("13-topshiriq")
# nuumbers = [3,5,7,9,11]
# ui=nuumbers[0]+nuumbers[1]+nuumbers[2]+nuumbers[3]+nuumbers[4]
# for q in nuumbers:
#     print(ui)
#
# print("16-topshiriq")
# number=[4,5,6,7,8,2,43,6]
# min_num = number[0]
# for i in number:
#     if min_num>i:
#         min_num=i
# print(min_num)

# print("21-topshiriq")
# number=[4,5,6,7,8,2,43,6]
# count=0
# for r in number:
#     if r%2==0:
#         count=count+r
# print(count)

# print("22-topshiriq")
# number=[4,5,6,7,8,2,43,6]
# for e in number:
#     e<=number[0]
# for g in number:
#     g>=number[0]

# number=[4,5,6,7,8,2,43,6]
# a=len(number)//2
# print(number[a])

    names=["Mirvayz", "Yaxyo", "Muzaffar", "Abduazim", "Furqat"]
    names.append("Fozil")
    print(names)
    a=names.pop(0)
    b=names.pop(0)
    newnames=[a,b]
    print(newnames)

