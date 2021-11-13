import random

def play_game(min_value: int, max_value: int):
    answer = random.randint(min_value, max_value)
    print(answer)

    # asking pc guess to user
    while True:
        try:
            guess:int = random.randint(min_value, max_value)
            ask_input = str(input(f'is {guess} is h[too_high], l[too low] or c[correct]: '))

            if ask_input == 'h':
                max_value = guess - 1 # Just for non repeating same value!
                print(min_value, max_value)
                continue

            elif ask_input == 'l':
                min_value = guess + 1
                print(min_value, max_value)
                continue

            elif ask_input == 'c':
                print('Thank you for playing!!')
                break

            else:
                print('unrecognised Input!')
                break


        except ValueError: # when min and max are equal!
            print('Sorry, you loose try again!')
            break

if __name__ == '__main__':
    play_game(1, 1000)

