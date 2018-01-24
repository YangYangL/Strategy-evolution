from Appendix_A import *

class SimpleGame:
    def __init__(self, player1, player2, payoffmat):
           # initialize instance attributes
           self.players = [player1, player2]
           self.payoffmat = payoffmat
           self.history = list()

    def run(self, game_iter=4):
           # unpack the two players
           player1, player2 = self.players
           # each iteration,get new moves and append these to history
           for iteration in range(game_iter):
               newmoves = player1.move(self), player2.move(self)
               self.history.append(newmoves)
               print(newmoves,self.payoffmat[player1.move(self)][player2.move(self)])

           # prompt players to record the game played(i.e.,'self')
           player1.record(self)
           player2.record(self)

    def payoff(self):
           # unpack the two players
           player1, player2 = self.players
           # generate a payoff pair for each game iteration
           payoffs = [self.payoffmat[m1][m2] for (m1, m2) in self.history]
           # payoffs = [self.payoffmat[m1][m2] for (m1, m2) in self.history]
           # transpose to get a payoff sequence for each player
           pay1, pay2 = transpose(payoffs)
           # return a mapping of each player to its mean payoff
           return {player1: mean(pay1), player2: mean(pay2)}