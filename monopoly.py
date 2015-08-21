import random #imports random library.

#Write your monopoly dice roller app here!
#You can make use of random.randint()
class Die(object):
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

dice = [Die(6), Die(6)]

for die in dice:
    print die.roll()

die = random.randint(1, 6)
die2 = random.randint(1, 6)
move = die + die2
if die == die2:
    print "Doubles! " + "Move " + str(move) + " spaces and roll again "
    die = random.randint(1, 6)
    die2 = random.randint(1, 6)
else:
    print "Move " + str(move) + " spaces." + " Next player\'s turn"
