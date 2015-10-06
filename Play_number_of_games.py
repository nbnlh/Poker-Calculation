t, times = 0, 1000
while t < times:
    drawn_cards = draw_cards(6, 1)
    my_cards = drawn_cards[0:2]
    if my_cards[0] is '01c':
        print 1111
    else:
        print 0
    t = t + 1
