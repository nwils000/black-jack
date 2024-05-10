import random

# Class that stores all of the cards in a deck
class Deck:
    suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
    ranks = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
    values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}

# Loops over suits and ranks and creates Cards for all of them
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

# Class that handles each players hand
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
    
    def reset_hand(self):
        self.cards = []
        self.hand_value = 0

# Class that handles storing card information
class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.value = value
        self.rank = rank

    def __repr__(self):
        return f"{self.rank} of {self.suit}"
    
# Class that handles all Player specific information
class Player:
    def __init__(self, name, hand, money=0, bet=0):
        self.name = name
        self.initial_money = money
        self.money = money
        self.bet = bet
        self.hand = hand

    def hit(self, deck):
        new_card = deck.deal_card()
        self.hand.add_card(new_card)

    def show_hand(self):
        return self.hand.cards

class Dealer(Player):
    def __init__(self, hand):
        super().__init__("Dealer", hand)

# Class that handles starting the game and logic that persists between rounds
class Game:
    def __init__(self):
        self.dealer = Dealer(Hand())
        self.players = []
        self.continue_playing = True
        self.starting_money = 0
        self.setup_players()
        self.play()
        
        # Loops over the amount of players and based on the input creates individual player Classes
    def setup_players(self):
        print("")
        self.amount_of_players = input("How many players? ")
        print("")
        for i in range(1, int(self.amount_of_players) + 1):
            players_name = input(f"Player {i}, what's your name? ")
            money = input(f"How much money do you have tonight? ")
            print("")
            self.players.append(Player(players_name, Hand(), int(money)))

# Unless they don't say yes in ask_for_another_round() it'll keep creating rounds
    def play(self):
        while self.continue_playing:
            round = Round(self.dealer, self.players)
            round.start_game()
            self.update_scores(round)
            self.show_scores()

            self.continue_playing = self.ask_for_another_round()

        self.end_game()

# Update the players money after the round ends
    def update_scores(self, round):
        for player in self.players:
            if player not in round.players_who_lost:
                player.money += int(player.bet) * 2
            else:
                player.money -= int(player.bet)

    def show_scores(self):
        print("")
        print("")
        for player in self.players:
            print(f"{player.name}s total money left is {player.money}")
             
    def ask_for_another_round(self):
        print("")
        response = input("Would you like to play another round? (Yes or No) ").lower()
        if response == "yes":
            return True
        else:
            return False
    
    def end_game(self):
        print("")
        print("Game over!")

# Class that handles individual round logic
class Round:
    def __init__(self, dealer, players):
        self.dealer = dealer
        self.players = players
        self.players_who_lost = []
        self.players_who_stood = []
        self.amount_of_decks = int(input("How many decks do you want to shuffle? "))
        # New deck per round
        self.deck = Deck(self.amount_of_decks)
        self.deck.shuffle()
        for player in self.players:
            player.hand.reset_hand()
        self.dealer.hand.reset_hand()

    def start_game(self):
        print("")
        print("Starting Game...")
        player_to_remove = "none"
        # Gets the players bets
        for player in self.players:
            print("")
            player.bet = input(f"{player.name}, you have {player.money} how much money do you want to bet this round? ")
            if int(player.money) < int(player.bet) or int(player.money) == 0:
                print("")
                print(f"Sorry {player.name}, I guess you're too broke to play...")
                player_to_remove = player

        # Doesn't allow broke players to play
        if player_to_remove != "none":
            self.players.remove(player_to_remove)
        
        # Ends game if there are no players with money left
        if len(self.players) == 0:
            print("")
            print("Game over!")
            quit()

        self.dealer.hit(self.deck)
        self.dealer.hit(self.deck)
        print("")
        print("")
        print("")
        print("")
        print(f"Dealer's face up card is {self.dealer.show_hand()[0]}")
        print("")

        # Sets up for the players turns
        for player in self.players:
            player.hit(self.deck)
            player.hit(self.deck)
            print("")

            if player.hand.calculate_hand_total() == 21:
                print(f"{player.name}, you got lucky. BLACKJACK!")
                self.players_who_stood.append(player)
            else:
                print(f"{player.name}'s starting hand: {player.show_hand()}")
                self.players_turn(player)

        self.dealers_turn()
        self.check_if_players_who_stood_won()

    # Lets the players hit if they want or if they haven't busted
    def players_turn(self, player):
        did_player_hit = input(f"{player.name}, would you like to hit? (Yes or No) ").lower()

        while did_player_hit == "yes":
            player.hit(self.deck)
            print(f"{player.name}, your new hand is {player.show_hand()}")
            if self.check_if_bust_on_hit(player) == "bust":
                self.players_who_lost.append(player)
                break
            did_player_hit = input(f"{player.name}, would you like to hit again? (Yes or No) ").lower()

        if did_player_hit == "no":
            print(f"{player.name} stands with {player.show_hand()}")
            self.players_who_stood.append(player)
            print("")

    def dealers_turn(self):
        while self.dealer.hand.calculate_hand_total() < 17:
            self.dealer.hit(self.deck)

    # Checks if the player busted or got blackjack
    def check_if_bust_on_hit(self, player):
        players_cards = player.show_hand()
        players_hand_value = player.hand.calculate_hand_total()
        if players_hand_value > 21:
            print(f"{player.name} drew a {players_cards[-1]} and busted with a total of {players_hand_value}")
            self.players_who_lost.append(player)
            return "bust"
        elif players_hand_value == 21:
            print("")
            print(f"{player.name} has Blackjack with {players_cards}!")
            self.players_who_stood.append(player)
            return "blackjack"
        else:
            return "continue"

    # If players havent busted or got black jack it checks their cards against the dealer
    # If they lost or drew it adds them to the players that lost
    def check_if_players_who_stood_won(self):
        dealers_cards = self.dealer.show_hand()
        dealers_hand_value = self.dealer.hand.calculate_hand_total()
        for player in self.players:
            if player in self.players_who_lost:
                continue
            players_hand_value = player.hand.calculate_hand_total()
            if dealers_hand_value > 21:
                print("")
                print(f"Dealer drew a {dealers_cards[-1]} and busted with a total of {dealers_hand_value}! {player.name}, you win with a total of {players_hand_value}!")
            elif dealers_hand_value == 21:
                print("")
                print(f"Dealer has Blackjack with {dealers_cards}! Sorry {player.name}, you lose...")
                self.players_who_lost.append(player)
            elif dealers_hand_value == players_hand_value:
                print("")
                print(f"Sorry {player.name}... it's a draw. Dealer has {dealers_hand_value} and you have {players_hand_value}")
                self.players_who_lost.append(player)
            elif players_hand_value > dealers_hand_value:
                print("")
                print(f"{player.name}, you win with a total of {players_hand_value}! Dealer has {dealers_hand_value}.")
            else:
                print("")
                print(f"Sorry {player.name}, you lose with a total of {players_hand_value}. Dealer has {dealers_hand_value}.")
                self.players_who_lost.append(player)


new_game = Game()
new_game

# Bug to fix is draws subtract your money