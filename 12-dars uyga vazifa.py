# #1
# def user_data(first_name, last_name, age):
#     print(f"Ism: {first_name}")
#     print(f"Familiya: {last_name}")
#     print(f"Yosh: {age}")
#
# first_name = input("Ismingizni kiriting: ")
# last_name = input("Familiyangizni kiriting: ")
# age = input("Yoshingizni kiriting: ")
#
# user_data(first_name, last_name, age)
#from curses.ascii import isalnum, isdigit


#2
# def find_max(a, b, c):
#     if a > b and a > c:
#         max = a
#     elif b > a and b > c:
#         max = b
#     else:
#         max = c
#     print(f"Eng kattasi: {max}")
#
# a = input(" a sonini kiriting: ")
# b = input(" b sonini kiriting: ")
# c = input(" c sonini kiriting: ")
# find_max(a, b, c)

#3
# def find_letter_count(word,letter):
#     coun=word.count(letter)
#     print(f"{word} so'zidagi {letter} dan {coun} ta bor")
#
#
# word=input(" so'z kiriting: ")
# letter=input(" qidirayotgan harfingizni kiriting: ")
# find_letter_count(word,letter)

#4
# def list_sum(myList):
#     jami=0
#     for son in myList:
#         jami+=son
#     print(f"listning umumiy yig'indisi {jami}")
#
# list_sum([1,2,3,4])

#5
# def daraja(a, b):
#     print(a**b)
# daraja(2,3)
from math  import *

#6
# def daraja4(a, b, c, d):
#     print(a**b)
#     print(c**d)
# daraja4(2,3,4,1)

#7

# def digit_count_and_sum(word):
#     jami = 0
#     raqam = 0
#
#     for son in word:
#         if son.isdigit():
#             jami += int(son)
#             raqam += 1
#
#     print(f"Raqamlar yig'indisi = {jami}")
#     print(f"Jami raqamlar: {raqam}")
#
# digit_count_and_sum("sakdvmmd 21444")

#8
# def add_right(a, b):
#     result = int(str(a) + str(b))
#     print(result)
# add_right(12,22)

#9
# def add_left(a, b):
#     result=int(str(b)+str(a))
#     print(result)
# add_left(23,56)
#10
# def work_with_list(a):
#     son = min(a)
#     yangi_list = []
#     for k in a:
#         yangi_list.append(k * son)
#     print(f"yangi list {yangi_list}")
#
#
# work_with_list([3, 2, 10, 6])
#11
# def big_sales(sales):
#     return max(sales, key=sales.get)
#
# sales={
#   "yanvar": 12000,
#   "mart": 6000,
#   "aprel": 15000,
#   "sentabr": 9000,
#   "dekabr": 10000,
# }
# print(big_sales(sales))

#12
# def min_max(numbers, max_num, min_num):
#     is_max = (max_num == max(numbers))
#     is_min = (min_num == min(numbers))
#     return is_max, is_min
#
# numbers = [14, 5, 8, 21, 5]
# print(min_max(numbers, 21, 5))
# print(min_max(numbers, 14, 8))

#13
# def expensiveProduct(products):
#     print(max(products, key=lambda product: product["price"])["name"])
# telefonlar = [
#     {
#         "name": "Iphone X",
#         "price": 600
#     },
#     {
#         "name": "Iphone 12",
#         "price": 1500
#     },
#     {
#         "name": "Samsung Note 9",
#         "price": 800
#     },
#     {
#         "name": "Samsung S10",
#         "price": 1100
#     },
# ]
#
# expensiveProduct(telefonlar)