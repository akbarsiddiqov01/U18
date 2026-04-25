while True:
    a=input("Sonni kiriting: ")
    if a=='stop':
        break
print("add    -> mahsulot qo‘shish")
print("show   -> mahsulotlarni ko‘rish")
print("buy    -> savatga qo‘shish")
print("card   -> kartaga pul tashash")
print("pay    -> sotib olish")
print("stop   -> chiqish")

def add(nom,narx):
    with open("Mahsulotlar.txt", "w") as file:
        file.write(f"{nom} --> {narx}")

# add("Kartoshka",4000)
def show():
    with open("Mahsulotlar.txt","r") as file:
        return file.read()
# print(show())
def buy(name):
    savat=[]
    with open("Mahsulotlar.txt","r") as file:
        for i in file:
            if i==name:
                savat.append(i)
    print(savat)
buy("Kartoshka")