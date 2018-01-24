class SimplePlayer:
    def __init__(self,playertype):
        self.playertype=playertype
        self.reset()
    def reset(self):
        self.games_played=list()
        self.players_played=list()
    def move(self,game):
        #delegate move to playertype
        return self.playertype.move(self,game)
    def record(self,game):
        self.games_played.append(game)
        opponent=game.opponents[self]
        self.players_played.append(opponent)