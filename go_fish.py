'''A simulation of an adaptation of the card game Go Fish.'''

from go_fish_functions import *

#Deck is created and shuffled. Hands are dealt to players.
deck = create_deck()
deck = shuffle_deck(deck)
player1_cards = deal_hand(deck, 7)
player2_cards = deal_hand(deck, 7)

#Original cards dealt to players.
print(f'Player1 original hand: {player1_cards}\n')
print(f'Player2 original hand: {player2_cards}\n')

#Inital pairs before players start.
player1_pairs = pairs(player1_cards)
player2_pairs = pairs(player2_cards)

#Loop of game. Players taking turns based on rules.
while len(deck) > 0 and len(player1_cards) > 0 and len(player2_cards) > 0:
    #player1 turn.
    player1_ask = ask_value(player1_cards, player2_cards, player1_pairs)
    again(player1_cards, player2_cards, player1_pairs)
    player1_dealed = deal_card(player1_cards, player2_cards, player1_pairs, deck)
    again(player1_cards, player2_cards, player1_pairs)

    #player2 turn.
    player2_ask = ask_value(player2_cards, player1_cards, player2_pairs)
    again(player2_cards, player1_cards, player2_pairs)
    player2_dealed = deal_card(player2_cards, player1_cards, player2_pairs, deck)
    again(player2_cards, player1_cards, player2_pairs)

print(f'Player1 pairs: {player1_pairs}\n')
print(f'Player2 pairs: {player2_pairs}\n')

print(f'Player1 cards left: {player1_cards}\n')
print(f'Player2 cards left: {player2_cards}\n')

print(f'Deck remaining: {len(deck)}\n')

if len(player1_pairs) > len(player2_pairs):
    print(f'Player1, you win! Well done!')
elif len(player2_pairs) > len(player1_pairs):
    print(f'Player2, you win! Well done!')
else:
    print(f"It's a draw!")

print(f'\nCards: {len(player1_pairs)+len(player2_pairs)+len(player1_cards)+len(player2_cards)+len(deck)}')
