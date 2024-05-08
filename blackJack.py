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
    
def checkIfBust(cards_total):
    if cards_total > 21:
        return "BUST!"
    elif cards_total == 21:
        return "BLACKJACK!"
    else:
        return "UNDER!"

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
        self.cards_total = 0
        self.shuffle_deck()
        

    def hit(self, who=""):        
        popped_card = show_random_suits_first_card(self.deck)

        if popped_card == 11:
            self.cards_total += popped_card - 1
        elif popped_card == 12:
            self.cards_total += popped_card - 2
        elif popped_card == 13:
            self.cards_total += popped_card - 3
        else:
            self.cards_total += popped_card
        
        if who == "player":
            if checkIfBust(self.cards_total) == "BUST!":
                print(f"BUST! You got {self.cards_total}... loser")
                quit()
            elif checkIfBust(self.cards_total) == "BLACKJACK!":
                print("BLACKJACK! Collect your winning!")
                quit()
            
        if who == "dealer":
            if self.cards_total > 17:
                if checkIfBust(self.cards_total) == "BUST!":
                    print(f"YOU WIN! Dealer busted with {self.cards_total}")
                    quit()
                elif checkIfBust(self.cards_total) == "BLACKJACK!":
                    print("Dealer got blackjack! Good luck next time")
                    quit()
                else:
                    return "compare"             
            else:
                self.hit("dealer")

        return popped_card

dealer = Hand()
player = Hand()

have_they_hit = ""

def handleNextHit(did_they_hit):
    if did_they_hit.lower() == "yes":
        player.hit("player")
        print("Your current total: ", player.cards_total)
        have_they_hit = input("hit? (Yes or No) ")
        handleNextHit(have_they_hit)
    else:
        print(dealer.hit("dealer"))
        if dealer.hit("dealer") == "compare":
            if(player.cards_total > dealer.cards_total):
                print(f"YOU WIN! Dealer had {dealer.cards_total}, and you had {player.cards_total}")
            if(player.cards_total < dealer.cards_total):
                print(f"YOU LOSE! Dealer had {dealer.cards_total}, and you had {player.cards_total}")
            else:
                print(f"Sorry, its a tie... Dealer had {dealer.cards_total}, and you had {player.cards_total}")


def startGame(dealer, player):
    print("Dealers card: ", dealer.hit())

    print("Your first card is: ", player.hit())
    print("Your second card is: ", player.hit())
    
    have_they_hit = input("hit? (Yes or No) ")
    handleNextHit(have_they_hit)

print("Lets play some Blackjack!")

startGame(dealer, player)
