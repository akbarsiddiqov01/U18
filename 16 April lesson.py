# with open("Akbar .txt","w") as file0:
#     file0.write("Akbar diplomatiyada o'qiydi")
# with open("Akbar1.txt","a") as file:
#     file.write("Akbar diplomatiyada o'qiydi")
# with open("Akbar.txt","r") as file1:
#     print(file1.read())

# import csv
# with open("Study.csv","w",newline="") as file:
#     writer=csv.writer(file)
#     writer.writerow(["name","age","id"])
#     writer.writerow(["Gulyuz", "21", "1"])
#     writer.writerow(["Yaxyo", "19", "2"])
#     writer.writerow(["Sardor", "20", "3"])

with open("nothing.txt","w") as file:
    file.write("Ananas ajoyib meva")
with open("nothing.txt","r") as file:34
    a=file.read()
count=0
for i in a:
    if i=="a":
        count+=1
print(count)
print(a[::-1])

