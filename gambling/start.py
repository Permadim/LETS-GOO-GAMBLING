import os
from games import classic_roulet


def clear_screen():
    os.system('clear')





def my_games_chosser():
    global money
    print('which shall you play?')
    possible_games = ['classic roulet','quit']
    for i in possible_games: print(i)
    game_chose = input()
    while game_chose not in possible_games:
        print("game not found, try again")
        game_chose = input()

    if game_chose == 'classic roulet':
        money = classic_roulet(money)
    if game_chose == 'quit':
        pass



def cassino_opener():
    global money

    clear_screen()
    print("""WELCOME TO THE MUSTELA CASSINO!!!!!
how much saw you wage?""")
    while True:
        try: 
            money = int(input(""))
            break
        
        except ValueError:
            print("are you stupid? Try again")
    print("""HA, great choice
Now, excited to play some of my games?
    """)
    input()



cassino_opener()
while True:
    clear_screen()
    print(f"You currently have {money} credits")
    my_games_chosser()
