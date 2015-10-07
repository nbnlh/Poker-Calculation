# -*- coding: cp1252 -*-
#------------------------------------------------
#------------------------------------------------
#-----------EXPLANATION PROGRAMME----------------
#------------------------------------------------
# 1. CARDDECK = Define carddeck - number of card decks
# 2. DEAL CARDS = Draw cards from the carddeck
# 3. POKERRANKS = Check dealt cards for combinations
# 4. DIDIWIN = Check if player 1 has won
#-----------ADDITIONS TO MAKE TO PROGRAMME----------------
# <<<<<<<<<AMMEND 5 HIGHEST CARD CALCULATION>>>>>>>>>>>>>>
# Make calculation for 5 highest cards make sure the combinations are included
# for a pair the pair needs to be included in the 5 highest cards even
# if 5 other cards are higher
# <<<<<<<<<<ADD ENTRY FOR CARDS OF PLAYER 1>>>>>>>>>>>>
# Add the optional addition of cards for player one so that can be calculated
# with user input instead of randomly selected cards
# <<<<<<<<<<ADD CALCULATION STRAIGHT FLUSH>>>>>>>>>>>>
# Add a calculation to give straight+flush higher value than flush
# <<<<<<<<<<CHECK PERCENTAGES>>>>>>>>>>>>
# At the moment the %s dont add up to the correct number
# User input should be taken from the random selection that is made
#------------------------------------------------
# Now Using Github for code sharing :)
#------------------------------------------------
#-----------POKERRANKS---------------------------
#------------------------------------------------
#Check for possible combinations
#1 SAMECARDS - Check for pairs, 3 of a kind, carre, 2 pairs, full house
#2 FLSUH - Check for Flush
#3 STRAIGHT - Check for Straight
#4 Flush + Straight = Straight Flush
#5 FIVE HIGHEST CARDS - If none of the above check for high card
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
def Carddeck(number_decks):
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
def Draw_cards(n, p):
    cards = Carddeck(p)
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
#1 Check for pairs, 3 of a kind, carre, 2 pairs, full house, high card
#------------------------------------------------
def Samecards(cards_played): #Output of is as [Rank, 'Card']
    a= [x[0:2] for x in list(cards_played)]    #Get's the numbers from the cards
    p = [[a.count(x),x] for x in set(a)]
    z = max(p)
    p.remove(z)
    f = max(p)
    if z[0] == 4:
    #    print 'You have Carré'
        return [8, z[1]]
    elif z[0]==3 and f[0]>1:
    #    print 'You have Full House'
        return [7, z[1]]
    elif z[0]==3 and f[0]==1:
        #    print 'You have 3 of a Kind'
        return [4, z[1]]
    elif z[0]==2 and f[0]==2:
    #    print 'You have 2 pair'
        return [3, z[1]]
    elif z[0]==2 and f[0]<2:
    #    print 'You have 1 pair'
        return [2, z[1]]
    else:
    #    print 'You have no pairs'
        return [1, z[1]]
#print samecards(cards_in_play), 'Rank, Card - PLAYER 1'
#hand_pl1 = samecards(cards_in_play)
#------------------------------------------------
#------------------------------------------------
#2 Check for Flush
#------------------------------------------------
def Flush(cards):
    a = [x[2:] for x in list(cards)]
#    print a
    p = [[a.count(x),x] for x in set(a)]
#    print p
    z = max(p)
#    print z
#    print z[0]
    if z[0]==5:
        return [6,0]
    else:
        return []
#drawn_cards = draw_cards(3, 1)
#print drawn_cards
#print flush(drawn_cards)
#------------------------------------------------
#3 Check for Straight
#------------------------------------------------
def Straight(cards):
    a= [x[0:2] for x in list(cards)]    #Get's the numbers from the cards
    f = set(a)                          #Eliminates duplicates
    p = sorted(f)                       #Sorts the set
#    print p
    card2 = len(p)-1
    card1 = card2-1
    v = 0
    while card2>0:
        if int(p[card2])-int(p[card1]) == 1:
            v= v+1
            if v>3:
                return [5,int(p[card2])+3]
                break
            else:
                ''
        else:
            v=0
        card2=card1
        card1=card1-1
#        print v
    return []
#drawn_cards = draw_cards(3, 1)
#print drawn_cards
#drawn_cards.sort()
#print drawn_cards
#print Straight(drawn_cards)
#------------------------------------------------
#------------------------------------------------
#5 Check for Highest Cards
#------------------------------------------------
def Fivehighestcards(cards):
#    print cards
    cards.sort()
    a = len(cards)
    b = len(cards)-5
    return cards[b:a]
#drawn_cards = draw_cards(3, 1)
#print drawn_cards
#print fivehighestcards(drawn_cards)
#------------------------------------------------
#-------------DIDIWIN----------------------------
#------------------------------------------------
#---ADD CHECKS OTHER THAN FOR PAIRS--------------
#------------------------------------------------
def DidIwin(cards_to_check, hand2check):
    a = 5
    b = 7
    z = []
    while a<len(cards_to_check):
        f = cards_to_check[0:5]+cards_to_check[a:b]
        d = Samecards(f)
        e = Straight(f)
        g = Flush(f)
        h = Fivehighestcards(f)
        i = [d]+[e]+[g]
#        print f
#        print i
#        print max(i)
        z = z+[[max(i),h]]
        j = cards_to_check[0:5]+cards_to_check[a:b]
        k = Samecards(hand2check)
        l = Straight(hand2check)
        m = Flush(hand2check)
        n = Fivehighestcards(hand2check)
        o = [k]+[l]+[m]
        p = [max(o), n]
#        print p
        a = a + 2
        b = b + 2
#    print ''
#    print z
#    print max(z)
    if (p == max(z)):
        return 1
    else:
        return 0
#------------------------------------------------
#-------------TEST ONCE--------------------------
#------------------------------------------------
#cards = Draw_cards(3,1)
#cards_pl1 = cards[0:7]
#print 'Cards being checked'
#print cards
#print cards_pl1
#print 'check DidIWin'
#print DidIwin(cards, cards_pl1)
#print 'check manually'
#print cards_pl1, 'Cards drawn from pile for 1st player'
#print Fivehighestcards(cards_pl1), 'Fivehighestcards for 1st player'
#print Straight(cards_pl1), 'Straight'
#print Flush(cards_pl1), 'Flush'
#print Samecards(cards_pl1), 'Check for same cards i.e. pair, 3 of a kind, carré and Full House'

#------------------------------------------------
#-------------TEST MULTIPLE----------------------
#------------------------------------------------
t, times = 0, 3000
v = 0
while t < times:
    t = t+1
    drawn_cards = Draw_cards(3, 1)
    cards_pl1 = drawn_cards[0:5]+['01c','01d']
#    print cards_pl1
#    print drawn_cards
    cards_in_calc = cards_pl1+drawn_cards[7:]
#    print cards_in_calc
    p = DidIwin(cards_in_calc, cards_pl1)
    v = v+p
#    print v, drawn_cards
print (v*100/times),'%'
