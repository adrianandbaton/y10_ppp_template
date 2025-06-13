import random
import os 
deck = ['R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6','R7', 'R8', 'R9', 'R+2', 'RS', 'RR', 
'Y0', 'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6','Y7', 'Y8', 'Y9', 'Y+2', 'YS', 'YR',
'G0', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6','G7', 'G8', 'G9', 'G+2', 'GS', 'GR',
'B0', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6','B7', 'B8', 'B9', 'B+2', 'BS', 'BR',
'R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6','R7', 'R8', 'R9', 'R+2', 'RS', 'RR', 
'Y0', 'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6','Y7', 'Y8', 'Y9', 'Y+2', 'YS', 'YR',
'G0', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6','G7', 'G8', 'G9', 'G+2', 'GS', 'GR',
'B0', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6','B7', 'B8', 'B9', 'B+2', 'BS', 'BR', 'WD4', 'WD4']

random.shuffle(deck)

rules = input('Do you want to review the rules?(Y/N)')
while rules != "N" and rules != "Y":
    rules = input("Please reenter with (Y/N)")
if rules == 'Y':
    print("""Each player has 7 cards 

First one to use all their cards win 

You can put a card of the same colour on top of each other 

You can put a card with the same number or action on top of each other  

Action cards  

Reverse – goes back to your turn 

Skip – goes back to your turn 

Draw 2 – opponent draws 2 

Wild draw 4 – opponent draws 4, and you get to choose the colour of the next card placed 

Change colour – changes the colour of the next card placed 

Flip – flip every card 

Wild draw colour card – draw until you get the colour chosen and then said colour will be the colour of the next card placed 

Draw 1 – opponents draw 1 

Draw 5 – opponents draw 5 

Skip everyone – goes back to your turn 

You cannot play after you draw

If you want to stop the game, press 'q' at the end of each turn""")


def distribute_cards(number, deck):
    player_deck = []
    for i in range(number):
        player_deck.append(deck[random.randint(0,104)])
    return player_deck

def next_turn(player_deck, player1_deck, player2_deck):
    whos_turn(player_deck, player1_deck, player2_deck, deck)
    ready = input("Has the laptop passed to the next user? (Y?N)")
    while ready.upper() != 'Y':
        ready = input("OK, now has the laptop been passed (Y/N)")
    if ready  == 'Y':
        os.system('clear')
    elif ready == 'Q' or 'q':
        quit()
    return ready, player_deck, player1_deck, player2_deck

def draw_card(player_deck, deck):
    x = deck[random.randint(0,104)]
    player_deck.append(x)
    return player_deck

def whos_turn(player_deck, player1_deck, player2_deck, deck):
    valid = True
    while valid:
        turn = int(input("Who's turn is it? Player 1 or player 2?"))
        if turn == 1: 
            player_deck = player1_deck
            valid = False
        elif turn == 2:
            player_deck = player2_deck
            valid = False
        else: 
           print('Please enter a valid player!')
           turn = int(input("Who's turn is it? Player 1 or player 2?"))
    return player_deck


def play_card(player_deck, center_card, player1_deck, player2_deck, deck):
    whos_turn(player_deck, player1_deck, player2_deck, deck)
    card = input("What card do you wish to place?, press 'd' to draw card")
    if card == 'd':
        draw_card(player_deck, deck)

    while card not in player_deck and card != 'd':
        print("This card is not in your deck, please reenter")
        card = input("What card do you wish to place?")

    if card in player_deck:
        while card[0] != center_card[0] and card[1] != center_card[1] and card != 'd':
            card = input("This card is not valid, please reenter")
        player_deck.remove(card)
        center_card = card

    if '+2' in card: 
        center_card = card
        next_turn(player_deck, player1_deck, player2_deck)
        draw_two(player_deck)
        next_turn(player_deck, player1_deck, player2_deck)

    if card[1] == 'R':
        center_card = card
        reverse(card ,player_deck, center_card, player1_deck, player2_deck, deck)
    if 'S' in card:
        center_card = card
        skip(card ,player_deck, center_card, player1_deck, player2_deck, deck)
    
    return card, center_card, player_deck, player1_deck, player2_deck


def draw_two(player_deck, player1_deck, player2_deck, deck):
    for i in range(2):
        draw_one(player_deck, player1_deck, player2_deck, deck)

def draw_one(player_deck, player1_deck, player2_deck, deck):
    who = int(input('Which player is going to draw 2?'))
    if who == 1: 
        player_deck = player1_deck
    else: 
        player_deck = player2_deck
    player_deck += deck[random.randint(0,104)]
    return player_deck

def draw_five(player_deck, player1_deck, player2_deck, deck, center_card):
    for i in range(5):
        draw_one(player_deck, player1_deck, player2_deck, deck)

def wild_draw_four(player_deck, player1_deck, player2_deck, deck, center_card):
    for i in range(4):
        draw_one(player_deck, player1_deck, player2_deck, deck)
    center_colour = input('what colour do you want to change the center card to?')
    valid = True
    while valid: 
        if center_colour == 'Y':
            center_card[0] = 'Y'
            valid = False
        elif center_colour == 'R':
            center_card[0] = 'R'
            valid = False
        elif center_colour == 'G':
            center_card[0] = 'G'
            valid = False
        elif center_colour == 'B':
            center_card[0] = 'B'
            valid = False
        else: 
            print('Invalid colour, please reenter')
            center_colour = input('what colour do you want to change the center card to?')

def reverse(card ,player_deck, center_card, player1_deck, player2_deck, deck): 
        next_turn(player_deck, player1_deck, player2_deck)
        next_turn(player_deck, player1_deck, player2_deck)

def skip(card ,player_deck, center_card, player1_deck, player2_deck, deck):
    next_turn(player_deck, player1_deck, player2_deck)
    next_turn(player_deck, player1_deck, player2_deck)
    

def check_win(player_deck, player1_deck, player2_deck, deck):
    whos_turn(player_deck, player1_deck, player2_deck, deck)
    if player_deck == player1_deck and player_deck == 0: 
        print('Player 1 has won!')
        return True
    elif player_deck == player2_deck and player_deck == 0: 
        print('Player 2 has won!') 
        return True
    else: 
        return False





def main(player_deck, player1_deck, player2_deck, deck):
    center_card = deck[deck[random.randint(0,104)]]
    while '+2' in center_card or center_card[1] == 'R' or 'S' in center_card:
        center_card = deck[deck[random.randint(0,104)]]
    player1_deck = distribute_cards(7,deck)
    player2_deck = distribute_cards(7,deck)
    print(player1_deck)
    print(player2_deck)
    while check_win(player_deck, player1_deck, player2_deck, deck)  == True: 
        player_deck = whos_turn(player_deck, player1_deck, player2_deck, deck)
        center_card, card, player1_deck, player2_deck, player_deck = play_card(player_deck, center_card, player1_deck, player2_deck, deck)
        next_turn(player_deck, player1_deck, player2_deck)







player_deck = []
player2_deck = []
player1_deck = []
main(player_deck, player1_deck, player2_deck, deck)