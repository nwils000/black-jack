import random

class Deck:
    suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
    ranks = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
    values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}

    def __init__(self, amount_of_decks=0):
        self.cards = []
        for _ in range(int(amount_of_decks)):
            for suit in self.suits:
                for rank in self.ranks:
                    self.cards.append([Card(suit, rank, self.values[rank])])

    def shuffle(self):
        random.shuffle(self.cards)

class Hand:
    def __init__(self):
        self.cards = []
        self.hand_value = 0

    def add_card(self, card):
        self.cards.append(card)

    def calculate_hand_total(self):
        for int in self.cards:
            self.hand_value += int

class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.value = value
        self.rank = rank

    def __repr__(self):
        return f"{self.rank} of {self.suit}"
    
class Player:
    def __init__(self, name, money, hand):
        self.name = name
        self.money = money
        self.hand = hand

class Dealer(Player):
    def __init__(self):
        super().__init__(name="Dealer")

class Game():
    def __init__(self):
        amount_of_decks_user_wants = input("How many decks do you want to shuffle?")
        deck = Deck(amount_of_decks_user_wants)
        deck.shuffle
        print(deck.cards)
    

    # Ill need to ditribute the deck amongst the amount of players














# def show_random_suits_first_card(deck):
#     randomNumber = random.randint(1, 4)
#     if randomNumber == 1:
#         return deck["hearts"].pop(0), "Hearts"
#     elif randomNumber == 2:
#         return deck["diamonds"].pop(0), "Diamonds"
#     elif randomNumber == 3:
#         return deck["spades"].pop(0), "Spades"
#     elif randomNumber == 4:
#         return deck["clubs"].pop(0), "Clubs"

# def checkIfBust(cards_total):
#     if cards_total > 21:
#         return "BUST!"
#     elif cards_total == 21:
#         return "BLACKJACK!"
#     else:
#         return "UNDER!"

# class Hand:
#     def shuffle_deck(self):
#         random.shuffle(self.deck["hearts"])
#         random.shuffle(self.deck["diamonds"])
#         random.shuffle(self.deck["spades"])
#         random.shuffle(self.deck["clubs"])

#     def __init__(self):
#         self.deck = {
#         "hearts": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
#         "diamonds": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
#         "spades": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
#         "clubs": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
#         }
#         self.cards_total = 0
#         self.shuffle_deck()
        

#     def hit(self, who=""):        
#         popped_card, suit = show_random_suits_first_card(self.deck)

#         if popped_card == 11:
#             self.cards_total += 10
#         elif popped_card == 12:
#             self.cards_total += 10
#         elif popped_card == 13:
#             self.cards_total += 10
#         else:
#             self.cards_total += popped_card
        
#         if who == "player":
#             if checkIfBust(self.cards_total) == "BUST!":
#                 print(f"BUST! You drew a {popped_card} of {suit} bringing your total to {self.cards_total}... loser")
#                 quit()
#             elif checkIfBust(self.cards_total) == "BLACKJACK!":
#                 print("BLACKJACK! Collect your winnings!")
#                 quit()
#         if popped_card == 11:
#             return f"Jack of {suit}"
#         elif popped_card == 12:
#             return f"Queen of {suit}"
#         elif popped_card == 13:
#             return f"King of {suit}"
#         else:
#             return f"{popped_card} of {suit}"

# dealer = Hand()
# player = Hand()

# have_they_hit = ""

# def handleNextHit(did_they_hit):
#     if did_they_hit.lower() == "yes":
#         print(f"You drew a {player.hit("player")} bringing your total to {player.cards_total}")
#         have_they_hit = input("hit? (Yes or No) ")
#         handleNextHit(have_they_hit)
#     else:
#         while dealer.cards_total < 17:
#             dealer.hit()
#         if dealer.cards_total >= 17:
#             if dealer.cards_total > 21:
#                 print(f"YOU WIN! Dealer busted with {dealer.cards_total}")
#             elif player.cards_total > 21:
#                 print(f"YOU LOSE! You busted with {player.cards_total}")
#             elif dealer.cards_total == 21 and player.cards_total < 21:
#                 print(f"YOU LOSE! The dealer got blackjack and you had {player.cards_total}")
#             elif player.cards_total > dealer.cards_total:
#                 print(f"YOU WIN! Dealer had {dealer.cards_total}, and you had {player.cards_total}")
#             elif player.cards_total < dealer.cards_total:
#                 print(f"YOU LOSE! Dealer had {dealer.cards_total}, and you had {player.cards_total}")
#             else:
#                 print(f"Sorry, it's a tie... Dealer had {dealer.cards_total}, and you had {player.cards_total}")
#         else:
#             dealer.hit()

# def startGame(dealer, player):
#     print(f"The dealer has a {dealer.hit()}")

#     print(f"You have a {player.hit()} and a {player.hit()}")
    
#     have_they_hit = input("hit? (Yes or No) ")
#     handleNextHit(have_they_hit)

# print("Lets play some Blackjack!")

# # Game starts here
# startGame(dealer, player)