# 1
# with open("test.txt","w") as file:
#     file.write("Hello")
#
# 2
# with open("test.txt","w") as file:
#     file.write("Hello")
# with open("test.txt","r") as file:
#     print(file.read())
#
# 3
# with open("test.txt","w") as file:
#     file.write("Salom")
# with open("test.txt","r") as file:
#     print(file.read())
#
# 4
# with open("test.txt","w") as file:
#     file.write("Hello")
# with open("test.txt","a") as file:
#     file.write("Python")
# with open("test.txt","r") as file:
#     print(file.read())
#
# 5
# with open("test.txt","w") as file:
#     file.write("Hello")
# with open("test.txt","r") as file:
#     a=file.read()
#     print(a)
#
# 7
# with open("test.txt","w") as file:
#     file.write("Line:Hello\n")
#     file.write("Line:world\n")
#     file.write("Line:guy\n")
# with open("test.txt","r") as file:
#     print(file.read())
#
# 6
# with open("test.txt","w") as file:
#     file.write("Hello\n")
#     file.write("world\n")
#     file.write("guy\n")
# with open("test.txt","r") as file:
#     print(file.read())
#
# 8
# with open("data.txt","w") as file:
#     file.write("lorem\n")
#     file.write("hello\n")
#     file.write("world\n")
# with open("data.txt","r") as file:
#     print(file.read())

# 9
# with open("data.txt","w") as file:
#     file.write("lorem\n")
#     file.write("hello\n")
#     file.write("world\n")
# with open("data.txt","r") as file:
#     a=file.readlines()
#     count=0
#     for i in a:
#         count+=1
#     print(count)

# 10
# with open("data.txt","w") as file:
#     file.write("lorem")
# with open("data.txt","r") as file:
#     a=file.read()
#     print(a.upper())
#
# 11
# with open("data.txt","w") as file:
#     file.write("Ananas ajoyib meva")
# with open("data.txt","r") as file:
#     a=file.read()
#     count=0
#     for i in a:
#         i=i.lower()
#         if i=="a":
#             count+=1
#     print(count)
#
#
12
with open("data.txt","w") as file:
    file.write("lorem\n")
    file.write("hello\n")
    file.write("world\n")
with open("data.txt","r") as file:
    a=file.read()
    count=0
    for i in a:
        if len(i)>=count:
            count=i
    print(count)
#
# 13
# with open("data.txt","w") as file:
#     file.write("Ananas ajoyib meva")
#     file.write("lorem")
#     file.write("Heloo")
# with open("data.txt","r") as file:
#     a=file.read()
#     print(a[::-1])
#
# 16
# import csv
# with open("data.csv","w",newline="") as file:
#     writer=csv.writer(file)
#     writer.writerow(['name','age'])
#     writer.writerow(['Ali','20'])
#     writer.writerow(['Vali','25'])
#
# 17
# import csv
# with open("data.csv","w",newline="") as file:
#     writer=csv.writer(file)
#     writer.writerow(['name','age'])
#     writer.writerow(['Ali','20'])
#     writer.writerow(['Vali','25'])
# with open("data.csv","r",newline="") as file:
#     print(file.read())

# 18
# import csv
# with open("data.csv","w",newline="") as file:
#     writer=csv.writer(file)
#     writer.writerow(['name','age'])
#     writer.writerow(['Ali','20'])
#     writer.writerow(['Vali','25'])
# with open("data.csv","r",newline="") as file:
#     a=csv.reader(file)
#     count=0
#     for i in a:
#         try:
#             i=int(i)
#             count+=i
#         except:
#             count+=0
#     print(count)

19
