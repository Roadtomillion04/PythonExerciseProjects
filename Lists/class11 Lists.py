'''Page 263 TYPE C'''
'''
lists = [1, 2, 4, 7, 6]
lists.reverse()
print(lists)


l1 = eval(input())
l2 = eval(input())
print(l1 + l2)


l3 = eval(input('e: '))
new_lis = []
for num in l3:
    if num > 10:
        num = 10
    new_lis.append(num)
print(new_lis)


input_name = eval(input('en: '))
new = []
for strings in input_name:
    new.append(strings[1:])
print(new)


lis = [a for a in range(50)]
lis2 = [a**2 for a in range(50)]
print(lis)
print(lis2)

counter = 0
l4 = []
for alpha in 'abcde':
    counter += 1
    alpha *= counter
    l4.append(alpha)
print(l4)


l = [3, 1, 4, 5]
m = [1, 5, 9, 10]
n = []
a = len(m)
if len(l) == len(m):
    for i in range(a):
        n.append(l[i] + m[i])
print(n)


l5 = [1, 3, 5, 7, 0]
       #0    adds rest of the list
l5 = l5[-1:] + l5[:-1]
print(l5)
'''

'''Find second largest number'''
# try:
#     user_input = eval(input("enter list: "))
#     user_input.sort()
#     length = len(user_input)
#     secon_large_no = user_input[-2]
#     print(f"second large number is {secon_large_no}")
# except IndexError:
#     print("hey enter more than one number")
# except AttributeError:
#     print("please enter only list!")


'''add all int(odd) in given list'''
L = [1, 2, 3, 4, 5, 6, 7]
sum = 0
for num in L:
    if num %2 != 0:
        sum += num
print(sum)


'''Count Frequency of list'''
# us_input:list = eval(input('Enter a List: '))
# dupl = []
# uniq = []
# repatead:bool = False #IDk how I did this but is's not a good way
# for values in us_input:
#     if not repat_count:
#         print(f'{values} ocuured {us_input.count(values)} times')
#
#     if us_input.count(values) > 1:
#         repatead = True
#         if not values in dupl: # this prevents repetion entry
#             dupl.append(values)
#             repated = False
#     else:
#         repated = False
#         uniq.append(values)
# print(f'duplicate = {dupl}')
# print(f'unique = {uniq}')


''' Find min element and its index'''
# enter_input:list = eval(input('Enter a list: '))
# new = enter_input[:]
# new.sort()
# min_element = new[0]
# print(f'The min element is {min_element} and index {enter_input.index(min_element)}')


