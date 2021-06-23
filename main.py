#black jack

import random
from art import logo
import os
from time import sleep
gameover = False
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# test deck
#cards = [11, 11, 11, 11, 11, 11, 10, 10, 10, 10, 10, 10, 10]

def clear_screen():
    # It is for MacOS and Linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # It is for Windows platfrom
        _ = os.system('cls')

#function for drawing cards
def random_card():
  random_num = random.randint(0, 12)
  chosen_card = int(cards[random_num])
  return(chosen_card)

#detrmie if ace should be 1 or 11
def ace(hand):
  if 11 in hand and sum(hand) > 21:
    index = hand.index(11)
    hand[index] = 1
    return(hand)
  else:
    return(hand)

def blackjack():
  global gameover
  while gameover == False:
    print(logo)
    dealers_cards = []
    players_cards = []

    #fisrt round of dealing
    dealers_cards.append(random_card())
    players_cards.append(random_card())
    dealers_cards.append(random_card())
    players_cards.append(random_card())
    dealers_cards = ace(dealers_cards)
    players_cards = ace(players_cards)

    #statement displayed at the end of every game
    def final_count():
      print(f"Your hand is {players_cards} for a total of {sum(players_cards)}. \nDealers hand is {dealers_cards} for a total of {sum(dealers_cards)}.")


    # checking for first round winner
    if sum(dealers_cards) == 21:
      print(f"Dealer wins...")
      final_count()
      cont = input("Would you like to play a new game of black jack? Type y for yes and n for no: ")
      if cont == "y":
        clear_screen()
        blackjack()
      else:
        gameover = True
        break
    elif sum(players_cards) == 21 and sum(dealers_cards) != 21:
      print(f"You Win!")
      final_count()
      cont = input("Would you like to play a new game of black jack? Type y for yes and n for no: ")
      if cont == "y":
        clear_screen()
        blackjack()
      else:
        gameover = True
        break
    else:
      print(f"Dealer's showing card is {dealers_cards[0]}.\nYour hand is {players_cards} for a total of {sum(players_cards)}.")


      #player drawing
    draw = input("Would you like to draw a card? Type y for yes and n for no:  ")
    if draw == "y":
      drawing = True
      while drawing:
        players_cards.append(random_card())
        players_cards = ace(players_cards)
        print(f"Your hand is {players_cards} for a total of {sum(players_cards)}.")
        draw = input("Would you like to draw a card? Type y for yes and n for no:  ")
        if draw == "n":
          drawing = False

    #dealer draws
    while sum(dealers_cards) < 16:
      dealers_cards.append(random_card())
      dealers_cards = ace(dealers_cards)
      print(f"Dealer drew a card")


    #show hands
    if sum(players_cards) > 21:
      print(f"\nYou lose... you went over 21 ")
      final_count()
    elif sum(dealers_cards) > 21 and sum(players_cards) <= 21:
      print(f"\nYou Win! The dealer went over 21")
      final_count()
    elif (sum(dealers_cards)) == (sum(players_cards)):
      print(f"\nTie... You have the same amount of cards as the dealer.")
      final_count()
    elif sum(dealers_cards) < sum(players_cards):
      print(f"\nYou Win! You got closer to 21.")
      final_count()  
    elif sum(dealers_cards) > sum(players_cards):
      print(f"\nYou Lose... The dealer got closer to 21.") 
      final_count()

    cont = input("Would you like to play a new game of black jack? Type y for yes and n for no: ")
    if cont == "y":
      clear_screen()
      blackjack()
    else:
      gameover = True
      break

blackjack()




