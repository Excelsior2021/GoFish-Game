'''Card Functions for Deck of Cards'''

non_num_cards = ['ace', 'jack', 'queen', 'king']
suits = ['clubs', 'diamonds', 'hearts', 'spades']

def choose_suit(deck, suit=None):
    '''Returns a list of cards specified by suit.
    if no suit is provided, the full deck is returned.'''
    list = []
    if suit:
        suit.lower()
        for x in deck:
            if suit.title() in x:
                list.append(x)
    else:
        return deck
    return list

def get_suit(card):
    '''Returns the suit of a the card.'''
    card = card.lower()
    for x in suits:
        if x in card:
            return x.title()

def get_value(card):
    '''Returns the value of a card.'''
    for x in range(2,11):
        if str(x) in card:
            return x
    for x in non_num_cards:
        if x.title() in card:
            return x.title()

def same_value(card1, card2, card3=None, card4=None):
    '''Returns True if up to four cards have the same value. 
        At least two cards need to be passed into the function.'''
    if card3 and card4:
        return get_value(card1) == get_value(card2) == get_value(card3) == get_value(card4)
    elif card3:
        return get_value(card1) == get_value(card2) == get_value(card3)
    else:
        return get_value(card1) == get_value(card2)

def same_suit(card1, card2, card3=None, card4=None):
    '''Returns True if at least four cards have the same suit. 
        At least two cards need to be passed into the function.'''
    if card3 and card4:
        return get_suit(card1) == get_suit(card2) == get_suit(card3) == get_suit(card4)
    elif card3:
        return get_suit(card1) == get_suit(card2) == get_suit(card3)
    else:
        return get_suit(card1) == get_suit(card2)