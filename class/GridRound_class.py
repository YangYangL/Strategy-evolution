from SoupRound_class import *

class GridRound(SoupRound):
    def run(self):
        payoff_matrix =self.payoffmat
        #each player plays each of its neighbors once
        for player in self.players:
            for neighbor in player.players_played:
                if neighbor not in player.players_played:
                    #creat and run a new game
                    game=CDIGame(player,neighbor,payoff_matrix)
                    game.run()
