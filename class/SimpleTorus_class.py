from Appendix_A import *


class SimpleTorus:
    def __init__(self,nrows,ncols,neighborhood):
        self.nrows,self.ncols=nrows,ncols
        self.neighborhood=neighborhood
        #empty dict will eventially map players to neighbors
        self.players2neighbors=dict()
        #create 2d grid (each element is None untill populated)
        self.players2d=[[None]*ncols for i in range(nrows)]
    def populate(self,players1d):
        players=iter(players1d)
        #put a player in each grid location(row,column)
        for row in range(self.nrows):
            for column in range(self.ncols):
                player=next(players)
                self.players2d[row][column]=player
                player.set_grid(self,row,column)
    def get_neighbors(self,player):
        if player in self.players2neighbors:
            neighbors=self.players2neighbors[player]
        else:
            neighbors=compute_neighbors(player,self)
            #map player to computed neighbors (for later use)
            self.players2neighbors[player]=neighbors
        return neighbors