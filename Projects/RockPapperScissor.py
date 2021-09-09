import random
import math # for fucking ceil method
print('Welcome to fucking Rock Papper Scissor game and pick your options')
#start = str(input('PRESS ENTER TO PLAY OR ESC TO QUIT: ')).upper()

# if start == 'E':
#     ask_choice()
# elif start == "Q":
#     quit()
# else:
#     print('Unrecognised INPUT!')


def run_game(rounds:int):
    user_wins:int = 0
    pc_wins:int = 0
    win_necessary = math.ceil(rounds/2) # ceil divides to half for even and half+1 for odd
    print(win_necessary)


    for times in range(rounds):
        pc_choice = random.choice(['r', 'p', 's']) #picks either 1 letter
        print(pc_choice)

        user_choice = str(input('PICK YOUR CHOICE r p s: ')).lower()
        #tie condition
        if user_choice == pc_choice:
            print(f'tie!,bruh you and pc picked {pc_choice}')
        # win condition
        elif (user_choice=='r' and pc_choice=='s') or (user_choice=='p' and pc_choice=='r') or (user_choice=='s' and pc_choice=='p'):
            print(f'OK you win, you picked {user_choice} and dumb pc picked {pc_choice}')
            user_wins += 1
        # loose condition
        elif (user_choice == 'r' and pc_choice == 'p') or (user_choice == 'p' and pc_choice == 's') or (user_choice == 's' and pc_choice == 'r'):
            print(f'looser!, you picked {user_choice} and pc picked {pc_choice}')
            pc_wins += 1

        else:
            print('fucking unrecognised Input so PC wins!')
            pc_wins += 1

        # in long rounds if already anyone wins above half rounds
        if rounds % 2 == 0:
            if user_wins > win_necessary:
                print(f'You won enough {user_wins} winning points out of {rounds} fucking rounds')
                break

            elif pc_wins > win_necessary:
                print(f'THe PC won enough {pc_wins} winning points out of {rounds} fucking rounds')
                break

        else: # for odd numbers i.e 3/2 gives 2
            if user_wins >= win_necessary:
                print(f'You won enough {user_wins} winning points out of {rounds} fucking rounds')
                break

            elif pc_wins >= win_necessary:
                print(f'THe PC won enough {pc_wins} winning points out of {rounds} fucking rounds')
                break

    print(f'END RESULTS : YOU WON {user_wins}!')
    print(f'END RESULTS : PC WON {pc_wins}!')
    print()




if __name__ == '__main__':
    while True:
        ask = str(input('Wanna play fucking game[y/n]: '))

        if ask == 'y':
            rounds = int(input('How many fucking rounds you want: '))
            run_game(rounds)
            continue
        else:
            break
