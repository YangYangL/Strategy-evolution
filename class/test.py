from numpy import *

class RandomMover:
    def move(self):
        return random.uniform(0,1)<0.5

##Game:RandomMover
#creat a payoff matrix
PAYOFFMAT=[[(3,3),(0,5)],[(5,0),(1,1)]]

#creat two players
player1=RandomMover()
player2=RandomMover()

#get a move from each player
move1=player1.move()
move2=player2.move()

#retrieve and print the payoffs
pay1,pay2=PAYOFFMAT[move1][move2]
print("player1 payoff:",pay1)
print("player2 payoff:",pay2)

