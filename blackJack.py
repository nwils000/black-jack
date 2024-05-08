import random

deck = {
    "hearts": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
    "diamonds": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
    "spades": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
    "clubs": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
}

def shuffle_deck():
    random.shuffle(deck["hearts"])
    random.shuffle(deck["diamonds"])
    random.shuffle(deck["spades"])
    random.shuffle(deck["clubs"])

shuffle_deck()

print(deck)