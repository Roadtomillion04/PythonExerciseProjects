'''match phone number pattern'''
# import re
# phone_no_pattern = re.compile(r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$')
# user_input = str(input('Enter phone number: '))
#                             #Remeber the pattern has to be in string
# if phone_no_pattern.search(user_input):
#     print(f'{user_input} is a valid_number')
# else:
#     print(f'{user_input} is Invalid number')

'''Chect string is palindrome or not'''
#palindrome ex - dad bob aibohphobia nan
# str_input = str(input('Enter string: '))
# reverse_str = str_input[::-1]
# print(reverse_str)
# if str_input == reverse_str:
#     print(f'{str_input} is a palindrome')
# else:
#     print(f'{str_input} is not a palindrome')


'''Print prototype of bill'''
#from datetime import datetime
# now = str(datetime.now())
#
# class Item(): #class attribute
#     all = []
#     def __init__(self, name:str, quantity: int, price: int):
#         #checking validation
#         assert price >= 0, f'Price {price} must be greater than zero!'
#         assert quantity >= 0, f'{quantity} must be greater than zero!'
#
#         # assigning instanciate attributes
#         self.name = name
#         self.quantity = quantity   #instanciate attributes
#         self.price = price
#
#         #appending values
#         Item.all.append(self)
#
#
#     def calculate_price(self):
#         gst: float = 0.08
#         tax: float = (price * quantity) * gst
#         total: float = (price * quantity)
#         net = total + tax
#         return net
#
# available_items = [f'Amul Butter {x*100}g' for x in range(1, 10)]
# print(available_items)
#
# store_items = {}
#
# for i in available_items:
#     user_input = input(f'{i} : ')
#     store_items[i] = int(user_input) if user_input else 0
# print(store_items)
#
#
# columns = '-' * 75
# print('\t\t\t     MY SUPERMARKET')
# print(columns)
# # \t adds tabs
# print(f'\tDate:\t\t\t\t\t{now}')
# print(columns)
# print('\titems\t\tprice\t\tquantity\t\ttotal')
# print(columns)
# for names, quantity in store_items.items():
#     names = Item(names, quantity, int(names.split()[2].replace('g', '')))
#
#     print(names.name, names.quantity, names.price)
#
#     print(f' {names}\t{price}\t\t {v}\t\t\t{names.calculate_price()}')
# print()
# #print(f'\tTax:\t\t\t\t\t\t\t{names.calculate_price()}')
# print(columns)
# #print(f'\tAmount Payable:\t\t\t\t\t\t{net}')



'''Rolling Dice'''
# import random
# min_value = 1
# max_value = 6
#
# while True:
#     ask_input = str(input('Roll the dice?[y/n]: '))
#
#     if ask_input == 'y':
#         times = int(input('How many times: '))
#
#         assert times > 0, 'num must be greater than zero'
#
#         print('Rolling dice')
#         print('The values are:')
#
#         for i in range(times):
#             print(random.randint(min_value, max_value))
#         continue
#
#     else:
#         break



'''password with sha1'''
import hashlib

def encode_password(password:str, hash_type:str = 'sha1'):
    # unicode must be encoded before hashing!
    encode = hashlib.sha1(password.encode('utf-8')).hexdigest () # don't forget to call hexadigest()


encode_password('ksdsads03')