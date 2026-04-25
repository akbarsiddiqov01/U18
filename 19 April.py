# class Animal:
#     def __init__(self,name,age):
#         self.name=name
#         self.age = age
#     def sound(self):
#         print("Animallar ovozi")
#
# class Cat(Animal):
#     def sound(self):
#         print(f"{self.name} Miyovlab {self.age}ga kirganini aytmoqchi bo'ldi")
# class Dog(Animal):
#     def sound(self):
#         print(f"{self.name} Vovullab {self.age}ga kirganini aytmoqchi bo'ldi")
#
# a=Cat("Mosh",2)
# a.sound()
# b=Dog("Bobik",4)
# b.sound()

class Bank:
    def __init__(self,card_name,balance):
        self.card_name= card_name
        self._balance=balance
    def show(self):
        print(f"Siz {self.card_name} kartasini ishlatasiz va sizning balansingiz: {self._balance}")
    def deposit(self,amount):
        if amount>=1000:
            self._balance += amount
            print(f"Sizning hisobingizga {amount} so'm pul qo'shildi va sizning hisobingiz: {self._balance}")
    def withdraw(self,amount):
        if amount<=self._balance:
            a=self._balance-amount
            print(f"Sizning hisobingizdan {amount} so'm pul ayrildi va sizning hisobingiz: {a}")
class Credit_account(Bank):
    def __init__(self, card_name, balance, credit_summa=0):
        super().__init__(card_name, balance)
        self.credit_summa = credit_summa
    def deposit(self,amount):
        self._balance+=amount
        print(f"Siz {amount} miqdorda kredit oldingiz va sizning hisobingiz: {self._balance} so'm")
        self.credit_summa+=amount
        print(f"Sizning kredit summangiz {self.credit_summa} so'm")

    def withdraw(self,amount):
        if amount>=10000 and self._balance>=amount:
            self.credit_summa-=amount
            print(f"Tabriklaymiz siz kreditingizni {amount} so'mga kamaytirdingiz va sizda: {self.credit_sum} so'm kreditngzi qoldi")


a=Bank("Humo",5000)
a.show()
# a.deposit(3000)
# a.withdraw(2000)
# b=Credit_account("Humo",300000)
# b.deposit(35000)
