from SoupPlayer_class import *

class GridPlayer(SoupPlayer):
    def set_grid(self,grid,row,column):
        self.grid=grid
        self.gridlocation=row,column
    def get_neighbors(self):
        return self.grid.get_neighbors(self)
