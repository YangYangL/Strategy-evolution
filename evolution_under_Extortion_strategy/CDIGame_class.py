from SimpleGame_class import *

class CDIGame(SimpleGame):
    def __init__(self,player1,player2,payoffmat):
        #begin initialization with '__init__' from SimpleGame
        SimpleGame.__init__(self,player1,player2,payoffmat)
        self.opponents={player1:player2,player2:player1}
    def get_last_move(self,player):
        #if history not empty,return prior move of 'player'
        if self.history:
            player_idx=self.players.index(player)
            last_move=self.history[-1][player_idx]
            print(player_idx,last_move)
        else:
            last_move=None
            print("last_move=None")
        return last_move