import random

# deck = {
#     "hearts": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
#     "diamonds": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
#     "spades": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
#     "clubs": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
# }

# def shuffle_deck():
#     random.shuffle(deck["hearts"])
#     random.shuffle(deck["diamonds"])
#     random.shuffle(deck["spades"])
#     random.shuffle(deck["clubs"])

# shuffle_deck()

# print(deck)

class Hand:
    deck = {
        "hearts": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
        "diamonds": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
        "spades": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
        "clubs": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
    }

    def shuffle_deck(self):
        random.shuffle(self.deck["hearts"])
        random.shuffle(self.deck["diamonds"])
        random.shuffle(self.deck["spades"])
        random.shuffle(self.deck["clubs"])

    def __init__(self):
        self.shuffle_deck()
        self.deck = self.deck

    def shuffle_the_deck(self):
        self.shuffle_deck()
    
currentPlayer = Hand()
print("current", currentPlayer.deck)

dealer = Hand()
print("other", currentPlayer.deck)

