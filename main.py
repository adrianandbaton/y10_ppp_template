import  random
cards = ['R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6','R7', 'R8', 'R9', 'R+2', 'RS', 'RR', 
         'Y0', 'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6','Y7', 'Y8', 'Y9', 'Y+2', 'YS', 'YR',
         'G0', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6','G7', 'G8', 'G9', 'G+2', 'GS', 'GR',
         'B0', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6','B7', 'B8', 'B9', 'B+2', 'BS', 'BR',]
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


def distribute_cards(deck):
    player_deck = []
