import time
import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
start = input("Welcome to blackjack, type 'y' to play.\n")

cards = {
    "Ace": 11,  # Ace can be 11 or 1, will be handled in adjust_ace_value
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
}

#Other improvements I would make include updating the play again logic to use the existing shuffled deck at the end of the game or to use a new (full 52 cards) deck.

starting_deck = list(cards.keys()) * 4

def adjust_ace_value(hand):
    for i, card in enumerate(hand):
        if card == "Ace" and calculate_hand_total(hand) > 21:
            hand[i] = "Ace (1)"  # Marking Ace as 1 for printing
    return hand

def blackjack():
    player_hand = []
    house_hand = []
    shuffled_deck = shuffle_cards(starting_deck)
    
    #Dealing cards
    shuffled_deck, house_hand = deal_card(shuffled_deck, house_hand)    
    shuffled_deck, player_hand = deal_card(shuffled_deck, player_hand)
    
    shuffled_deck, house_hand = deal_card(shuffled_deck, house_hand)  
    shuffled_deck, player_hand = deal_card(shuffled_deck, player_hand)
    
    print("The dealer is dealing cards:")
    time.sleep(1)
    playing = True
    
    while playing:
        if calculate_hand_total(player_hand) <= 21:
            print(f"Your hand: {print_hand(player_hand)}, current score: {calculate_hand_total(player_hand)}")
            print(f"House hand: {print_hand([house_hand[0]])} & X")     
            hit_me = input("Would you like to hit or stay?\n").lower()
            if hit_me == "hit":
                shuffled_deck, player_hand = deal_card(shuffled_deck, player_hand)
                player_hand = adjust_ace_value(player_hand)
            elif hit_me == "stay":
                playing = False
        else:
            playing = False             
    while calculate_hand_total(house_hand) < 17 and calculate_hand_total(player_hand) < 22:
        shuffled_deck, house_hand = deal_card(shuffled_deck, house_hand)
    
    player_final_score = calculate_hand_total(player_hand)
    house_final_score = calculate_hand_total(house_hand)
    print(f"Your hand: {print_hand(player_hand)}, final score: {player_final_score}")
    print(f"House hand: {print_hand(house_hand)}, final score: {house_final_score}")
    if player_final_score > 21:
        print("You busted!:( You lose.")
    elif player_final_score == house_final_score:
        print("You and the house had the same score. You tie.")
    elif player_final_score < house_final_score and house_final_score <=21:
        print("The house beat you. You lose.")
    else:
        print("You beat the house! You win!")
        
def shuffle_cards(deck):
    random.shuffle(deck)
    return deck

def deal_card(deck, hand):
    random.seed(time.time())
    dealt_card = random.choice(deck)
    deck.remove(dealt_card)
    hand.append(dealt_card)
    return deck, hand

def calculate_hand_total(hand):
    total = 0
    for card in hand:
        if card == "Ace (1)":  # Handling the Ace marked as 1
            total += 1
        else:
            total += cards.get(card, 0)  # Get the card's value, defaulting to 0 if not found
    return total

def print_hand(hand):
    return ' & '.join(hand)

def start_game():
    print(logo)
    play_again = True
    while play_again:
        blackjack()
        if input("Would you like to play again? (y/n)\n").lower() != "y":
            print("Thank you for playing, goodbye!")
            play_again = False
            time.sleep(2)
            break
        
if start == 'y':        
    start_game()