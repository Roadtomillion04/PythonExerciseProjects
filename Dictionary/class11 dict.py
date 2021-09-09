# '''count the frequency of words using dict'''
# from json import dumps
# user_input = str(input('prompt: '))
# lists = user_input.split() #As default split splits based on space
# print(lists)
# dictinory = {}
# for items in lists:
#     k = items
#     v = lists.count(items)
#
#     if not items in dictinory: #this prevents repetition entry of keys
#         dictinory[k] = v
#                                                     # For nice gap
# print(f'The counting frequency is {dumps(dictinory, indent=1)}')


'''page 288 Type C'''
# from operator import itemgetter
# calandar = {'jan': 31, 'feb': 28, 'mar': 31, 'apr': 30, 'may': 31, 'june': 30, 'july': 31, 'aug': 31, 'sep': 30, 'oct': 31, 'nov': 30, 'dec': 31}
# ask = str(input('select month: '))
# if ask in calandar.keys():
#     print(f'{ask} month has {calandar[ask]} days!')
#
# print(sorted(calandar.keys()))
#
# for months, days in calandar.items():
#     if days == 31:
#         print(f'{months} months has 31 days!!')
#                                 # grabs second element of tuple
# print(sorted(calandar.items(), key=itemgetter(1)))


'''swap keys and values'''
d = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
inverted_d:dict = {}
for k, v in d.items():
    inverted_d[v] = k

print(inverted_d)

