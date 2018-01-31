import random


def mean(seq):#simplest computation of mean
    """Return mean of value in 'seq'."""
    n=len(seq)
    return sum(seq)/float(n)

def transpose(seqseq):#simplest 2-dimentional transpose
    """Return list of best (maximum payoff) player types."""
    return zip(*seqseq)

def topscore_playertypes(player):
    """Return list of best (maximum payoff) player types."""
    best_types=[player.playertype]
    best_payoff=player.get_payoff()
    for opponent in player.players_played:
        payoff=opponent.get_payoff()
        if payoff>best_payoff:
            best_payoff=payoff
            best_types=[opponent.playertype]
        elif payoff==best_payoff:
            best_types.append(opponent.playertype)
    return best_types


def maxmin_playertypes(player):
    """Return list of best (maxmin payoff) player types."""
    #initialize mapping (playertypes->payoffs)
    pt2po=dict()
    #find minimum payoff for each encountered playertype
    pt2po[player.playertype]=player.get_payoff()
    for n in player.get_neighbors():
        pt,po=n.playertype,n.getpayoff()
        try:
            if pt2po[pt]>po:
                pt2po[pt]=po
        except KeyError:
            pt2po[pt]=po
    #find best playertype (max of minimum payoff)
    maxmin=max(pt2po.items())
    best_playertype=[pt for pt in pt2po if pt2po[pt]==maxmin]
    return best_playertype


def random_pairs_of(players):
    """Return all of players as random pairs."""
    #copy player list
    # for i in iter(players):
    #     print(i)

    players=list(players)
    #shuffle the new player list in place
    random.shuffle(players)
    #yield the shuffled players,2 at a time
    player_iter=iter(players)
    return zip(player_iter,player_iter)


def compute_neighbors(player,grid):
    """Return neighbors of 'player'on 'grid'"""
    player_row,player_col=player.gridlocation
    nrows,ncols=grid.nrows,grid.ncols
    players2d=grid.players2d
    #initialize list of neighbors
    neighbors=list()
    #append all neighbors to list
    for offset in grid.neighborhood:
        dc,dr=offset    #note:x,y neighborhood
        r=(player_row+dr)%nrows
        c=(player_col+dc)%ncols
        neighbor=players2d[r][c]
        neighbors.append(neighbor)
    return neighbors


def count_player_types(players):
    """Return mao (playertype->frequency)for 'players'"""
    ptype_counts = dict(int)   #empty dictionary,default count is 0
    for player in players:
        ptype_counts[player.playertype]+=1
    return ptype_counts


