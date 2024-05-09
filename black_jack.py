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
                    self.cards.append(Card(suit, rank, self.values[rank]))

    def __repr__(self):
        return f"{self.cards}"

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop(0)

class Hand:
    def __init__(self):
        self.cards = []
        self.hand_value = 0

    def add_card(self, card):
        self.cards.append(card)

    def calculate_hand_total(self):
            total = 0
            ace_count = 0
            for card in self.cards:
                total += card.value
                if card.rank == "Ace":
                    ace_count += 1
                    
            while total > 21 and ace_count > 0:
                total -= 10
                ace_count -= 1

            return total

class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.value = value
        self.rank = rank

    def __repr__(self):
        return f"{self.rank} of {self.suit}"
    
class Player:
    def __init__(self, name, hand, money=0):
        self.name = name
        self.money = money
        self.hand = hand

    def hit(self, deck):
        new_card = deck.deal_card()
        self.hand.add_card(new_card)

    def show_hand(self):
        return self.hand.cards

class Dealer(Player):
    def __init__(self, hand):
        super().__init__("Dealer", hand)

class Game():
    def __init__(self):
        self.dealer = Dealer(Hand())
   
        self.amount_of_decks = input("How many decks do you want to shuffle? ")
        self.deck = Deck(self.amount_of_decks)
        self.deck.shuffle()
        
        self.players = []
        self.players_who_already_lost = []
        self.amount_of_players = input("How many players? ")
        for i in range(1, int(self.amount_of_players) + 1):
            players_name = input(f"player{i}, whats your name? ")
            players_money = input(f"Okay {players_name}, how much money are you betting? ")
            self.players.append(Player(players_name, Hand(), players_money))

        self.start_game()

    def start_game(self):
        print("Starting Game...")
        self.dealer.hit(self.deck)
        self.dealer.hit(self.deck)
        print(f"Dealers face up card is {self.dealer.show_hand()[0]}")

        for i in range(int(self.amount_of_players)):
            self.players[i].hit(self.deck)
            self.players[i].hit(self.deck)
            print(f"{self.players[i].name}s starting hand {self.players[i].show_hand()}")

            if self.players[i].hand.calculate_hand_total() == 21:
                print(f"{self.players[i].name}, you got lucky. BLACKJACK!")
            else:
                self.players_turn(self.players[i])
        
        for loser in self.players_who_already_lost:
            self.players.remove(loser)

        self.dealers_turn()
        self.check_if_players_who_stood_won(self.players)
    
    def players_turn(self, player):
            did_player_hit = input(f"{player.name}, would you like to hit? (Yes or No)")
            
            if did_player_hit.lower() == "yes":
                player.hit(self.deck)
                print(f"{player.name}, your new hand is {player.show_hand()}")
                if self.check_if_bust_on_hit(player) == "continue":
                    self.players_turn(player)
            else:
                pass

    def dealers_turn(self):
        while self.dealer.hand.calculate_hand_total() < 17:
            self.dealer.hit(self.deck)

    def check_if_bust_on_hit(self, player):  
        players_cards = player.show_hand()
        players_hand_value = player.hand.calculate_hand_total()
        if players_hand_value > 21:
            print(f"{player.name} drew a {players_cards[-1]} and busted with a total of {players_hand_value}")
            self.players_who_already_lost.append(player)
            return "turn over"
        elif players_hand_value == 21:
            print(f"{player.name} has Blackjack with {players_cards}!")
            self.players_who_already_lost.append(player)
            return "turn over"
        else:
            return "continue"

    def check_if_players_who_stood_won(self, players):
        dealers_cards = self.dealer.show_hand()
        dealers_hand_value = self.dealer.hand.calculate_hand_total()    
        for player in players:        
            players_hand_value = player.hand.calculate_hand_total()     
            if dealers_hand_value > 21:
                print(f"Dealer drew a {dealers_cards[-1]} and busted with a total of {dealers_hand_value}! {player.name}, you win with a total of {players_hand_value}!")
            elif dealers_hand_value == 21:
                print(f"Dealer has Blackjack with {dealers_cards}! Sorry {player.name}, you lose...")
            elif dealers_hand_value == players_hand_value:
                print(f"Sorry {player.name}... it's a draw. Dealer has {dealers_hand_value} and you have {players_hand_value}")
            elif players_hand_value > dealers_hand_value:
                print(f"{player.name}, you win with a total of {players_hand_value}! Dealer has {dealers_hand_value}.")
            else:
                print(f"Sorry {player.name}, you lose with a total of {players_hand_value}. Dealer has {dealers_hand_value}.")
    


new_game = Game()
new_game
    # I'll need to ditribute the deck amongst the amount of players
