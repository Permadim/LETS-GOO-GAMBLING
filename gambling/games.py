import os
import random
def clear_screen():
    os.system('clear')




def classic_roulet(curency):
    clear_screen()
    numbers = []
    colors = ['red','green','black']
    for i in range(37):
        numbers.append(str(i))
    print("""Now, in this game, we will roll a classic roulette
This roulette wil have the numbers from 0 to 36
You can chosse between betting in a single number or in the colors RED, GREEN and BLACK 
    """)

    while True:
        bet = input()
        if bet == 'all in':
            bet = curency
            break
        else:
            try:
                 bet = int(bet)
                 break
            except ValueError:
                print("Invalid bet, try again")


    
    
    curency -= bet
    choosen_bet = input('Trype your desired choosen_bet:').lower()
    while not ((choosen_bet in colors) or (choosen_bet in numbers)):
        print("not a valid choosen_bet, try again")
        choosen_bet = input().lower()
    if choosen_bet in colors:
        multiplyer = 1.2
    if choosen_bet in numbers:
        multiplyer = 2.3
    winner_number = random.choice(numbers)
    if winner_number == '0': winner_color = 'green'
    elif int(winner_number)%2 == 0: winner_color = 'red'
    else: winner_color = 'black'
    winner_qualitis = [winner_number,winner_color]
    if choosen_bet in winner_qualitis:
        curency += bet*multiplyer
        print("CONGRATULATIOMS, YOU JUST WON!!!!")
        print(f"YOU JUST WON {bet*multiplyer} DOLARS!!!!!")
    else: 
        print("OH NO! YOU JUST LOST THE BET :(((")
        print(f"AND WITH THAT LOSS, YOU JUST LOST {bet} DOLARS")
        print("YOU CANT JUST LET IT END LIKE THIS, IN THE LOSS")
    input()
    return curency
