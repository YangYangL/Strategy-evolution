from SimplePlayer_class import *
from Appendix_A import *

class SoupPlayer(SimplePlayer):
    # def __init__(self,playertype):
    #     SimplePlayer.__init__(self,playertype)
    #     self.next_playertype=
    def evolve(self):
        self.playertype=self.next_playertype
    def get_payoff(self):
        return sum(game.payoff()[self] for game in self.games_played)
    def choose_next_type(self):
        #find the playertype(s) producing the highest score (s)
        best_playertypes=topscore_playertypes(self)
        #choose randomly from these best playertypes
        self.next_playertype=random.choice(best_playertypes)  #random.choice(self,seq)choose a random element from a non-empty sequence
