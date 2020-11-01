# Exercise 8
# Rock Paper Scissors

import random

index = ['Scissors', 'Rock', 'Paper', 'exit']

computer = index[random.randint(0, 2)]

player_count = 0
computer_count = 0

player = False

while player == False:
    player = input('Rock, Paper, Scissors?: ')
    if player == computer:
        print('Tie.')
        print(player_count, computer_count)
    elif player == 'Rock':
        if computer == 'Paper':
            print('You lose!', computer, 'covers', player)
            computer_count += 1
            print(player_count, computer_count)
        else:
            print('You win!', player, 'smahes', computer)
            player_count += 1
            print(player_count, computer_count)
    elif player == 'Paper':
        if computer == 'Scissors':
            print('You lose!', computer, 'cuts', player)
            computer_count += 1
            print(player_count, computer_count)
        else:
            print('You win!', player, 'covers', computer)
            player_count += 1
            print(player_count, computer_count)
    elif player == 'Scissors':
        if computer == 'Rock':
            print('You lose!', computer, 'smashes', player)
            computer_count += 1
            print(player_count, computer_count)
        else:
            print('You win!', player, 'cuts', computer)
            player_count += 1
            print(player_count, computer_count)
    elif player == 'Exit':
        print(f'Final score --' ' player: ' + str(player_count) + ' computer: ' + str(computer_count))
        print(""" 
        
        Thanks for playing!""")
        break
    else:
        print('Invalid play, check spelling')

    if player_count == 50:
        print(f'Final score --' ' player: ' + str(player_count) + ' computer: ' + str(computer_count))
        print("""
       
        You won! Congratulations!""")
        break
    
    if computer_count == 50:
        print(f'Final score --' ' player: ' + str(player_count) + ' computer: ' + str(computer_count))
        print("""
        
        You lost! Come again!""")
        break
    player = False
    computer = index[random.randint(0, 2)]

# Made by Simoniezi
# Discord: Simoniezi#7138