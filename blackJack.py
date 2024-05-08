import random

def show_random_suits_first_card(deck):
    randomNumber = random.randint(1, 4)
    if randomNumber == 1:
        return deck["hearts"].pop(0)
    elif randomNumber == 2:
        return deck["diamonds"].pop(0)
    elif randomNumber == 3:
        return deck["spades"].pop(0)
    elif randomNumber == 4:
        return deck["clubs"].pop(0)

class Hand:
    def shuffle_deck(self):
        random.shuffle(self.deck["hearts"])
        random.shuffle(self.deck["diamonds"])
        random.shuffle(self.deck["spades"])
        random.shuffle(self.deck["clubs"])

    def __init__(self):
        self.deck = {
        "hearts": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
        "diamonds": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
        "spades": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
        "clubs": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
        }
        self.shuffle_deck()
        

    def hit(self):
        return show_random_suits_first_card(self.deck)
    
currentPlayer = Hand()

dealer = Hand()

print("fulldeck", dealer.deck)
print("currentCard", dealer.hit())
print("fulldeck", dealer.deck)
print("currentCard", dealer.hit())
print("fulldeck", dealer.deck)
print("currentCard", dealer.hit())
print("fulldeck", dealer.deck)
print("currentCard", dealer.hit())
print("fulldeck", dealer.deck)
print("currentCard", dealer.hit())
print("fulldeck", dealer.deck)
print("currentCard", dealer.hit())
print("fulldeck", dealer.deck)
print("currentCard", dealer.hit())
print("fulldeck", dealer.deck)
print("currentCard", dealer.hit())
print("fulldeck", dealer.deck)
print("currentCard", dealer.hit())
print("fulldeck", dealer.deck)
print("currentCard", dealer.hit())
print("fulldeck", dealer.deck)
print("currentCard", dealer.hit())
print("fulldeck", dealer.deck)
print("currentCard", dealer.hit())
print("fulldeck", dealer.deck)
print("currentCard", dealer.hit())
print("fulldeck", dealer.deck)
print("currentCard", dealer.hit())
print("fulldeck", dealer.deck)
print("currentCard", dealer.hit())
print("fulldeck", dealer.deck)
print("currentCard", dealer.hit())