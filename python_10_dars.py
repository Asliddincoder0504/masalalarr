# qiziqishingiz=input("Qiziqqan  sohangiz:  ")
# if qiziqishingiz.find("kitob")>-1 or qiziqishingiz.find("kutubxona")>-1:
#     kitob=input("Qaysi janrdagi kitobga qiziqasz")
#     if qiziqishingiz.find("detiktiv")>-1:
#         print("Shaytanat  kitobi haqida  xulosangizni aytib  bering ")
#     elif qiziqishingiz.find("diniy")>-1:
#         print("Hadis va Hayot  kitobi sovg'a qilamiz sizga")
# elif qiziqishingiz.find("sport")>-1:
#     sport_turi=input("Qaysi sport turiga qiziqasz")
#     # print("Qaysi  sport turiga qiziqasz")
#     if qiziqishingiz.find("futbol")>-1:
#         komanda=input("Qaysi komandaga muxlislik qilasz")
#         # print("Qaysi  komandaga muxlislik qilasz")
#         if qiziqishingiz.find("Real")>-1 or qiziqishingiz.find("Barsa")>-1:
#             print("El Classikoga chipta beramiz sizga")
#from numpy.ma.core import append
#from scipy.stats import kolmogn

# qiziqishingiz = input("Qiziqqan sohangiz: ")
#
# if qiziqishingiz.find("kitob") > -1 or qiziqishingiz.find("kutubxona") > -1:
#     kitob = input("Qaysi janrdagi kitobga qiziqasiz: ")
#     if kitob.find("detektiv") > -1:
#         print("Shaytanat kitobi haqida xulosangizni aytib bering.")
#     elif kitob.find("diniy") > -1:
#         print("Hadis va Hayot kitobiga ega bo'ldingiz")
# elif qiziqishingiz.find("sport") > -1:
#     sport_turi = input("Qaysi sport turiga qiziqasiz: ")
#     if sport_turi.find("futbol") > -1:
#         komanda = input("Qaysi komandaga muxlislik qilasiz: ")
#         if komanda.find("Real") > -1 or komanda.find("Barsa") > -1:
#             print("El Classikoga chipta yutib oldingiz")



#1-MASALA..Elektron Pochta Manzillarini Tekshirish:

# pochtalar = ["user1@gmail.com", "user2yahoo.com", "user3@outlook.com","asliddin@123"]
# for i in pochtalar:
#     if "@" not in  i or "." not in i:
#         print("Noto'g'ri  email manzili")
#     else:
#         print("Email manzilingiz to'g'ri")



#2-MASALA.. Parol Kuchini Tekshirish
# parollar=["password123", "Qwerty!", "admin", "StrongPass1!"]
# belgilar=".,;!?@#$%^&*()"
# for i in parollar:
#     if len(i)<8:
#         print("Juda qisqa parol")
#     elif i.isnumeric()==False and i.isascii()==False:
#         print("Kuchsiz parol")
#     else:
#         print("Kuchli parol")



#3-MASALA.. Ob-havo Ma'lumotlarini Tahlil Qilish:
# ob_havo=[20,22, 19, 24, 25, 23, 21,31,34,45]
#
# a = sum(ob_havo) / len(ob_havo)
# print(a)
# for i in ob_havo:
#
#     if i>=22:
#         print("Iliq")
#     else:
#         print("Salqin")


#4-MASALA... Restoran Buyurtmalari:
# taomlar= ["Osh", "Shashlik", "Manti","Lag'mon"]
#
# buyurtma=input("Qaysi taomni  yemoqchisz: ")
#
# taom=False
# for buyurtma in taomlar:
#     if buyurtma==taom:
#         taom=True
#         break
# if taom:
#     print("Buyurtmangiz qabul qilindi")
# else:
#     print("Taom  menuda mavjud emas")


#5-MASALA.. Anketa Tahlili.
# yoshlar=[16, 21, 17,30, 25]
# for yosh in yoshlar:
#     if yosh<18:
#         print(f" Sizning yoshingiz {yosh} da Yosh chegarasiga yetmagansiz")
#     else:
#         print(f" Sizning yoshingiz {yosh}da Xush kelibsz")



#6-MASALA..Mobil Ilova Bildirishnomalari:
# xabarlar=["Yangi xabar", "Batareya past", "Yangilanish mavjud","Javobsiz qomg'iroq"]
# for xabar in xabarlar:
#     if xabar==xabarlar[1]:
#         print("Qurilmangizni zaryadlash qurilmasiga ulang")
#         break


#7-MASALA.. Fayllarni guruhlash:
# fayllar = ["kitob.jpg", "kok_jiguli.mp3", "tabiat.jpg", "malohat.mp3", "iphone16.jpg"]
# musiqalar=[]
# rasmlar=[]
# for i in fayllar:
#     if i.find(".mp3")!=-1:
#         musiqalar.append(i)
#
#     elif i.find(".jpg")!=-1:
#         rasmlar.append(i)
# print("Musiqalar",musiqalar)
# print("Rasmlar",rasmlar)






