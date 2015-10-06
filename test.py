# -*- coding: cp1252 -*-
#------------------------------------------------
#------------------------------------------------
#-----------EXPLANATION PROGRAMME----------------
#------------------------------------------------
# 1. CARDDECK = Define carddeck - number of card decks
# 2. DEAL CARDS = Draw cards from the carddeck
# 3. POKERRANKS = Check dealt cards for combinations
# 4. DIDIWIN = Check if player 1 has won
#------------------------------------------------
#-----------POKERRANKS---------------------------
#------------------------------------------------
#Check for possible combinations
#1 Check for pairs, 3 of a kind, carre, 2 pairs, full house
#2 Check for Flush
#3 Check for Straight
#4 Flush + Straight = Straight Flush
#5 If none of the above - check for high card
#------------------------------------------------
#1 - HIGH CARD
#2 - ONE PAIR
#3 - TWO PAIRS
#4 - THREE OF A KIND
#5 - STRAIGHT
#6 - FLUSH
#7 - FULL HOUSE
#8 - FOUR OF A KIND
#9 - STRAIGHT FLUSH
#------------------------------------------------
#--------------DEAL CARDS------------------------
#------------------------------------------------
#drawn_cards = draw_cards(3, 1)
#my_cards = drawn_cards[5:7]
#flop = drawn_cards[0:3]
#turn = drawn_cards[3]
#river = drawn_cards[4]
#other_players = drawn_cards[7:]
#cards_in_play = drawn_cards[0:7]
#------------------------------------------------
#--------------IMPORT MODULES--------------------
#------------------------------------------------
import random
#------------------------------------------------
#-------------CARD DECK--------------------------
#------------------------------------------------
def carddeck(number_decks):
    n = 0
    cards = ['01c','02c','03c','04c','05c','06c','07c','08c','09c','10c','11c',\
             '12c','13c','01d','02d','03d','04d','05d','06d','07d','08d','09d',\
             '10d','11d','12d','13d','01s','02s','03s','04s','05s','06s','07s',\
             '08s','09s','10s','11s','12s','13s','01h','02h','03h','04h','05h',\
             '06h','07h','08h','09h','10h','11h','12h','13h']
    cards1 =[]
    while n<number_decks:
        cards1 = cards1+cards
        n=n+1
    return cards1
#------------------------------------------------
#-------------DRAW CARDS-------------------------
#------------------------------------------------
# n = number of players
# p = number of carddecks
# f = number of cards to draw for texas hold'em
def draw_cards(n, p):
    cards = carddeck(p)
    f = 5 + n*2
    a = random.sample(cards, f)
    return a
#print drawn_cards
#print ''
#print cards_in_play
#print ''
#print other_players
#print ''
#------------------------------------------------
#-------------POKERRANKS-------------------------
#------------------------------------------------
#------------------------------------------------
#5 Check for Highest Cards
#------------------------------------------------
def fivehighestcards(cards):
    print cards
    cards.sort()
    a = len(cards)
    b = len(cards)-5
    return cards[b:a]
#drawn_cards = draw_cards(3, 1)
#print drawn_cards
#print fivehighestcards(drawn_cards)