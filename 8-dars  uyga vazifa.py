#append
# mevalar=["olma","anor","behi"]
# mevalar.append("banan")
# print(mevalar) -> ['olma', 'anor', 'behi', 'banan']  yani oxiriga bitta element qo'shyapti
from Tools.scripts.verify_ensurepip_wheels import print_notice

#extend
# mevalar=["olma","anor"]
# mevalar.extend("banan")
# print(mevalar) -> ['olma', 'anor', 'b', 'a', 'n', 'a', 'n'] elementlarni bittalab qushadi

#insert
# mevalar=["behi","anor","olma"]
# mevalar.insert(0,"anjir")
# print(mevalar) -> ['anjir', 'behi', 'anor', 'olma']  indeks buyicha element qushish

#pop
# mevalar=["olma","anor"]
# mevalar.pop(1)
# print(mevalar) -> ['olma'] 1-indeksli elementni yulib oladi hech qanday o'chirmaydi

#remove
# mevalar=["anor","olma","behi"]
# mevalar.remove("olma")
# print(mevalar) -> ['anor', 'behi'] 1ta elementni o'chirib tashladik

#clear
# meva=["olma","behi"]
# x=meva.clear()
# print(meva) -> [] yani tozalab beradi

#copy
# cars=["bmw m5", "porsche 911","mercedec gts"]
# cars.copy()
# print(cars) -> ['bmw m5', 'porsche 911', 'mercedec gts'] kopiya qiladi

#count
# mashinalar=["bmw","mercedec","supra mk4","bmw","bmw"]
# x=mashinalar.count("bmw")
# print(x) -> 3 elementlarni sanayapti

#index
# meva=["olma","anor","behi"]
# x=meva.index("behi")
# print(x) ->2 nechanchi indeksli ekanini chiqaradi

#sort
# mevalar=["olma","behi","anor","gilos"]
# mevalar.sort()
# print(mevalar) ->['anor', 'behi', 'gilos', 'olma'] tartiblayapti

#reverse
# mevalar = ["olma", "behi", "anor", "gilos"]
# mevalar.reverse()
# print(mevalar) -> ['gilos', 'anor', 'behi', 'olma'] elementlarni indeks kamayishi buyicha chiqaradi
