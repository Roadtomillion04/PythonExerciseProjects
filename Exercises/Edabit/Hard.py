'''Disarium Number'''
# A number is said to be Disarium if the sum of its digits raised to their respective positions is the number itself.
def is_disarium(n:int):
    n = str(n)
    sum = 0
    i: int = 1

    for x in n:
        sum += int(x) ** i
        i += 1
    print(sum)

    return sum == int(n)

print(is_disarium(135))
print(is_disarium(13))


