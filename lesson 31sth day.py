# dict_={"Olma": 50, "Banan": 20,"Nok": 100}
# try:
#     print(dict_["Anor"])
# except:
#     print("Xatolik yuz berdi")
from compression.zstd import zstd_version_info

number=input("Sonni kiriting: ")
try:
    number=int(number)
    c=20/number
    print(c)
except ValueError:
    print("Son kiritmadingiz")
except ZeroDivisionError:
    print("0 ga bolinmaydi")
finally:
    print("tizimda xatolik")