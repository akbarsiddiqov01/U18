print("1-topshiriq")
words=input("Matn kiriting: ")
count={}
for i in words:
    count[i]=0
    for j in words:
        if i==j:
            count[i]+=1
max=0
word=""
for key,value in count.items():
    if value>=max:
        max=value
        word=key
print(f"Eng ko'pi {word} harfi {max} marta ishlatildi")

print("2-topshiriq")
l=[1,2,34,65,1,23,34,"salom","hayr", "salom"]
count={}
repeat=[]
for i in l:
    count[i]=0
    for j in l:
        if i==j:
            count[i]+=1
for key, value in count.items():
    if value>1:
        repeat.append(key)
print(repeat)