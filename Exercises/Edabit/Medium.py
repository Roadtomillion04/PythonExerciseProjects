# '''Recreating python int and str'''
# def int_to_str(value:int):
#     return str(value)
#
# def str_to_int(value:str):
#     return int(value)
#
#
# '''Fizzbuzz interview question'''
# def fizz_buzz(num):
#     if num % 3 == 0 and num % 5 == 0:
#         return "FizzBuzz"
#     elif num % 5 == 0:
#         return "Buzz"
#     elif num % 3 == 0:
#        return "Fizz"
#     else:
#        return str(num)
#
# print(fizz_buzz(3))
# print(fizz_buzz(15))
# print(fizz_buzz(7))
#

'''count the number without len()'''
# def number_length(num:int):
#     counter = 0
#     for _ in str(num):
#         counter += 1
#     print(counter)
#
# number_length(4)
# number_length(11)
# number_length(1000)


'''Cricket balls to over - take balls and convert to overs'''
# def total_overs(balls:int):
#     overs, balls_left = divmod(balls, 6) # returns in tuple
#     print(f'{overs}.{balls_left}') if balls_left > 0 else print(overs)
#
# total_overs(12)
# total_overs(5)
# total_overs(120)


'''Date Format - MM/DD/YYYY to YYYYDDMM'''
# def format_date(date:str):
#     date = date.split('/')
#     year, day, month = date[::-1]
#     print(f'{year}{day}{month}')
#
# format_date("01/15/2019")
# format_date("03/13/2004")


'''Get the area of country - 
The total world's landmass is 148,940,000 [Km^2]'''
# def area_of_country(name:str, area:float):
#     total_landmass = 148940000
#     result = round((area / total_landmass)*100, 2)
#     print(f'{name} is {result}% of total World\'s landmass')
#
# area_of_country("Russia", 17098242)
# area_of_country("USA", 9372610)


'''Simple OOP calculator'''
# class Calculator:
#     def __init__(self):
#         pass
#
#     def add(self, x:int, y:int):
#         print(x+y)
#     def subtract(self, x:int, y:int):
#         print(x-y)
#     def multiply(self, x:int, y:int):
#         print(x*y)
#     def division(self, x:int, y:int):
#         assert y != 0, 'Zero division error'
#         print(x/y)
#
# calculator = Calculator()
# calculator.add(10, 5)
# calculator.subtract(10, 5)
# calculator.multiply(10, 5)
# calculator.division(10, 5)


'''Classes For Fetching Information on a Sports Player'''
# class Player():
#     def __init__(self, name:str, age:int, height:int, weight:int):
#         self.name = name
#         self.age = age
#         self.height = height
#         self.weight = weight
#
#     def get_age(self):
#         print(f'{self.name} is {self.age} years old')
#     def get_height(self):
#         print(f'{self.name} is {self.height}cm ')
#     def get_weight(self):
#         print(f'{self.name} is {self.weight}kg')
#
# p1 = Player("David Jones", 25, 175, 75)
# p1.get_age()
# p1.get_height()
# p1.get_weight()


'''Calculate the Profit'''
# def profit(info:dict):
#     cost_price, sell_price, quantity = info.values()
#     total_sales = (sell_price - cost_price) * quantity
#     print(round(total_sales, 1))
#
# profit({
#   "cost_price": 32.67,
#   "sell_price": 45.00,
#   "inventory": 1200
# })
#
# profit({
#   "cost_price": 225.89,
#   "sell_price": 550.00,
#   "inventory": 100
# })


'''Adding Numbers - takes two str and returns in str'''
# def add(x:str, y:str):
#     try: print(str(int(x) + int(y)))
#     except: print('Invalid Operands')
#
# add('111', '111')
# add('', '555')


'''List of Multiples'''
# def list_of_multiples(num:int, length:int):
#     lis = []
#     for i in range(1, length+1):
#         lis.append(num*i)
#     print(lis)
#
# list_of_multiples(5, 7)
# list_of_multiples(4, 2)


'''Full Name and Email'''
# class Employee():
#     def __init__(self, first_name:str, last_name:str):
#         self.first_name = first_name
#         self.last_name =  last_name
#
#         self.full_name = f'{first_name} {last_name}'
#         self.email = f'{first_name}.{last_name}@company.com'.lower()
#
# emp_1 = Employee("John", "Smith")
# emp_2 = Employee("Mary",  "Sue")
# emp_3 = Employee("Antony", "Walker")
#
# print(emp_1.full_name)
# print(emp_2.email)
# print(emp_3.first_name)


'''Algorithms I: Introduction to Recursion - Do factorials'''
# def factorial(num:int):
#     return 1 if num == 0 else num * factorial(num - 1) # it calls itself until reaches 0
#
# print(factorial(5))
# print(factorial(1))


'''Sum of Odd and Even Numbers'''
# def sum_odd_and_even(lst:list):
#     odd, even = [], []
#     for num in lst:
#         odd.append(num) if num % 2 != 0 else even.append(num)
#     result_list = [sum(even), sum(odd)]
#     print(result_list)
#
# sum_odd_and_even([1, 2, 3, 4, 5, 6])
# sum_odd_and_even([0, 0])


'''Sum Fractions - 1st ele - numerator, 2nd ele - denominator'''
# def sum_fractions(lst:list):
#     all = len(lst)
#     first_ele = [lst[a][0] for a in range(all)] # getting 0 element
#     second_ele = [lst[a][1] for a in range(all)] # getting 1st element
#
#     print(first_ele, second_ele)
#
#     result = [first_ele[x]/second_ele[x] for x in range(all)] # doing fraction with x0, y0 like that
#
#     sum = 0
#     for i in result:
#         sum += round(i, 0)
#     print(sum)

# sum_fractions([[18, 13], [4, 5]])
# sum_fractions([[11, 2], [3, 4], [5, 4], [21, 11], [12, 6]])


'''Harshad Number - number divisible by sum of its digits'''
# def is_harshad(n:int):
#     sum = 0
#     for i in str(n):
#         sum += int(i)
#
#     return n % sum == 0
#
# print(is_harshad(171))
# print(is_harshad(481))


'''Sum of Missing Numbers - sort list and find missing numbers'''
def sum_missing_numbers(lst:list):
    start, end = min(lst), max(lst)

    arr = []
    for ele in range(start, end):
        if ele not in lst:
            arr.append(ele)

    print(sum(arr))

sum_missing_numbers([4, 3, 8, 1, 2])
sum_missing_numbers([17, 16, 15, 10, 11, 12])
sum_missing_numbers([1, 2, 3, 4, 5])
