# from abc import ABC, abstractmethod
# class Car(ABC):
#     def __init__(self,colour,motor,balance,probeg):
#         self.colour=colour
#         self.motor = motor
#         self._balance = balance
#         self.__probeg=probeg
#
#     def show_balance(self):
#         return f"Siz ${self._balance} lik moshina sotib olyapsiz"
#
#     @abstractmethod
#     def get_info(self):
#         return f"Mercedes rangi {self.colour}, motori {self.motor} ot kuchi, narxi {self._balance}"
#
# class Merc(Car):
#     def __init__(self,colour,motor,balance,probeg,seats=4):
#         super().__init__(colour,motor,balance,probeg)
#         self.seats=seats
#
#     def show_balance(self):
#         return f"Siz sotib olaotgan Merc ${self._balance} turadi"
#
#     def get_info(self):
#         return f"Mercedes rangi {self.colour}, motori {self.motor} ot kuchi, narxi {self._balance}, o'rindiqlari {self.seats}"
# # a=Car("Qora",670,50000,80000)
# # print(a.get_info())
# b=Merc("Qora",800,80000,200000,2)
# print(b.get_info())

a=input("Son kiriting: ")
while True:
    if a=="stop":
        break
    else:
        a=int(a)

