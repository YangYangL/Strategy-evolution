import random

class CDIPlayerType:
    def __init__(self,p_cdi=(0.5,0.5,0.5)):
        self.p_cdi=p_cdi
    def move(self,player,game):
        #get opponent and learn her last move
        opponent=game.opponents[player]
        last_move=game.get_last_move(opponent)
        #respond to opponent's last move
        if last_move is None:
            p_defect =self.p_cdi[-1]
        else:
            p_defect=self.p_cdi[last_move]
        return random.uniform(0,1)<p_defect