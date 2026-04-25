# matn=input("Matn kiriting: ")
# count=0
# set1=set(matn)
# for i in set1:
#     for j in matn:
#         if i==j:
#             count+=1
#     print(f"{i} harfi {count} marta")
#     count=0

# u=input("Ma'lumot kirgizing: ")
# a=" "
# b=" "
# for i in range(len(u)-1):
#     a+=u[i]
# for j in a:
#     b+=j[::-1]
# print(b)

# def log(f):
#     print("Funksiya ishlamoqda...")
#     print(f*7)
#     print("Funksiya tugadi")
# def salom(num1,num2):
#     a=num1+num2
#     return a
# log(salom(2,8))







def log_decorator(a):
    def kichik():
        return a().lower()
    return kichik

@log_decorator
def soz():
    return "Hello world"

print(soz())















