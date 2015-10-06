#This Module is going to generate a set of five cards
# c=clubs
# d=diamonds
# s=spades
# h=hearts

import random
print '---WHICH 5 CARDS ARE DRAWN--------'
cards = ['01c','02c','03c','04c','05c','06c','07c','08c','09c','10c','11c',\
         '12c','13c','01d','02d','03d','04d','05d','06d','07d','08d','09d',\
         '10d','11d','12d','13d','01s','02s','03s','04s','05s','06s','07s',\
         '08s','09s','10s','11s','12s','13s','01h','02h','03h','04h','05h',\
         '06h','07h','08h','09h','10h','11h','12h','13h']
a = random.sample(cards, 5)
print a
a = ['01c','02c','03c','04c','06d']

card1 = a.pop()
card2 = a.pop()
card3 = a.pop()
card4 = a.pop()
card5 = a.pop()
print ''
print '---CHECKING IF STATEMENTS FOR SUITS--------'
suit_card1 = card1[2:]
print suit_card1
suit_card2 = card2[2:]
print suit_card2
suit_card3 = card3[2:]
print suit_card3
suit_card4 = card4[2:]
print suit_card4
suit_card5 = card5[2:]
print suit_card5

print ''
print '-----CHECKING IF STATMENTS FOR NUMBERS------'

number_card1 = card1[:2]
print number_card1
number_card2 = card2[:2]
print number_card2
number_card3 = card3[:2]
print number_card3
number_card4 = card4[:2]
print number_card4
number_card5 = card5[:2]
print number_card5

#Check for possible combinations
#1 Check for pairs, 3 of a kind, carre, 2 pairs, full house
#2 Check for Flush
#3 Check for Straight
#4 Flush + Straight = Straight Flush
#5 If none of the above - check for high card
print ''
print 'MAKE LIST OF NUMBERS AND SUITS'
suits = [suit_card1,suit_card2,suit_card3,suit_card4,suit_card5]
print suits
suits.sort()
print suits
numbers = [number_card1,number_card2,number_card3,number_card4,number_card5]
print numbers
numbers.sort()
print numbers
# 1 Check for pairs, 3 of a kind, carre, 2 pairs, full house 
print ''
print 'Check if multiple occurances in list'
print 'Check for pairs, 3 of a kind, carre, 2 pairs, full house'
count1 = numbers.count(number_card1)
count2 = numbers.count(number_card2)
count3 = numbers.count(number_card3)
count4 = numbers.count(number_card4)
count5 = numbers.count(number_card5)
print count1
print count2
print count3
print count4
print count5
print 'check max'
b = (count1, count2, count3, count4, count5)
d = max(b)
print d
print 'number of pairs'
c = b.count(2)
print c/2
print 'number of 3 of a kind'
e = b.count(3)
print e/3
print 'number of carre'
f = b.count(4)
print f/4
print 'full house'
print (c + e) / 5
#2 Check for Flush
print 'Check for Flush'
print suits[0]
print suits[4]
if suits[0] is suits[4]:
    print 'FLUSH'
else:
    print 'NO FLUSH'
#3 Check for Straight
print int(numbers[4])
print int(numbers[3])
print int(numbers[2])
print int(numbers[1])
print int(numbers[0])
if int(numbers[4])-int(numbers[3])==1 and\
   int(numbers[3])-int(numbers[2])==1 and\
   int(numbers[2])-int(numbers[1])==1 and\
   int(numbers[1])-int(numbers[0])==1:
    print 'STRAIGHT'
else:
    print 'NO STRAIGHT'
#4 Flush + Straight = Straight Flush
# if and flush and straight == Straight Flush
#5 If none of the above - check for high card
# if not 1 and not 2 and not 3 then look for high card
