from audioop import reverse
from multiprocessing.sharedctypes import Value
from optparse import Values
import random
from itertools import combinations
from collections import defaultdict

#suits : clubs, hearts, spades, diamonds
#hands: card, pair, 2 pairs, 3 of a kind, straight, flush, full house, 4 of a kind, straight flush, royal flush

class Card(object):
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        cards_name = {10: "T", 11:"J", 12:"Q", 13:"K", 14:"A"}
        name = str(self.value) if self.value < 10 else cards_name[self.value]
        return name + str(self.suit)

class Deck(object):
    def __init__(self):
        self.cards = self.shuffled_deck()

    def shuffled_deck(self):
        cards = [Card(v, s) for s in '♤♡♧♢' for v in range(2, 15)]
        random.shuffle(cards)
        return cards

    def give(self, num):
        return [self.cards.pop() for i in range(num)]
        
    
class Player(object):
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

def best_five(hand, board):
    seven_cards = hand + board
    best_rang = -1
    seven_cards = sorted(seven_cards, key=lambda k: k.value, reverse = True)
    for five_cards in combinations(seven_cards, 5):
        rang, cards = score5(five_cards)
        if rang > best_rang:
            best_rang = rang
            best_cards = cards
    return best_rang, best_cards


def score5(cards_5):
    consec_cards = defaultdict(list)
    cards_value = defaultdict(list)
    for k in cards_5:
        cards_value[k.value].append(k)
    for v in cards_value.values():
        consec_cards[len(v)] += v

    value = {k.value for k in cards_5}
    straight = (len(value) == 5 and max(value) - min(value) == 4) or \
               value == {5,4,3,2,14} 

    suit = {k.suit for k in cards_5}
    flush = len(suit) == 1
    
    #Royal Flush
    if flush and straight and min(value) == 10:
        return 9, cards_5

    #Straight Flush
    if straight and flush:
        if value == {5,4,3,2,14}:
            cards_5 = cards_5[1:] + cards_5[:1]
        return 8, cards_5
    
    #Four of a kind
    if 4 in consec_cards:
        return 7, consec_cards[4] + consec_cards[1]

    #Full House
    if 3 in consec_cards and 2 in consec_cards:
        return 6, consec_cards[3] + consec_cards[2]

    #Flush
    if flush:
        return 5, cards_5

    #Straight
    if straight:
        if value == {5,4,3,2,14}:
            cards_5 = cards_5[1:] + cards_5[:1]
        return 4, cards_5

    #Three of a kind
    if 3 in consec_cards and 1 in consec_cards:
        return 3, consec_cards[3] + consec_cards[1]

    #Two Pair
    if 2 in consec_cards and len(consec_cards[2]) == 4:
        return 2, consec_cards[2] + consec_cards[1]

    #One Pair
    if 2 in consec_cards:
        return 1, consec_cards[2] + consec_cards[1]

    #High Card
    return 0, cards_5


result = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

for i in range(100000):
    deck = Deck()
    pocket = deck.give(2)
    board = deck.give(5)
    rang, cards = best_five(pocket, board)
    result[rang] += 1

print(result)

