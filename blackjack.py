#Blackjack game
import random
import time

player = []
dealer = []
card_types = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] 

#generate random deck
def make_deck(card_types):
    new_deck = []
    for i in range(4):
        new_deck.extend(card_types)
    random.shuffle(new_deck)
    return new_deck


#give player and dealer cards
def hands(deck):
    for i in range(2):
        player.append(deck[i])
        dealer.append(deck[i + 2])

def hand_value(player):
    value = 0
    ace_11 = 0
    for card in player:
        if card == 'Q' or card == 'J' or card == 'K':
            value += 10
        elif card in range(11):
            value += card
        else:
            value += 11
            ace_11 += 1
    while ace_11 > 0 and value > 21:
        value -= 10
        ace_11 -= 1
    return value




def main():
    deck = make_deck(card_types)
    hands(deck)
    player_value = hand_value(player)
    
    print(f"You have {player} with a total value of {player_value}")
    print(f"The dealer has got {dealer[0]} & X")
    
    #player needs to stay or hit after that the dealer continues
    while True:
        #Asking user if he wants to hit or stay
        next = input("What would you like to do next(Hit/Stay)? ")
        
        #if hit than add the next card in the deck to the players hand and calc score
        if next.lower() == "hit":
            i = len(player) + len(dealer) #determine which card in the deck is next
            player.append(deck[i])
            player_value = hand_value(player)
            print(f"Now you have {player} with a total value of {player_value}")
            time.sleep(1)

            #if the score is over 22 he loses
            if player_value > 21:
                print(f"It looks like you lost the game because your score is over 22.")
                return
        elif next.lower() == "stay":
            break

    dealer_value = hand_value(dealer)
    print(f"Now its the dealers turn: With his hidden card he has {dealer} with a total value of: {dealer_value}")
    time.sleep(1)
    while dealer_value < 17:
        j = len(player) + len(dealer)
        dealer.append(deck[j])
        dealer_value = hand_value(dealer)

        if dealer_value > 21:
            print(f"Dealer had to bust with {dealer} and a score of {dealer_value}, you won!")
            return

    print(f"Your score is {player_value}")
    time.sleep(1)
    print(f"The dealers value is {dealer_value} with {dealer}")
    time.sleep(1)
    if player_value > dealer_value:
        print("You won!")
    elif dealer_value > player_value:
        print("The Dealer has won")
    else:
        print("Its a tie")


    
        









main()