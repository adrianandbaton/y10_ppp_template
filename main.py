import random
import os

deck = ['R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6','R7', 'R8', 'R9', 'R+2', 'RS', 
'Y0', 'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6','Y7', 'Y8', 'Y9', 'Y+2', 'YS',
'G0', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6','G7', 'G8', 'G9', 'G+2', 'GS',
'B0', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6','B7', 'B8', 'B9', 'B+2', 'BS',
'R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6','R7', 'R8', 'R9', 'R+2', 'RS', 
'Y0', 'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6','Y7', 'Y8', 'Y9', 'Y+2', 'YS',
'G0', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6','G7', 'G8', 'G9', 'G+2', 'GS',
'B0', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6','B7', 'B8', 'B9', 'B+2', 'BS', 'WD4', 'WD4']
random.shuffle(deck)
flipped_deck = ['O0', 'O1', 'O2', 'O3', 'O4', 'O5', 'O6','O7', 'O8', 'O9', 'O+2', 'OS', 
'Y0', 'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6','Y7', 'Y8', 'Y9', 'Y+2', 'YS',
'G0', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6','G7', 'G8', 'G9', 'G+2', 'GS',
'B0', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6','B7', 'B8', 'B9', 'B+2', 'BS',
'R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6','R7', 'R8', 'R9', 'R+2', 'RS', 
'Y0', 'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6','Y7', 'Y8', 'Y9', 'Y+2', 'YS',
'G0', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6','G7', 'G8', 'G9', 'G+2', 'GS',
'B0', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6','B7', 'B8', 'B9', 'B+2', 'BS', 'WD4', 'WD4']


def introduction():
    os.system('clear')
    print("Welcome to UNO!")
    print()
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
    else:
        print("OK, let's start")
def draw_card(player_deck, deck, number):
    for i in range(number):
        x = deck.pop(0)
        player_deck.append(x)
    return x,deck

    return player_deck
def next_turn():
    print("Please pass the laptop to another person")
    ready = input("Has the laptop been passed? (Y/N)")

    while ready.upper() != 'Y':
        print("Ok Bro, has it been passed now?")
    
    os.system('clear')
def play_card(main_deck, other_deck, deck, center_card, main_player, other_player):
    print("Center card is {}".format(center_card))
    repeat = False
    print("It is now {}'s turn!".format(main_player))
    print("This is your deck: ")
    print(main_deck)
    
    card = input("Which card would you like to place, press d to draw: ")

    while card not in main_deck and card != 'd':
        print("That card is not in your deck")
        card = input("Which card would you like to place, press d to draw: ")

    if card in main_deck:
        while card[0] != center_card[0] and card[1] != center_card[1]:
            print("{} cannot be placed. Please enter again: ".format(card))
            card = input("Which card would you like to place, press d to draw: ")

            if card == 'd':
                break
        print("{} is successfully placed".format(card))
        center_card = card
    
    if card == 'd':
        card_drawn, deck = draw_card(main_deck, deck, 1)
        print("You have drawn the card {}".format(card_drawn))
    
    if "+2" in card:
        print("Since you placed a +2 card, 2 cards are added to {}'s deck".format(other_player))
        card_drawn, deck = draw_card(other_deck, deck, 2)
    
    if "S" in card:
        print("Since you have drawn the skip card, {}'s turn is skipped.".format(other_player))
        repeat = True
        
    if repeat == True:
        play_card(main_deck, other_deck, deck, center_card, main_player, other_player)
    

def main(deck):

    introduction()
    print()
    player1_deck = []
    player2_deck = []
    card_drawn, deck = draw_card(player1_deck, deck, 7)
    crd_drawn, deck = draw_card(player2_deck, deck, 7)

    player1 = input("Player 1, enter your name: ")
    player2 = input("Player 2, enter your name: ")
    center_card = deck.pop(0)

    first = input("Who wants to go first?")
    while first != player1 and first != player2:
        print("Bro really? Not funny")
        first = input("Who wants to go first?")
    
    if first == player1:
        while len(player1_deck) != 0 and len(player2_deck) != 0:
            play_card(player1_deck, player2_deck, deck, center_card, player1, player2)
            next_turn()
            play_card(player2_deck, player1_deck, deck, center_card, player2, player1)
            next_turn
    
    elif first == player2:
        while len(player1_deck) != 0 and len(player2_deck) != 0:
            play_card(player2_deck, player1_deck, deck, center_card, player2, player1)
            next_turn()
            play_card(player1_deck, player2_deck, deck, center_card, player1, player2)
            next_turn
    
    if len(player1_deck) == 0:
        print("Congrats, {} won!!!".format(player1))
    else:
        print("What an unexpected turn of events, who would have believes that {} won???".format(player2))
        print("GGs")

main(deck)