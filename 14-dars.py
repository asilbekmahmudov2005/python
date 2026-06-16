#1
# ismlar=["Jonibek","Shamshod","Asad"]
# print("salom ",ismlar[0],"bugun choyxona bormi?")
# print(ismlar[2],"choyxona boramizmi")

#2
# sonlar=[1,2,3,-5,0.8]
# sonlar[-1]=5
# a=sonlar[0]+sonlar[-1]
# print(sonlar)
# print(a)

#3
# t_shaxslar=['ABU ALI IBN SINO','AMIR TEMUR','ALISHER NAVOIY']
# z_shaxslar=['otabek','shavkat','saida']
# kurishmoqchiman=t_shaxslar.pop(1)
# kurishmoqchiman2=z_shaxslar.pop(0)
# print(f" Men tarixiy shaxslardan {kurishmoqchiman} bilan,zamonaviy shaxslardan esa {kurishmoqchiman2} bilan suhbat qilishni istar edim")

#4

# friends=[]
# friends.append('jasur')
# friends.append('asad')
# friends.append('laziz')
# friends.append('omad')
# print(friends)
# kelmaydi=friends.remove("asad")
# friends.insert(0,"sardor")
# friends.append("akish")
# friends.insert(2,"akbar")
# print(friends)

# taomlar=['osh','gush','msnti','tovuq','shurva']
# nonushta=taomlar[:]
# nonushta.append("tabaka")
# nonushta.append("sut")
# nonushta.insert(0,"qaymoq va non")
# nonushta=tuple(nonushta)
# print(taomlar)
# print(nonushta)

#1
# ismlar=["Ali","Vali","Omad","Yashnar","Asad"]
# n=0
# for ism in ismlar:
#     print(" salom ",ism)
#     n += 1
# print(f" kod {n} marta takrorlandi")

#2
# sonlar=list(range(11,100,2))
# print(sonlar)
# for son in sonlar:
#     print(f"{son} ning kubi {son**3} ga teng")

#3

# n_people=int(input("Bugun necha ksihi bilan suhbat qildingiz: "))
# ismlar=[]
# for n in range(n_people):
#     ismlar.append(input(f"{n+1} chi kim bilan kurishgan edingiz"))
# print(ismlar)

#1
# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car!="gm":
#         print(car.upper())
#     else:
#         print(car.title())

#2
# login=input(" loginingizni kiriting: ")
# if login=="admin":
#     print(" xush kelbsiz admin")
#     print("Foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#     print(f"Xush kelibsiz, {login}!")

#3
# a=int(input("istalgan sonni kiriting: "))
# if a>0:
#     print((a)**0.5)
# else:
#     print("musbat son kiriting ")

#1
# foydalanuvchi_yoshi=int(input("yoshingizni kiriting: "))
# if foydalanuvchi_yoshi<4 or foydalanuvchi_yoshi>60:
#     narx=0
# elif foydalanuvchi_yoshi<18:
#     narx=10000
# elif foydalanuvchi_yoshi>=18:
#     narx=20000
# print(narx)

#2
# a=int(input("1-sonni kiriting: "))
# b=int(input("2-sonni kiriting: "))
# if a>b:
#     print(f" {a}>{b} dan")
# elif a<b:
#     print(f"{a}<{b} dan")
# else:
#     print("ular teng")

#3
# mahsulotlar=["anor","apelsin","behi","qulupnay","olma","nok","shaftoli","olcha","anjir","kivi"]
# savat=[]
# mah1=input(" savatga 1-mahsulotni qushing: ")
# mah2=input(" savatga 2-mahsulotni qushing: ")
# mah3=input(" savatga 3-mahsulotni qushing: ")
# mah4=input(" savatga 4-mahsulotni qushing: ")
# mah5=input(" savatga 5-mahsulotni qushing: ")
# if mah1 in mahsulotlar:
#     print(f" Do'konimizda {mah1} bor")
# if mah1 not in mahsulotlar:
#     print(f" Do'konimizda {mah1} yuq")
# if mah2 in mahsulotlar:
#     print(f" Do'konimizda {mah2} bor")
# if mah2 not in mahsulotlar:
#     print(f" Do'konimizda {mah2} yuq")
# if mah3 in mahsulotlar:
#     print(f" Do'konimizda {mah3} bor")
# if mah3 not in mahsulotlar:
#     print(f" Do'konimizda {mah3} yuq")
# if mah4 in mahsulotlar:
#     print(f" Do'konimizda {mah4} bor")
# if mah4 not in mahsulotlar:
#     print(f" Do'konimizda {mah4} yuq")
# if mah5 in mahsulotlar:
#     print(f" Do'konimizda {mah5} bor")
# if mah5 not in mahsulotlar:
#     print(f" Do'konimizda {mah5} yuq")

# foydalanuvchilar=["anvar","aziz","qobil","shavkat","olim"]
# foy=input("loginingizni kiriting: ")
# if foy in foydalanuvchilar:
#     print("xush kelibsiz ")
# if foy not in foydalanuvchilar:
#     print(f"{foy} bu login band")

# son_k=int(input(" son kiriting: "))
# if son_k%2==0:
#     print(f"{son_k} 2 ga qoldiqsiz bo'linadi")

