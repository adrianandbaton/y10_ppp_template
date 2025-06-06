import random
import os 
deck = ['R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6','R7', 'R8', 'R9', 'R+2', 'RS', 'RR', 
'Y0', 'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6','Y7', 'Y8', 'Y9', 'Y+2', 'YS', 'YR',
'G0', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6','G7', 'G8', 'G9', 'G+2', 'GS', 'GR',
'B0', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6','B7', 'B8', 'B9', 'B+2', 'BS', 'BR',
'R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6','R7', 'R8', 'R9', 'R+2', 'RS', 'RR', 
'Y0', 'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6','Y7', 'Y8', 'Y9', 'Y+2', 'YS', 'YR',
'G0', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6','G7', 'G8', 'G9', 'G+2', 'GS', 'GR',
'B0', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6','B7', 'B8', 'B9', 'B+2', 'BS', 'BR']

random.shuffle(deck)

rules = input('Do you want to review the rules?(Y/N)')
while rules != "N" or rules != "Y":
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

You cannot play after you draw""")


def distribute_cards(number, deck):
    player_deck = []
    for i in range(number):
        x = deck.pop[i]
        player_deck.append(x)

    return player_deck

def next_turn(player_deck, player1_deck, player2_deck):
    valid = True
    while valid:
        turn = int(input("Who's turn is it? Player1 or player2?"))
        if turn == 1: 
            player_deck = player1_deck
            valid = False
        elif turn == 2:
            player_deck = player2_deck
            valid = False
        else: 
            print('Please enter a valid player!')
            turn = int(input("Who's turn is it? Player1 or player2?"))

    ready = input("Has the laptop passed to the next user? (Y?N)")
    while ready.upper() != 'Y':
        ready = input("OK, now has the laptop been passed (Y/N)")
    if ready  == 'Y':
        os.system('clear')

def draw_card(player_deck, deck):
    x = deck[0]
    player_deck.append(x)
    return player_deck

def play_card(player_deck, center_card, deck):
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
        next_turn()
        draw_two(player_deck)

def draw_two(player_deck, deck):
    player_deck += deck[random.randint(0,104)]
    player_deck += deck[random.randint(0,104)]




def main(deck):
    y = 0
    center_card = deck[y]
    while '+2' in center_card or center_card[1] == 'R' or 'S' in center_card:
        center_card = deck[y+1]
    player1_deck = distribute_cards(7,deck)
    player2_deck = distribute_cards(7,deck)
