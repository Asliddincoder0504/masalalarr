#WHILE  SIKLI BOYICHA  UYGA VAZIFA
# 1. Svetafor: Foydalanuvchidan inputda svetavor qaysi rangda deb so’rang. qizil,
# sariq yoki yashil deb yozmoagunicha, bu xato rang deb qayta so’rayvering. Agar shu
# ranglardan birini tanlasa “rahmat, to’g’ri keladi” degan print chiqazing.
# from Tools.scripts.make_ctype import values
# from scipy.constants import value
# from scipy.stats import yulesimon

# while True:
#     rang1=input("Rang  kiriting: ")
#     if rang1!="qizil" and rang1!="yashil" and rang1!="sariq":
#         print("bu xato rang")
#     else:
#         print("Bu rang  to'g'ri")
#         break

#2-MASALA
# Tasodifiy Sonni Topish O'yini: Kompyuter 1 dan 10 gacha bo'lgan tasodifiy son
# o'ylaydi. Foydalanuvchidan ushbu sonni topishni so'rang. Foydalanuvchi to'g'ri sonni
# topguncha davom etadi. Har bir noto'g'ri urinishdan so'ng, "Noto'g'ri, qayta urinib
# ko'ring" deb chiqaring. To'g'ri topilganda, "Tabriklaymiz, siz topdingiz!" deb chiqaring.
# Ko'rsatma: random. dan foydalanib tasodifiy son yarating va while sikli yordamida
# foydalanuvchi kiritmalarini tekshiring

# import random
# son=random.randint(1,10)
# while True:
#
#     a=int(input("Kompyuter o'ylagan  sonni toping: "))
#     if a==son:
#         print("Bu son to'g'ri")
#         break
#     else:
#         print("bu son xato")

#3-MASALA
#. Do'stlar Ro'yxatini Yaratish:
# ● Vazifa: Foydalanuvchidan do'stlarining ismlarini kiritishni so'rang.
# Foydalanuvchi "stop" deb yozmaguncha, yangi ismlar qo'shilaveradi. Oxirida
# barcha do'stlarining ismlari ro'yxatini chiqaring.
# ● Ko'rsatma: While sikli va list metodlaridan foydalanib, ro'yxatni shakllantiring.


# list = []
# while True:
#     friends = input("Do'stlaringiz ismini kiriting  yoki stop deb to'xtating: ")
#     if friends.lower()=="stop":
#         print("Stop")
#         break
#     else:
#
#         list.append(friends)
#         print("Sizning  do'stlaringiz=",list)


#4-MASALA
# Valyuta Ayirboshlash Kalkulyatori: Foydalanuvchiga valyuta ayirboshlash
# imkoniyatini bering. U so'mni dollarga almashtirishi mumkin. Valyuta kurslarini
# oldindan belgilang (masalan, 1 USD = 12,600 so'm). Foydalanuvchi summani
# kiritadi, dastur esa hisob-kitobni chiqaradi. Foydalanuvchi "exit" deb yozmaguncha
# dastur davom etadi.exit deb yozsa dastur to’xtaydi.


# USD=12800
# EURO=13700
# RUBL=130
# valyuta=input("Valyuta kiriting: Almashtirish mumkin bo'lgan valyutalar=USD,EURO,RUBL==")
# while True:
#
#     if valyuta=="exit":
#         print("Dastur to'xtadi")
#         break
#     elif valyuta=="EURO":
#         summa=int(input("Summa kiriting="))
#         print(f" bu summa {summa/EURO}   Yevroni tashkil  qiladi: ")
#     elif valyuta=="USD":
#         summa=int(input("Summa kiriting="))
#         print(f"bu summa {summa/USD}  Dollarni tashkil qiladi")
#     elif valyuta=="RUBL":
#         summa=int(input("Summa  kiriting="))
#         print(f"bu summa {summa/RUBL} Rublni  tashkil  qiladi")


#2-$$$$$TOPSHIRIQ$$$$$

#1-MASALA..1. While siklidan foydalanib print qiling:
# 1
# 22
# 333
# 4444
# 55555

# n=1
# while n<=8:
#     print(str(n)*n)
#     n+=1


#2-MASALA..2. While dan foydalanib sondagi raqamlar yig'indisini topadigan dastur tuzing.
# input: 555   output: 15
# input: 8125   output: 16

# son=int(input("Son kiriting=="))
# yigindi=0
# while son>0:
#     raqam=son%10
#     yigindi+=raqam
#     son//=10
# print("Raqamlar yig'indi",yigindi)


#3-MASALA.. While orqali 1 dan 100 gacha bo'lgan toq solar yig'indisini topuvchi dastur tuzing
# son=1
# yigindi=0
#
# while son<=100:
#     if son%2!=0:
#         yigindi+=son
#     son+=1
# print(yigindi)


#4-MASALA..Taxmin qilish o'yinini simulyatsiya qiladigan dastur yarating.
# Dastur 1 dan 100 gacha bo'lgan tasodifiy sonni yaratishi va
# foydalanuvchidan raqamni taxmin qilishni so'rashi kerak.
# Agar foydalanuvchi taxmini haqiqiy raqamdan yuqori bo'lsa, dastur "Juda baland!" va
# foydalanuvchidan yana taxmin qilishni so'rang. Xuddi shunday, agar foydalanuvchining
# taxmini haqiqiy raqamdan past bo'lsa, dastur "Juda past!" va foydalanuvchidan yana taxmin
# qilishni so'rang. Dastur foydalanuvchidan to'g'ri raqamni topmaguncha taxmin qilishni so'rashi kerak.

#
# import random
# son=random.randint(1,1)
#
# while True:
#     tahmin = int(input("Son kiriting: "))
#     if tahmin<son:
#         print('Son kichik:Qayta urining')
#
#     elif tahmin>son:
#         print('Son kichik:Qayta urining')
#     else:
#         print("To'g'ri topdingiz")
#         break

# class Transport:
#     def __init__(self, brand, model, type):
#         self.brand = brand
#         self.model = model
#         self.type = type
#
#     def info(self):
#         print(f"Brand: {self.brand}, Model: {self.model}, Type: {self.type}")
#
#
# class ElectroCars(Transport):
#     def __init__(self, brand, model, type, battery_life, charging_time):
#         super().__init__(brand, model, type)
#         self.battery_life = battery_life
#         self.charging_time = charging_time
#
#     def more_info(self):
#         print(f"Brand: {self.brand}, Model: {self.model}, Type: {self.type}, "
#               f"Battery Life: {self.battery_life}, Charging Time: {self.charging_time}")
#
#
# class SportCars(Transport):
#     def __init__(self, brand, model, type, motor, color):
#         super().__init__(brand, model, type)
#         self.motor = motor
#         self.color = color
#
#     def more_info(self):
#         print(f"Brand: {self.brand}, Model: {self.model}, Type: {self.type}, "
#               f"Motor: {self.motor}, Color: {self.color}")
#
#
# class Truck(Transport):
#     def __init__(self, brand, model, type, motor, height, length, weight):
#         super().__init__(brand, model, type)
#         self.motor = motor
#         self.height = height
#         self.length = length
#         self.weight = weight
#
#     def more_info(self):
#         print(f"Brand: {self.brand}, Model: {self.model}, Type: {self.type}, "
#               f"Motor: {self.motor}, Height: {self.height}, Length: {self.length}, Weight: {self.weight}")
#
# ecar = ElectroCars("Tesla", "Model S", "Electric", "100 kWh", "1 hour")
# sc = SportCars("Ferrari", "488", "Sport", "V8", "Red")
# truck = Truck("Volvo", "FH16", "Truck", "D16", "4 meters", "7 meters", "25 tons")
#
# ecar.more_info()
# sc.more_info()
# truck.more_info()


#
# def big_sales(sales):
#     return max(sales,key=sales.get)
#
# print(big_sales({
#         "yanvar": 12000,
#         "fevral": 10000,
#         "mart": 8000,
#         "dekabr": 18000,
# }))
def tub_sonlar(a, b):
    tub_sonlar = []
    for son in range(a, b):
        if son < 2:
            continue
        k = 0
        for i in range(2, int(son**0.5) + 1):
            if son % i == 0:
                k += 1
                break
        if k == 0:
            tub_sonlar.append(son)
    return tub_sonlar

def teskari_modul(a, b):
    """Evklid algoritmi yordamida a sonining b moduli teskari qiymatini hisoblash"""
    x_2, x_1 = 1, 0
    y_2, y_1 = 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x_2, x_1 = x_1, x_2 - q * x_1
        y_2, y_1 = y_1, y_2 - q * y_1
    if a != 1:
        return None  # Teskari modul mavjud emas
    return x_2 % b  # Teskari modul

def shifr(p, q, e):
    n = p * q
    f_n = (p - 1) * (q - 1)
    d = teskari_modul(e, f_n)  # d ni hisoblash uchun teskari modul
    if d is None:
        return None, None, None
    return n, e, d


p = int(input("p = "))
q = int(input("q = "))
e = int(input("e = "))

n, e, d = shifr(p, q, e)
if n is None:
    print("Xatolik: Teskari modul mavjud emas.")
else:
    M = 87
    C = pow(M, e, n)
    M_ = pow(C, d, n)
    print(f"Shifrlangan xabar (C): {C}")
    print(f"Deshifrlangan xabar (M): {M_}")

N = 1024
print("Tub sonlar 2 va 1024 oralig'ida:", tub_sonlar(2, N))




