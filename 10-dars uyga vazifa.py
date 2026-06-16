#1
# pochtalar = ["user1@gmail.com", "user2yahoo.com", "user3@outlook.com"]
# for pochta in pochtalar:
#     if "@" not in pochta:
#         print(f" noto'g'ri email manzil: {pochta}")
#2
# foydalanuvchi_paroli=["password123", "Qwerty!", "admin", "StrongPass1!"]
# for parol in foydalanuvchi_paroli:
#     if len(parol)<8:
#         print(f"juda qisqa:{parol}")
#     elif parol.isalpha():
#         print(f"kuchsiz parol{parol}")
#     else:
#         print(f"kuchli parol{parol}")
#3
# haroratlar=[20,22, 19, 24, 25, 23, 21]
# jami=0
# for h in haroratlar:
#     jami+=h
# urtacha=jami/len(haroratlar)
# print(urtacha," harorat")
# for h in haroratlar:
#     if h > 22:
#         print(h,">-iliq kun")
#     else:
#         print(h,">-sovuq kun")

#4
# mavjudlar = ["Osh", "Shashlik", "Manti", "Lag'mon"]
# foydalanuvchi = input("Nima ovqat buyurtma qilasiz?: ")
# topildi = False
# for taom in mavjudlar:
#     if foydalanuvchi == taom:
#         topildi = True
#         break
#
# if topildi:
#     print("Buyurtma qabul qilindi")
# else:
#     print("Bunday ovqat yo'q")

#5
# foydalanuvchi_yoshlari=[16, 21, 17,30, 25]
# for foydalanuvchi in foydalanuvchi_yoshlari:
#     if foydalanuvchi<18:
#         print(foydalanuvchi,">-hali yoshsiz")
#     else:
#         print(foydalanuvchi,"xush kelibsiz")

#6
# xabarlar=["Yangi xabar", "Batareya past", "Yangilanish mavjud"]
# for xabar in xabarlar:
#     if xabar=="Batareya past":
#         print("telefoningizni quvvatlang")

#7
# fayllar = ["kitob.jpg", "ko_jiguli.mp3", "tabiat.jpg", "malohat.mp3", "iphone16.jpg"]
#
# musiqalar = []
# rasmlar = []
#
# for fayl in fayllar:
#     if fayl.find(".jpg") != -1:
#         rasmlar.append(fayl)
#     elif fayl.find(".mp3") != -1:
#         musiqalar.append(fayl)
#
# print("Rasmlar:", rasmlar)
# print("Musiqalar:", musiqalar)



