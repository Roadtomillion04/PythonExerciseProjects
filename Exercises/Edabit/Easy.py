'''from edabit'''
'''convert mins to sec'''
#minute = int(input('ENter a minute: '))
#sec = minute * 60
#print(f'{minute} minute is {sec} seconds')


'''stuttering the word'''
def stutter(word:str):
    a = word[:2]
    b = '..'
    print(f'{a}{b} {a}{b} {word}?')
#stutter('word')


'''find discount'''
# def discount(price, discont):
#     print(price * (100 - discont)/100)
# discount(100, 75)
# discount(199, 13)
# discount(5999, 23 )


# '''curzon number 2**num + 1 is divisible by 2*num +1'''
# def is_curzon(num):
#     a = 2**num + 1
#     b = 2*num + 1
#     if a % b == 0:
#         print(f'{num} is a curzon number')
# is_curzon(9)
# is_curzon(5)
# is_curzon(14)
#

# '''calculator'''
# def calculator(num1:float, operator, num2:float):
#     if operator == '+':
#         print(num1 + num2)
#     elif operator == '*':
#         print(num1 * num2)
#     elif operator == '/':
#         if num2:
#             print(num1 / num2)
#
# calculator(2, '+', 5)
# calculator(2, '/', 0)


'''How many vovels'''
# def count_vowels(txt):
#                 # tuple comprehension
#    print(sum(x in "aeiou" for x in txt))
#
# count_vowels('aaaeeiioouu')
#

'''ASCII code'''
# def ascii_code(letter:str):
#     print(ord(letter) if len(letter) == 1 else None)
# ascii_code('aa')
# ascii_code('A')


'''Inclusive list ranges'''
def inclusive_list(start:int, end:int):
    print(list(range(start, end+1) if start<end else [start]))
inclusive_list(1, 5)
inclusive_list(15, 5)


'''Vowel replacer'''
def vowel_replacer(txt:str, symbol):
    for x in txt:
        if x in 'aeiou': #The in keyword is used to check if a value is present in a sequence
            txt = txt.replace(x, symbol)
    print(txt)
vowel_replacer('asdsseii', '?')


'''Programming polygot - assign points to language and display them'''
# def get_languages(points:int):
#     program_lang = {'c#': 1, 'c++': 2, 'java': 10, 'python': 32}
#     for k, v in program_lang.items():
#         if points > v:
#             print(k, v)
#get_languages(10)


'''acronymes '''
# def acronymes(words:str):
#     words = words.split()
#     a:str = ''
#     for word in words:
#         word = word[:1]
#         '''adding word to emtpy string to get result in same line'''
#         a += word.upper()
#     print(a)
# acronymes('Aritfi Intell mac lear')


'''Hiding card number'''
def hide_card_num(num:str):
    if num.isdigit():
        split_num = num[:-4]
        tail = num[-4:]
        split_num = len(split_num) * '*'
        print(split_num + tail)
hide_card_num('7392047324974')


'''Return true if x == o times'''
# def XO(txt:str):
#     x_count = txt.count('x')
#     o_count = txt.count('o')
#     if x_count == o_count:
#         return True
#     elif (x_count and o_count) == 0:
#         return True
#     else:
#         return False
#
# print(XO('ooxxox'))
# print(XO('ooxxx'))
# print(XO('asdfg'))


'''shuffle the name'''
def shuffle_name(name:str):
    first, last = name.split()[0], name.split()[1]
    return ' '.join([last, first])
print(shuffle_name('Nirmal Kumar'))


'''hamming distance if two str dosent matches count'''
# def hamming_distance(str1, str2):
#     counter = 0
#     a = len(str1)
#     b = len(str2)
#
#     if a == b:
#         if str1 == str2:
#             print(0)
#
#         else:
#             for idx in range(a): # grabbing index and checking down below
#                 if str1[idx] != str2[idx]:
#                     counter += 1
#
#             print(counter)
# hamming_distance('asd', 'asd')
# hamming_distance('purple', 'purely')


