#FUNKSIYA  MAVZUSI   MASALALARI
#
from mpmath import ln, cot

#1-MASALA.."user_data" funksiyasini elon qilasizlar.
# Funksiyani 3 ta parametri bor (first_name, last_name, age).
# Input orqalik ism, familiya va yoshni kiritamiz.
# va bu bu qiymatlarni "user_data" funksiyasini chaqirib argumentlariga beramiz.
# "user_data" funksiyasi bu (first_name, last_name, age) o'zgaruvchilarni qiymatini


# def user_data(first_name,last_name,age):
#
#     print(f"Ism: {first_name}")
#     print(f"Familya: {last_name}")
#     print(f"Yosh: {age}")
# first_name=input("Ism: ")
# last_name=input("Familya: ")
# age=int(input("Yosh: "))
# user_data(first_name,last_name,age)



#2-MASALA.. "find_max" funksiyasini elon qilasizlar.
# Funksiyani 3 ta parametri bor (a, b, c).
# Input orqalik 3 ta son kiritamiz.
# va bu sonlarni "find_max" funksiyasi chaqirib argumentlariga beramiz.
# "find_max" funksiyasini bu (a, b, c) o'zgaruvchilardan eng kattasini
# topib print qiladi.



#   Eng katta son - A = 10
#   yoki
#   Eng katta son - A va B = 10
#   yoki
#   Eng katta son - A va B va C = 10
2
# def find_max(a,b,c):
#     max_value=max(a,b,c)
#
#     if a==b and b==c and a==c:
#         print("A-B va C  eng katta son")
#     elif a==max_value and b==max_value:
#         print("A va B sonlar eng katta sonlar")
#     elif a==max_value and c==max_value:
#         print("A va C sonlar eng katta sonlar")
#     elif b==max_value and c==max_value:
#         print("B va C sonlar eng katta sonlar")
#     elif a==max_value:
#         print("A soni eng katta son")
#     elif b==max_value:
#         print("B soni eng katta son")
#     elif c==max_value:
#         print("C soni eng katta son")
#
# a = int(input("a="))
# b = int(input("b="))
# c = int(input("c="))
#
# find_max(a, b, c)

#3-MASALA.."find_letter_count" funksiyasini elon qilasizlar.
# Funksiyani 2 ta parametri bor (word, letter).
# Input orqalik so'z kiritamiz, keyin esa shu so'zda qidirmoqchi bolgan so'zimizni kiritamiz.
# va bu qiymatlarni "find_letter_count" funksiyasini chaqirib argumentlariga beramiz.
# "find_letter_count" funksiyasi bu (word, letter) o'garuvchilardan foydalanib
# "word" da "letter" nechi martda qatnashganini print qilsin.
#
#   "Programing" so'zida "r" dan 2 ta.

# def find_letter_count(word,letter):
#      return word.count(letter)
# natija=find_letter_count("wordwordwordd","d")
# print(natija)


#4-MASALA.."list_sum" funksiyasi elon qilasizlar.
# Funksiyani 1 ta pametrni bor (myList).
# "myList" funksiyasini chaqirib unda argumentini berasizlar.
# uni ichida esa myList elementlarini yig'indisini print qilasizlar.
#
#   Listning elementlar yig'indisi = 32



# def list_sum(myList):
#     umumiy=sum(myList)
#     print(f"Ro'yxat  elementlari yig'indisi: {umumiy}")
# myList=[12,34,56,67]
# list_sum(myList)


#5-MASALA.. daraja(a, b) - bu funksiya a ni b darajasini print qilsin.
# def daraja(a,b):
#
#     natija=a**b   # a  ning  b  chi  darajasini  hisoblayabdi
#     print(f"a ning b darajasi: {natija}")  # a ning b darajasini  printga chiqaryabdi
#
# a=int(input("a="))  # a sonini kiritishni  so'rayabdi
# b=int(input("b="))    # b sonini kiritishni  so'rayabdi
#
# daraja(a,b)


#6-MASALA..daraja4(a, b, c, d) - bu funksiya a ni b, c va d chi darajasini print qilsin.
# def daraja4(a,b,c,d):
#      natija=a**b
#      print(f"a ning  b  darajasi: {natija}")
#      natija=a**c
#      print(f"a ning  c  darajasi: {natija}")
#      natija = a ** d
#      print(f"a ning  d  darajasi: {natija}")
#
#
#
# a=int(input("a="))
# b=int(input("b="))
# c=int(input("c="))
# d=int(input("d="))
#
# daraja4(a, b, c, d)



#7-MASALA..digit_count_and_sum(word) - bu funksiya "word" ni ichidagi raqamni aniqlab ularni yig'indisini va nechtaligini print qilsin.

# def digit_count_and_sum(word):
#     digit_sum=0
#     digit_count=0
#     for char in word:
#         if char.isdigit():
#             digit_sum+=int(char)
#             digit_count+=1
#     print(f"Raqamlar yig'indisi:  {digit_sum} ")
#     print(f"Raqamlar soni:  {digit_count} ")
# word=input("Matn kiriting: ")
# digit_count_and_sum(word)



#8-MASALA..add_right(a, b) - bu funksiya a sonini o'ng tomoniga b sonini birlashtirib qoysin va print qilsin.

# def add_right(a,b):
#     s=int(str(a)+str(b))
#     print(s)
# a=1234
# b=5664
# add_right(a,b)


#9-MASALA..add_left(a, b) - bu funksiya a sonini chap tomoniga b sonini birlashtirib qoysin va print qilsin.
# def add_left(a,b):
#     p=int(str(b)+str(a))
#     print(p)
# a=34
# b=54
# add_left(a,b)


#10-MASALA..work_with_list(a) - bu funksiya a listdan eng kichik sonni topib list elementlariga ko'paytirib qiymatini o'zgartiradi va listni print qilsin.
# def work_with_list(a):
#     min_value=min(a)
#     a=[x*min_value for x in a]
#     print(a)
# a=[23,56,87,32,90]
# work_with_list(a)


#11-MASALA...big_sales(sales) funksiyasini yarating.
# sales bu dictionary:
# {
#   "yanvar": 12000,
#   "mart": 6000,
#   "aprel": 15000,
#   "sentabr": 9000,
#   "dekabr": 10000,
# }
#
# qaysi oyda eng ko'p sotuv bolgan bo'lganini return qilsin.

# def big_sales(sales):
#     return max(sales,key=sales.get)
# print(big_sales({
#         "yanvar": 12000,
#         "fevral": 10000,
#         "mart": 8000,
#         "dekabr": 18000,
# }))


#12-MASALA..min_max(numbers, max_num, min_num) max_num numbers ichigagi eng katta sonmi yoki yoqmi shuni aniqlang,
# min_num numbers ichigagi eng kichik sonmi yoki yoqmi shuni aniqlang

# def min_max(numbers,max_num,min_num):
#     maksimal_son=max(numbers)
#     minimal_son=min(numbers)
#
#     if maksimal_son==max_num:
#         print(f"{max_num} sonlar  ro'yxatidagi eng katta son")
#     else:
#         print(f"{max_num} sonlar  ro'yxatidagi eng katta son emas")
#
#     if minimal_son==min_num:
#         print(f"{min_num} sonlar  ro'yxatidagi eng kichik son")
#     else:
#         print(f"{min_num} sonlar  ro'yxatidagi eng kichik son emas")
# numbers=[23,4,2,87,9,45]
# max_num=9
# min_num=2
# min_max(numbers,max_num,min_num)


#213-MASALA..expensiveProduct(products) - funksiyadagi products - list.
# Unga products sifatida [
#   {
#     "name": "Iphone X",
#     "price": 600
#   },
#   {
#     "name": "Iphone 12",
#     "price": 1500
#   },
#   {
#     "name": "Samsung Note 9",
#     "price": 800
#   },
#   {
#     "name": "Samsung S10",
#     "price": 1100
#   },
# ] shunaqa qiymat beriladi.
# Eng qimmat telefon nomini print qilib bersin bu funksiya.



# def expensiveProduct(products):
#     # `products` ichida eng qimmat mahsulotni izlaymiz
#     expensive_product = products[0]
#     for product in products:
#         if product['price'] > expensive_product['price']:
#             expensive_product = product
#     print(f"Eng qimmat telefon: {expensive_product['name']}")
#
# # Misol uchun products ro'yxatini beramiz
# products = [
#     {"name": "Iphone X", "price": 600},
#     {"name": "Iphone 12", "price": 1500},
#     {"name": "Samsung Note 9", "price": 800},
#     {"name": "Samsung S10", "price": 1100},
# ]
#
# # expensiveProduct funksiyasini chaqiramiz
# expensiveProduct(products)



# import numpy as np
# A = np.random.rand(9, 9, 9)
# s = 0
# for i in range(9):
#     for j in range(9):
#         for k in range(9):
#             if (i == j == k) or (i + j == 8) or (j + k == 8) or (i + k == 8):
#                 s += A[i][j][k]
# print("Bo'yalgan joylar yig'indisi:", s)



# import numpy as np
# s_box=[[0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76],
#     [0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0],
#     [0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15],
#     [0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75],
#     [0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84],
#     [0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF],
#     [0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8],
#     [0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2],
#     [0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73],
#     [0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB],
#     [0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79],
#     [0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08],
#     [0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A],
#     [0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E],
#     [0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF],
#     [0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16]
# ]
#
# s_box_inv=[
#     [0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB],
#     [0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB],
#     [0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E],
#     [0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25],
#     [0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92],
#     [0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84],
#     [0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06],
#     [0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B],
#     [0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73],
#     [0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E],
#     [0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B],
#     [0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4],
#     [0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F],
#     [0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF],
#     [0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61],
#     [0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D]
# ]
#
#
#
#
#
# def subkey(M, key):
#     text = [[int(x) for x in row] for row in M]
#     key = [[int(x) for x in row] for row in key]
#
#     for i in range(4):
#         for j in range(4):
#             M[i][j] = int(M[i][j]) ^ int(key[i][j])
#     return M
#
#
# def s_box_change(M):
#     for i in range(4):
#         for j in range(4):
#             row = int(M[i][j]) >> 4
#             col = int(M[i][j]) & 0x0F
#             M[i][j] = s_box[row][col]
#     return M
#
#
# def inv_s_box(M):
#     for i in range(4):
#         for j in range(4):
#             row = M[i][j] >> 4
#             col = M[i][j] & 0x0F
#             M[i][j] = s_box_inv[row][col]
#     return M
#
#
# def shift_row(M):
#     M[1] = M[1][1:] + M[1][:1]
#     M[2] = M[2][2:] + M[2][:2]
#     M[3] = M[3][3:] + M[3][:3]
#     return M
#
#
# def inv_shift_row(M):
#     M[1] = M[1][-1:] + M[1][:-1]
#     M[2] = M[2][-2:] + M[2][:-2]
#     M[3] = M[3][-3:] + M[3][:-3]
#     return M
#
#
# def galois(a, b):
#     result = 0
#     for i in range(8):
#         if b & 1:
#             result ^= a
#         high = a & 0x80
#         a = a << 1
#         if high:
#             a ^= 0x1B
#         b = b >> 1
#     return result & 0xFF
#
#
# def mixcolumn(M):
#     for i in range(4):
#         column = M[i]
#         M[i] = [galois(column[0], 2) ^ galois(column[1], 3) ^ column[2] ^ column[3],
#                 column[0] ^ galois(column[1], 2) ^ galois(column[2], 3) ^ column[3],
#                 column[0] ^ column[1] ^ galois(column[2], 2) ^ galois(column[3], 3),
#                 galois(column[0], 3) ^ column[1] ^ column[2] ^ galois(column[3], 2)]
#     return M
#
#
# def inv_mixcolumn(M):
#     for i in range(4):
#         column = M[i]
#         M[i] = [galois(column[0], 14) ^ galois(column[1], 11) ^ galois(column[2], 13) ^ galois(column[3], 9),
#                 galois(column[0], 9) ^ galois(column[1], 14) ^ galois(column[2], 11) ^ galois(column[3], 13),
#                 galois(column[0], 13) ^ galois(column[1], 9) ^ galois(column[2], 14) ^ galois(column[3], 11),
#                 galois(column[0], 11) ^ galois(column[1], 13) ^ galois(column[2], 9) ^ galois(column[3], 14)]
#     return M
#
#
# def AES_shifrlash(M, key):
#     M = subkey(M, key)
#     for i in range(1, 10):
#         M = s_box_change(M)
#         M = shift_row(M)
#         M = mixcolumn(M)
#         M = subkey(M, key)
#     M = s_box_change(M)
#     M = shift_row(M)
#     M = subkey(M, key)
#     return M
#
#
# def AES_deshifrlash(C, key):
#     C = subkey(C, key)
#     C = inv_shift_row(C)
#     C = inv_s_box(C)
#     for i in range(1, 10):
#         C = subkey(C, key)
#         C = inv_mixcolumn(C)
#         C = inv_shift_row(C)
#         C = inv_s_box(C)
#     C = subkey(C, key)
#     return C
#
#
# text = "0123456789ABCDEF"
# k = "FEDCBA9876543210"
# M = []
# for i in text:
#     M = np.append(M, ord(i))
# M = np.reshape(M, (-1, 4))
# key = []
# for i in k:
#     key = np.append(key, ord(i))
# key = np.reshape(key, (-1, 4))
# C = AES_shifrlash(M, key)
# print(C)
# c = ''
# for i in C:
#     for j in i:
#         c += chr(j)
# print(c)







def birlashtir_lugatlar(*lugatlar):
    birlashgan = {}
    for lugat in lugatlar:
        for yosh, qiymat in lugat.items():
            if yosh in birlashgan:
                birlashgan[yosh] += qiymat
            else:
                birlashgan[
                    yosh
                ] = qiymat
    return birlashgan

lugat1 = {'yosh1': 10, 'yosh2': 20, 'yosh3': 30}
lugat2 = {'yosh4': 15, 'yosh5': 25, 'yosh6': 35}
lugat3 = {'yosh7': 5, 'yosh8': 10, 'yosh9': 50}


natija = birlashtir_lugatlar(lugat1, lugat2, lugat3)

print("Birlashgan lug'at:", natija)



