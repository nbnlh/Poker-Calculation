import random
def draw_cards(n):
    cards = ['01c','02c','03c','04c','05c','06c','07c','08c','09c','10c','11c','12c','13c','01d','02d','03d','04d','05d','06d','07d','08d','09d','10d','11d','12d','13d','01s','02s','03s','04s','05s','06s','07s','08s','09s','10s','11s','12s','13s','01h','02h','03h','04h','05h','06h','07h','08h','09h','10h','11h','12h','13h']
    a = random.sample(cards, n)
    print a

t, times = 0, 5
while t < times:
    draw_cards(5)
    t = t + 1


