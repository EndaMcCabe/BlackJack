import random

'''
These are the values that will be associated to the cards in the game.
'''

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Card:
    
    def __init__ (self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]

    def __str__(self) -> str:
        return self.rank + ' of ' + self.suit

class Deck:

    def __init__(self):

        '''
        This creates the deck by looping through the suits and ranks tuples and creating 52 unique cards which will be our Deck
        '''

        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(rank, suit))

        #This will shuffle the deck
        def shuffle(self):
            random.shuffle(self.all_cards)
        
        #This will remove one Card from the deck acting like a dealer dealing one card
        def deal_one(self) -> object:
            return self.all_cards.pop()

class Player:

    def __init__(self, name):
        
        self.name = name
        self.balance = 100
        self.cards = []

    def __str__(self) -> str:
        return f"Player has {self.balance} left."

    def add_card(self):
        return self.cards.append(deck.deal_one())

me = Player("Me")
print(me)

